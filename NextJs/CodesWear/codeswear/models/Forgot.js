const mongoose = require('mongoose');

const ForgotSchima = new mongoose.Schema({
    userid:{type:String,required:true},
    email:{type:String,required:true,unique:true},
    token:{type:String,required:true}
},{timestamps:true})

mongoose.models = {}

export default mongoose.model("Forgot",ForgotSchima)