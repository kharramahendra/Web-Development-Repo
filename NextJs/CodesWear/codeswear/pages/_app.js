import { useEffect, useState } from 'react'
import Footer from '../components/footer'
import { useRouter } from 'next/router'
import Navbar from '../components/navbar'
import '../styles/globals.css'
import Script from 'next/script'
import LoadingBar from 'react-top-loading-bar'


function MyApp({ Component, pageProps }) {
  const router = useRouter()
  const [cart ,setCart] = useState({})
  const [subTotal,setSubTotal] = useState(0)
  const [user,setUser] = useState({value:null})
  const [key,setKey] = useState(0)
  const [progress, setProgress] = useState(0)

  useEffect(()=>{
    router.events.on('routeChangeStart',()=>{
      setProgress(40)
    })
    router.events.on('routeChangeComplete',()=>{
      setProgress(100)
    })

    try{
      if (localStorage.getItem("cart")){
        setCart(JSON.parse(localStorage.getItem("cart")))
        saveCart(JSON.parse(localStorage.getItem("cart")))
      }
    }catch (error){
      localStorage.clear()
    }
    const myuser = JSON.parse(localStorage.getItem('myuser'))
    if(myuser){
      setUser({token:myuser.token,email:myuser.email})
    }
    setKey(Math.random())
  },[router.query])

  const logout = ()=>{
    localStorage.removeItem('myuser')
    setUser({value:null})
    setKey(Math.rendom)
    router.push("/")
  }

  const saveCart = (myCart)=>{
    localStorage.setItem("cart",JSON.stringify(myCart));
    let subt = 0;
    let keys = Object.keys(myCart)
    for (let i = 0;i<keys.length;i++){
      subt += myCart[keys[i]].price * myCart[keys[i]].qty
    }
    setSubTotal(subt)

  }

  const addtoCart = (itemCode,qty,price,name,size,variant)=>{
    let newCart = cart;
    if(itemCode in cart){
      newCart[itemCode].qty = cart[itemCode].qty + qty
    }else{
      newCart[itemCode] = {qty:1,price,name,size,variant}
    }
    setCart(newCart)
    saveCart(newCart)
    console.log(cart)
  }

  const buyNow = (itemCode,qty,price,name,size,variant)=>{
    let newCart = {}
    newCart[itemCode] = {qty:1,price,name,size,variant}
    setCart(newCart)
    saveCart(newCart)
    router.push('/checkout')
  }
  

  const clearCart = ()=>{
    setCart({})
    saveCart({})
  }

  const removeFromCart = (itemCode,qty,price,name,size,variant)=>{
    let newCart = JSON.parse(JSON.stringify(cart));
    if(itemCode in cart){
      newCart[itemCode].qty = cart[itemCode].qty - qty
    }
    if(newCart[itemCode]["qty"]<=0){
      delete newCart[itemCode]
    }
    setCart(newCart)
    saveCart(newCart)
  }


  return<>
  <Script src="https://cdn.tailwindcss.com"/>
  <LoadingBar
        color='#f11946'
        progress={progress}
        waitingTime={400}
        onLoaderFinished={() => setProgress(0)}
      />
  <Navbar logout={logout} user={user} key={key} cart={cart} addtoCart={addtoCart} removeFromCart={removeFromCart} clearCart={clearCart} subTotal={subTotal}/>
  <Component cart={cart} addtoCart={addtoCart} removeFromCart={removeFromCart} buyNow={buyNow} clearCart={clearCart} subTotal={subTotal} {...pageProps} /> 
  <Footer/></>
}

export default MyApp
