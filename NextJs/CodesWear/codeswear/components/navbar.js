import React from 'react'
import Image from 'next/image'
import Link from 'next/link'
import { useRef } from 'react';
import Script from 'next/dist/client/script';
import { AiFillCloseCircle, AiFillMinusCircle, AiFillPlusCircle, AiOutlineShoppingCart } from 'react-icons/ai';
import { BsFillBagCheckFill } from 'react-icons/bs'
import { MdAccountCircle } from 'react-icons/md'
import { useState } from 'react';
import { useEffect } from 'react';
import { useRouter } from 'next/dist/client/router';

const Navbar = ({ logout, user, cart, addtoCart, removeFromCart, clearCart, subTotal }) => {
  const [dropdown, setDropdown] = useState(false)
  const [sidebar, setSidebar] = useState()
  const router = useRouter()
  useEffect(() => {
    Object.keys(cart).length !== 0 && setSidebar(true)
    let exempted = ['/checkout', '/order', '/orders']
    if (exempted.includes(router.pathname)) {
      setSidebar(false)
    }
  }, [])


  const toggledropdown = () => {
    setDropdown(!dropdown)
  }
  const toggleCart = () => {
    setSidebar(!sidebar)
    // if (ref.current.classList.contains('translate-x-full')) {
    //   ref.current.classList.remove('translate-x-full')
    //   ref.current.classList.add('translate-x-0')
    // }
    // else if (ref.current.classList.contains('translate-x-0')) {
    //   ref.current.classList.remove('translate-x-0')
    //   ref.current.classList.add('translate-x-full')
    // }
  }
  const ref = useRef()
  return (
    <>
      <span >
        {dropdown && <div onMouseOver={() => { setDropdown(true) }} onMouseLeave={() => { setDropdown(false) }} className='fixed right-5 bg-white shadow-lg top-6 rounded-md px-5 w-32 z-20'>
          <ul className='cursor-pointer'>
            <Link href={'/myaccount'}><li className='py-1 font-bold text-sm hover:text-pink-700'>My account</li></Link>
            <Link href={'/orders'}><li className='py-1 font-bold text-sm hover:text-pink-700'>Orders</li></Link>
            <li onClick={logout} className='py-1 font-bold text-sm hover:text-pink-700'>Logout</li>
          </ul>
        </div>}
      </span>



      <div className={`flex flex-col md:flex-row justify-center shadow-md py-2 items-center sticky top-0 bg-white z-10 ${!sidebar && 'overflow-hidden'}`}>
        <div className='logo mx-5'>
          <Link href={'/'}><a><Image src="/vercel.svg" width={200} height={40} alt="" /></a></Link>
        </div>
        <div className='nav'>
          <ul className='flex items-center  space-x-6 font-bold md:text-xl'>
            <Link href={'/tshirts'}><a><li className='hover:text-pink-600'>Tshirts</li></a></Link>
            <Link href={'/hoodies'}><a><li className='hover:text-pink-600'>Hoodies</li></a></Link>
            <Link href={'/stickers'}><a><li className='hover:text-pink-600'>Stickers</li></a></Link>
            <Link href={'/mugs'}><a><li className='hover:text-pink-600'>Mugs</li></a></Link>
          </ul>
        </div>
        <div className='cart absolute cursor-pointer right-0 top-0 mx-5 z-10 flex'>

          <span onMouseOver={() => { setDropdown(true) }}>
            {user.value && <MdAccountCircle onMouseOver={toggledropdown} onMouseLeave={toggledropdown} className='hover:text-pink-600 cursor-pointer text-xl md:flex mx-2' />}
          </span>


          {!user.value && <Link href={'/login'}><a>
            <button className='bg-pink-700 rounded-md text-sm px-2 py-1 text-white mx-2'>Login</button>
          </a></Link>}

          <AiOutlineShoppingCart onClick={toggleCart} className='hover:text-pink-500 cursor-pointer md:text-3xl' />
        </div>


        <div ref={ref} className={` w-72 h-[100vh] sideCart overflow-y-scroll absolute top-0 ${sidebar ? 'right-0' : '-right-96'} bg-pink-100 py-10 px-8 transition-all z-30`}>
          <h2 className='font-bold text-xl text-center'>Shopping cart</h2>
          <span onClick={toggleCart} className='absolute top-5 right-2 text-2xl cursor-pointer text-pink-500 '><AiFillCloseCircle /></span>
          <ol className='list-decimal'>
            {Object.keys(cart).length == 0 &&
              <div className='my-4 text-base font-normal'>Your cart is empty</div>
            }
            {Object.keys(cart).map((k) => {
              return <li key={k}>
                <div className='flex my-3 item'>
                  <div className='w-2/3 font-semibold'>{cart[k].name}({cart[k].size}/{cart[k].variant})</div>
                  <div className='flex fomt-semibold items-center justify-center w-1/3 text-lg'><AiFillMinusCircle onClick={() => {
                    removeFromCart(k, 1, cart[k].price, cart[k].name, cart[k].size, cart[k].variant)
                  }} className='cursor-pointer text-pink-500' /> <span className='mx-2'>{cart[k].qty}</span> <AiFillPlusCircle onClick={() => {
                    addtoCart(k, 1, cart[k].price, cart[k].name, cart[k].size, cart[k].variant)
                  }} className='cursor-pointer text-pink-500' /></div>
                </div>
              </li>

            })}
            <div className='total font-bold my-2'> subtotal:{subTotal}</div>


            <div className='flex'>
              <Link href={'/checkout'}><button disabled={Object.keys(cart).length === 0} className="flex mr-2 text-white disabled:bg-pink-300 bg-pink-600 border-0 py-2 px-2 focus:outline-none hover:bg-pink-600 rounded text-sm"><BsFillBagCheckFill className='m-1' /> Checout</button></Link>
              <button onClick={clearCart} disabled={Object.keys(cart).length === 0} className="flex mr-2 text-white disabled:bg-pink-300 bg-pink-600 border-0 py-2 px-2 focus:outline-none hover:bg-pink-600 rounded text-sm">Clear Cart</button>
            </div>
          </ol>

        </div>
      </div></>
  )
}

export default Navbar