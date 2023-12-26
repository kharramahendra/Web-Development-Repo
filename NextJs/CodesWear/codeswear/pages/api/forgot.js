import Forgot from "../../models/Forgot"


export default function handler(req, res) {
    //check if user exist in databse
    let token = `ieuwh rinhriohoiehqr oqh`;
    let forgot = new Forgot({
        email:req.body.email,
        token:token,
    })
    let eemail = `<span style="font-size: 12px; line-height: 1.5; color: #333333;">

    We have sent you this email in response to your request to reset your password on CodesWear.com. After you reset your password, any credit card information stored in My Account will be deleted as a security measure.

    <br/><br/>

    To reset your password for <a href="http://localhost:3000/forgot?token=${token}">Click here</a>, please follow the link below:

    <a href="${reset-password-url}">Click here to reset your password</a>

    <br/><br/>

    We recommend that you keep your password secure and not share it with anyone.If you feel your password has been compromised, you can change it by going to your   __  My Account Page and clicking on the "Change Email Address or Password" link.

   

</span>`
    res.status(200).json({ name: 'John Doe' })
  }
  