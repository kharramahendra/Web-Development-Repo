import React from 'react'
import { AiFillCloseCircle, AiFillMinusCircle, AiFillPlusCircle, AiOutlineShoppingCart } from 'react-icons/ai';
import { BsFillBagCheckFill } from 'react-icons/bs'
import Head from 'next/head'
import Script from 'next/dist/client/script';
import { useState } from 'react';
import Link from 'next/dist/client/link';
import { useEffect } from 'react';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { userAgent } from 'next/server';
import { Router } from 'next/router';

const Checkout = ({cart, clearCart, removeFromCart, addtoCart, subTotal }) => {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [phone, setPhone] = useState('')
  const [address, setAddress] = useState('')
  const [pincode, setPincode] = useState('')
  const [city, setCity] = useState('')
  const [state, setState] = useState('')
  const [disabled, setDisabled] = useState(true)
  const [user, setUser] = useState(null)



  useEffect(() => {
    const myuser = JSON.parse(localStorage.getItem('myuser'))
    if(myuser && myuser.token){
      setUser(myuser)
      setEmail(myuser.email)
      fetchData(myuser.token)
    }
    }, [])
    const fetchData = async (token) => {
      let data = { token: token }
      let a = await fetch(`${process.env.NEXT_PUBLIC_HOST}/api/getuser`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
      let res = await a.json()
      console.log(res)
      setName(res.name)
      setAddress(res.address)
      setPincode(res.pincode)
      setPhone(res.phone)
      getPincode(res.pincode)
  
    }

    const getPincode = async (pin)=>{
      let pins = await fetch(`${process.env.NEXT_PUBLIC_HOST}/api/pincode`)
        let pinJson = await pins.json()
        if (Object.keys(pinJson).includes(pin)) {
          setState(pinJson[pin][1])
          setCity(pinJson[pin][0])
        }
        else {
          setState('')
          setCity('')
        }
    }

  const handleChange = async (e) => {

    if (e.target.name == 'name') {
      setName(e.target.value)
    }
    else if (e.target.name == 'email') {
      setEmail(e.target.value)
    }
    else if (e.target.name == 'phone') {
      setPhone(e.target.value)
    }
    else if (e.target.name == 'address') {
      setAddress(e.target.value)
    }
    else if (e.target.name == 'pincode') {
      setPincode(e.target.value)
      if (e.target.value.length == 6) {
        let pins = await fetch(`${process.env.NEXT_PUBLIC_HOST}/api/pincode`)
        let pinJson = await pins.json()
        console.log()
        if (Object.keys(pinJson).includes(e.target.value)) {
          setState(pinJson[e.target.value][1])
          setCity(pinJson[e.target.value][0])
        }
        else {
          setState('')
          setCity('')
        }
      } else {
        setState('')
        setCity('')
      }
    }
    if (name.length > 3 && email.length > 3 && phone.length > 3 && address.length > 3 && pincode.length > 3) {
      setDisabled(false)
    }
  }


  const initiatePayment = async () => {
    let oid = Math.floor(Math.random() * Date.now());
    //get a transaction token
    const data = { cart, subTotal, oid, email: email, name, address, pincode, phone ,city,state}
    let a = await fetch(`${process.env.NEXT_PUBLIC_HOST}/api/pretransaction`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    let txnRes = await a.json()
    console.log(txnRes)

    if (txnRes.success) {
      let txnToken = txnRes.txnToken

      var config = {
        "root": "",
        "flow": "DEFAULT",
        "data": {
          "orderId": oid, /* update order id */
          "token": txnToken, /* update token value */
          "tokenType": "TXN_TOKEN",
          "amount": subTotal /* update amount */
        },
        "handler": {
          "notifyMerchant": function (eventName, data) {
            console.log("notifyMerchant handler function called");
            console.log("eventName => ", eventName);
            console.log("data => ", data);
          }
        }
      };

      console.log("error at 95")

      window.Paytm.CheckoutJS.init(config).then(function onSuccess() {
        window.Paytm.CheckoutJS.invoke();
      }).catch(function onError(error) {
        console.log("error => ", error);
      });
    }
    else {
      if(txnRes.clear==true){
      clearCart()
      toast.error(txnRes.error, {
        position: "bottom-right",
        autoClose: 2000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
      });
    }
  else{
    toast.error(txnRes.error, {
      position: "bottom-right",
      autoClose: 2000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    });
  }}
  }





  return (
    <div className='container m-auto mx-2'>
      <ToastContainer
        position="bottom-right"
        autoClose={2000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
      />
      <Head><meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, maximum-scale=1.0" /></Head>
      <Script type="application/javascript" crossorigin="anonymous" src={`${process.env.NEXT_PUBLIC_PAYTM_HOST}/merchantpgpui/checkoutjs/merchants/${process.env.NEXT_PUBLIC_PAYTM_MID}.js`} />

      <h1 className='font-bold text-3xl my-8 text-center'>Checkout</h1>
      <h2 className='font-semibold text-xl'>1.Delivery Details</h2>
      <div className='mx-auto flex my-4'>
        <div className='px-2 w-1/2'>
          <div className='mb-4'>
            <label htmlFor="name" className="leading-7 text-sm text-gray-600">Name</label>
            <input onChange={handleChange} value={name} type="text" id="name" name="name" className="w-full bg-white rounded border border-gray-300 focus:border-pink-500 focus:ring-2 focus:ring-pink-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" />
          </div>
        </div>
        <div className='px-2 w-1/2'>
          <div className='mb-4'>
            <label htmlFor="email" className="leading-7 text-sm text-gray-600">Email</label>
            {user && user.token ? <input onChange={handleChange} value={user.email} type="email" id="email" name="email" className="w-full bg-white rounded border border-gray-300 focus:border-pink-500 focus:ring-2 focus:ring-pink-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" readOnly={true} />
              :<input onChange={handleChange} value={email} type="email" id="email" name="email" className="w-full bg-white rounded border border-gray-300 focus:border-pink-500 focus:ring-2 focus:ring-pink-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" />
            }
          </div>
        </div>
      </div>
      <div className='px-2 w-full'>
        <div className='mb-4'>
          <label htmlFor="address" className="leading-7 text-sm text-gray-600">Adderess</label>
          <textarea onChange={handleChange} value={address} name="address" cols="30" rows="2" id="address" className="w-full bg-white rounded border border-gray-300 focus:border-pink-500 focus:ring-2 focus:ring-pink-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" />
        </div>
      </div>
      <div className='mx-auto flex my-4'>
        <div className='px-2 w-1/2'>
          <div className='mb-4'>
            <label htmlFor="phone" className="leading-7 text-sm text-gray-600">10 Digit Phone</label>
            <input onChange={handleChange} value={phone} type="number" id="phone" name="phone" className="w-full bg-white rounded border border-gray-300 focus:border-pink-500 focus:ring-2 focus:ring-pink-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" />
          </div>
        </div>
        <div className='px-2 w-1/2'>
          <div className='mb-4'>
            <label htmlFor="pincode" className="leading-7 text-sm text-gray-600">Pincode</label>
            <input onChange={handleChange} value={pincode} type="number" id="" name="pincode" className="w-full bg-white rounded border border-gray-300 focus:border-pink-500 focus:ring-2 focus:ring-pink-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" />

          </div>
        </div>
      </div>
      <div className='mx-auto flex my-4'>
        <div className='px-2 w-1/2'>
          <div className='mb-4'>
            <label htmlFor="state" className="leading-7 text-sm text-gray-600">State</label>
            <input onChange={handleChange} type="text" value={state} id="state" name="state" className="w-full bg-white rounded border border-gray-300 focus:border-pink-500 focus:ring-2 focus:ring-pink-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" />
          </div>
        </div>
        <div className='px-2 w-1/2'>
          <div className='mb-4'>
            <label htmlFor="city" className="leading-7 text-sm text-gray-600">District</label>
            <input onChange={handleChange} type="text" id="city" value={city} name="city" className="w-full bg-white rounded border border-gray-300 focus:border-pink-500 focus:ring-2 focus:ring-pink-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out" />

          </div>
        </div>

      </div>


      <h2 className='font-semibold text-xl'>2.Review Cart Items and Pay</h2>
      <div className=' bg-pink-100 p-10 mx-4'>
        <ol className='list-decimal'>
          {Object.keys(cart).length == 0 &&
            <div className='my-4 text-base font-normal'>Your cart is empty</div>
          }
          {Object.keys(cart).map((k) => {
            return <li key={k}>
              <div className='flex my-3 item'>
                <div className=' font-semibold'>{cart[k].name}</div>
                <div className='flex fomt-semibold items-center justify-center w-1/3 text-lg'><AiFillMinusCircle onClick={() => {
                  removeFromCart(k, 1, cart[k].price, cart[k].name, cart[k].size, cart[k].varient);
                }} className='cursor-pointer text-pink-500' /> <span className='mx-2'>{cart[k].qty}</span> <AiFillPlusCircle onClick={() => {
                  addtoCart(k, 1, cart[k].price, cart[k].name, cart[k].size, cart[k].varient);
                }} className='cursor-pointer text-pink-500' />
                </div>
              </div>
            </li>
          })}
        </ol>
        <span className='total font-bold'> subtotal:{subTotal}</span>
      </div>
      <div className='container m-4'>
        <Link href={'/checkout'}><button onClick={initiatePayment} disabled={disabled} className="disabled:bg-pink-300 flex mr-2 text-white bg-pink-500 border-0 py-2 px-2 focus:outline-none hover:bg-pink-600 rounded text-sm"><BsFillBagCheckFill className='m-1' />PAY</button></Link>
      </div>
    </div>
  )
}

export default Checkout