import { request } from 'http';
import Order from "../../models/Order"
import connectDb from "../../middleware/mongoose"
import Product from "../../models/Product"
const https = require('https');
const PaytmChecksum = require("paytmchecksum");
import pincodes from '../../pincodes.json'



const handler = async (req,res)=>{
    if (req.method == 'POST') {
       ///ALL CHECKS FOR ORDER PLACEMENT 
        
        //check if pincode is serviceable
        if(!Object.keys(pincodes).includes(req.body.pincode)){
            res.status(200).json({success:false,"error":'The pincode you have entered is not  serviceable!'})
        }
        //check if cart temporred
        let product,sumTotal = 0;
        //check if cart is empty
        if(req.body.subTotal<=0){
            res.status(200).json({success:false,"error":"Please build your cart and try again!",clear:true})
            return
        }
        //check if cart temporred
        for (let item in req.body.cart){
            sumTotal+=req.body.cart[item].price*req.body.cart[item].qty
            product = await Product.findOne({slug:item})
            //check if any product in cart is out of stock
            if(product.availableQty<req.body.cart[item].qty){
                res.status(200).json({success:false,"error":"Some items in your cart went out of stock.Please try again",clear:true})
                return
            }
            if(product.price != req.body.cart[item].price){
                res.status(200).json({success:false, 'error':"The price of some items in your cart has changed.Please try again",clear:true})
                return
            }
        }
        if (sumTotal!=req.body.subTotal){
            res.status(200).json({success:false, 'error':"The price of some items in your cart has changed.Please try again",clear:true})
            return
        }
        //check if details are valid or not
        if(req.body.phone.length!==10 || !Number.isInteger(Number(req.body.phone))){
            res.status(200).json({success:false,"error":"Please enter your 10 digit Phone number!",clear:false})
            return
        }
        if(req.body.pincode.length!==6 || !Number.isInteger(Number(req.body.pincode))){
            res.status(200).json({success:false,"error":"Please enter your 6 digit Pincode!",clear:false})
            return
        }




    //INITIATE THE ORDER
        let order = new Order({
            email:req.body.email,
            name:req.body.name,
            orderId:req.body.oid,
            address:req.body.address,
            phone:req.body.phone,
            city:req.body.city,
            state:req.body.state,
            pincode:req.body.pincode,
            amount:req.body.subTotal,
            products:req.body.cart
        })
        await order.save()
        var paytmParams = {};

        paytmParams.body = {
            "requestType": "Payment",
            "mid": process.env.NEXT_PUBLIC_PAYTM_MID,
            "websiteName": "YOUR_WEBSITE_NAME",
            "orderId": req.body.oid,
            "callbackUrl": `${process.env.NEXT_PUBLIC_HOST}/api/posttransaction`,
            "txnAmount": {
                "value": req.body.subTotal,
                "currency": "INR",
            },
            "userInfo": {
                "custId": req.body.email,
            },
        };

        const checksum = await PaytmChecksum.generateSignature(JSON.stringify(paytmParams.body), process.env.NEXT_PUBLIC_PAYTM_MKEY) 

            paytmParams.head = {
                "signature": checksum
            };

            var post_data = JSON.stringify(paytmParams);

            const requestAsync = async () => {
                return new Promise((resolve, reject) => {
                    var options = {
                        hostname: 'securegw.paytm.in',
                        port: 443,
                        path: `/theia/api/v1/initiateTransaction?mid=${process.env.NEXT_PUBLIC_PAYTM_MID}&orderId=${req.body.oid}`,
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Content-Length': post_data.length
                        }
                    };
                    var response = "";
                    var post_req = https.request(options, function (post_res) {
                        post_res.on('data', function (chunk) {
                            response += chunk;
                        });

                        post_res.on('end', function () {
                            let ress = JSON.parse(response).body
                            ress.success=true
                            resolve(ress)
                        });
                    });
                    post_req.write(post_data);
                    post_req.end();
                })
            }

            let myr = await requestAsync()
            res.status(200).json(myr);
    }
}

export default connectDb(handler);