import Order from "../../models/Order";
import connectDb from "../../middleware/mongoose";
import Product from "../../models/Product";
import PaytmChecksum from "paytmchecksum";

const handler = async (req, res) => {
  let order;


  //PAYTM CHECKSUM  
  var paytmChecksum = "";
  var paytmParams = {}
  const received_data = req.body
  console.log("DATA ",received_data)
  for (var key in received_data) {
    if (key == 'CHECKSUMHASH') {
      paytmChecksum = received_data.CHECKSUMHASH
    }
    else {
      paytmParams[key] = received_data[key];
    }
  }
  
  console.log("paytm params",paytmParams)
  console.log("checksum",paytmChecksum)
  var isValidChecksum = PaytmChecksum.verifySignature(paytmParams, process.env.NEXT_PUBLIC_PAYTM_MKEY, paytmChecksum);
  if (!isValidChecksum) {
    res.status(500).send("Some error Occured")
    return
  }




  //final finishing
  if (req.body.STATUS == 'TXN_SUCCESS') {
    order = await Order.findOneAndUpdate({ orderId: req.body.ORDERID }, { status: "Paid", paymentInfo: JSON.stringify(req.body) })
    let products = order.products
    for (let slug in products) {
      await Product.findOneAndUpdate({ slug: slug }, { $inc: { "availableQty": -products[slug].qty } })
    }
  }
  else if (req.body.STATUS == 'pending') {
    order = await Order.findOneAndUpdate({ orderId: req.body.ORDERID }, { status: "Pending", paymentInfo: JSON.stringify(req.body) })

  }

  res.redirect('/order?clearCart=1&id=' + order._id, 200)

}

export default connectDb(handler);