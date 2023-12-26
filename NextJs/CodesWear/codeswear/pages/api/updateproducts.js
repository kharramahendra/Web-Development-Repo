import Product from "../../models/Product"
import connectDb from "../../middleware/mongoose"


const handler = async (req,res)=>{
    if(req.method == 'POST'){
        for (let i = 0;i<req.body.length;i++){
            let p = await Product.findByIdAndUpdate(req.body[i]._id,req.body[i])
            //await p.save()
        }
        res.status(400).json({success:"success"})
        
    }
    else{
        res.status(400).json({error:"error"})
    }

}

export default connectDb(handler);