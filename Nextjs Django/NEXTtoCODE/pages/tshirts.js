import React from 'react'
import Link from 'next/dist/client/link'
const Tshirts = ({ products }) => {
  return (
    <div>
      <section className="text-gray-600 body-font">
        <div className="container px-5 py-24 mx-auto">
          <div className="flex flex-wrap justify-center">
            {Object.keys(products).map((item) => {
              return <Link passHref={true} key={products[item]._id} href={`/product/${products[item].slug}`}>
                <div className="lg:w-1/5 md:w-1/2 p-4 w-full cursor-pointer shadow-lg mx-2">
                  <a className="block relative rounded overflow-hidden">
                    <img alt="ecommerce" className="h-[36vh] block m-auto" src={products[item].img} />
                  </a>
                  <div className="mt-4 text-center md:text-left">
                    <h3 className="text-gray-500 text-xs tracking-widest title-font mb-1">Tshirts</h3>
                    <h2 className="text-gray-900 title-font text-lg font-medium">{products[item].title}</h2>
                    <p className="mt-1">₹{products[item]['price']}</p>
                    <div className='mt-1'>

                      {products[item].size.includes('S') && <span className='border border-gray-600 px-1 mx-1'>S</span>}
                      {products[item].size.includes('M') && <span className='border border-gray-600 px-1 mx-1'>M</span>}
                      {products[item].size.includes('L') && <span className='border border-gray-600 px-1 mx-1'>L</span>}
                      {products[item].size.includes('XL') && <span className='border border-gray-600 px-1 mx-1'>XL</span>}
                      {products[item].size.includes('XXL') && <span className='border border-gray-600 px-1 mx-1'>XXL</span>}
                    </div>
                    <div className='mt-1'>
                      {products[item].color.includes('red') && <button className="border-2 border-gray-300 ml-1 bg-red-700 rounded-full w-6 h-6 focus:outline-none"></button>}
                      {products[item].color.includes('blue') && <button className="border-2 border-gray-300 ml-1 bg-blue-700 rounded-full w-6 h-6 focus:outline-none"></button>}
                      {products[item].color.includes('green') && <button className="border-2 border-gray-300 ml-1 bg-green-700 rounded-full w-6 h-6 focus:outline-none"></button>}
                      {products[item].color.includes('cyan') && <button className="border-2 border-gray-300 ml-1 bg-cyan-700 rounded-full w-6 h-6 focus:outline-none"></button>}

                    </div>

                  </div>
                </div>
              </Link>

            })}

          </div>
        </div>
      </section>
    </div>
  )
}



export async function getServerSideProps(context) {
  // if (!mongoose.connections[0].readyState) {
  //   await mongoose.connect("mongodb://localhost:27017/codeswear")
  // }
  // let products = await Product.find({ category: "tshirts" })
  // let tshirts = {}
  // for (let item of products) {
  //   if (item.title in tshirts) {
  //     if (!tshirts[item.title].color.includes(item.color) && item.availableQty > 0) {
  //       tshirts[item.title].color.push(item.color)
  //     }
  //     if (!tshirts[item.title].size.includes(item.size) && item.availableQty > 0) {
  //       tshirts[item.title].size.push(item.size)
  //     }
  //   }
  //   else {
  //     tshirts[item.title] = JSON.parse(JSON.stringify(item))
  //     if (item.availableQty > 0) {
  //       tshirts[item.title].color = [item.color]
  //       tshirts[item.title].size = [item.size]
  //     }
  //     else {
  //       tshirts[item.title].color = []
  //       tshirts[item.title].size = []
  //     }
  //   }

  // }
  //console.log(tshirts)

  const res = await fetch('http://127.0.0.1:8000/getproducts/')
  const json_res = await res.json()
  // console.log(tshirts)
  let products = JSON.parse(JSON.stringify(json_res))
  let tshirts = products.tshirts
  // for (let item in tshirts){
  //   console.log("new tshirt")
  //   console.log(tshirts[item].size)
  // }
  return {
    props: { products: JSON.parse(JSON.stringify(tshirts)) } // will be passed to the page component as props
  }
}

export default Tshirts