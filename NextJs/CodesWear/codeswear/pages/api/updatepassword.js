import User from "../../models/User"
import connectDb from "../../middleware/mongoose"
import jsonwebtoken from "jsonwebtoken"

var AES = require("crypto-js/aes");
var CryptoJS = require('crypto-js')


const handler = async (req,res)=>{
    if(req.method=='POST'){
        let token = req.body.token
        let user = jsonwebtoken.verify(token,process.env.NEXT_PUBLIC_JWT_SECRET)
        let dbuser = await User.findOne({email:user.email})
        const bytes = CryptoJS.AES.decrypt(dbuser.password,process.env.NEXT_PUBLIC_AES_SECRET);
        let decryptedPass = bytes.toString(CryptoJS.enc.Utf8)
        if(decryptedPass == req.body.password && req.body.npassword == req.body.cpassword){
            dbuser = await User.findOneAndUpdate({email:user.email},{password:CryptoJS.AES.encrypt(req.body.npassword,process.env.NEXT_PUBLIC_AES_SECRET).toString()})
            res.status(200).json({ success:true,})
            return
        }
        res.status(200).json({ success:false,})
    }
    else{
        res.status(400).json({error:"error"})
    }
}
export default connectDb(handler);