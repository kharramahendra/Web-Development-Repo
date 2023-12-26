import User from "../../models/User"
import connectDb from "../../middleware/mongoose"
var jwt = require('jsonwebtoken')
var AES = require("crypto-js/aes");
var CryptoJS = require('crypto-js')

const handler = async (req,res)=>{
    if(req.method == 'POST'){
        console.log(req.body)
        let user = await User.findOne({"email":req.body.email})
        const bytes = CryptoJS.AES.decrypt(user.password,process.env.NEXT_PUBLIC_AES_SECRET);
        let decryptedPass = bytes.toString(CryptoJS.enc.Utf8)
        console.log(decryptedPass)
        if (user){
            if(req.body.password == decryptedPass){
                var token = jwt.sign({email:user.email,name:user.name},process.env.NEXT_PUBLIC_JWT_SECRET,{expiresIn:"2d"})
                res.status(200).json({success:true,token,email:user.email})
            }
            else{
                res.status(200).json({success:false,error:"Invalid credentials"})
            }
        }
        res.status(200).json({success:true,error:"No user found"})

        
    }
    else{
        res.status(400).json({error:"error"})
    }

}

export default connectDb(handler);