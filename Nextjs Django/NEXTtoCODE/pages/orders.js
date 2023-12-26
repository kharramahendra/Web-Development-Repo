import React from 'react'
import { useEffect } from 'react'
import { useRouter } from 'next/router'
import { useState } from 'react'
import Link from 'next/dist/client/link';

const Orders = () => {
  const [orders, setOrders] = useState([])

  const router = useRouter()
  useEffect(() => {
    const fetchorder = async () => {
      // `${process.env.NEXT_PUBLIC_HOST}/api/myorders
      let a = await fetch('http://127.0.0.1:8000/myorders/', {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ token : JSON.parse(localStorage.getItem('myuser')).token})
      })
      let res = await a.json()
      // let orders = JSON.parse(JSON.stringify(res.orders))
      setOrders(res.orders)
    }
    if (!localStorage.getItem('myuser')) {
      router.push('/')
    }
    else {
      fetchorder()

    }




  }, [router.query])
  return (
    <div>
      <h1 className='font-semibold text-center p-8 text-2xl'>My Orders</h1>
      <div className='container mx-auto '>
        <div className="flex flex-col">
          <div className="overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div className="py-2 inline-block min-w-full sm:px-6 lg:px-8">
              <div className="overflow-hidden">
                <table className="min-w-full">
                  <thead className="bg-white border-b">
                    <tr>
                      <th scope="col" className="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                        #Order Id
                      </th>
                      <th scope="col" className="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                        Name
                      </th>
                      <th scope="col" className="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                        Amount
                      </th>
                      <th scope="col" className="text-sm font-medium text-gray-900 px-6 py-4 text-left">
                        Details
                      </th>
                    </tr>
                  </thead>
                  <tbody>

                    {orders.map((item)=>{
                      return  <tr key={item._id} className="bg-gray-100 border-b">
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{item.orderId}</td>
                      <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                        {item.email}
                      </td>
                      <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                        {item.amount}
                      </td>
                      <td className="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap">
                        <Link href={'/order?id=' + item.orderId}><a>Details</a></Link>
                      </td>
                    </tr>
                    })}
                   

                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}




export default Orders