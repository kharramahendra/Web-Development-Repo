const mongoose = require('mongoose');

const userSchima = new mongoose.Schema({
    name:{type:String,required:true},
    email:{type:String,required:true,unique:true},
    phone:{type:String,required:true,default:''},
    password:{type:String,required:true},
    address:{type:String,required:true,default:""},
    pincode:{type:String,required:true,default:""}
},{timestamps:true})

mongoose.models = {}

export default mongoose.model("User",userSchima)