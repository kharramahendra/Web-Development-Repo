import User from "../../models/User"
import connectDb from "../../middleware/mongoose"
var AES = require("crypto-js/aes");
var CryptoJS = require('crypto-js')

const handler = async (req,res)=>{
    if(req.method == 'POST'){
        console.log(req.body)
        const { name,email } = req.body
        let u = new User({name,email,password:CryptoJS.AES.encrypt(req.body.password,process.env.NEXT_PUBLIC_AES_SECRET).toString()})
        await u.save()
        res.status(400).json({success:"success"})
        
    }
    else{
        res.status(400).json({error:"error"})
    }

}

export default connectDb(handler);