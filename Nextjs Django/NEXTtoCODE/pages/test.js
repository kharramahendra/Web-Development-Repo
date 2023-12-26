import { useState } from "react"
import React from 'react'


const Blogs = ({ blogs }) => {

    const [username, setUsername] = useState('')
    const [userage, setUserage] = useState()


    const handleChange = async (e)=>{
        if (e.target.name=='name'){
            setUsername(e.target.value)
        }
        else if (e.target.name=='age'){
            setUserage(e.target.value)
        }
    }

    const getData = async (name, id) => {
        let data = { name: name, id: id }
        let res = await fetch('https://tensorcodes.com', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json'
            },
            body: data
        })
        let response_json = await res.json()
    }



    return <>
        <h1>BLOGS </h1>
        {/* maping blogs  */}
        {blogs.map((blog) => {
            return <div key={blog.sno}>
                <h2>{blog.title}</h2>
                <h2>{blog.content}</h2>
                {/* conditionals */}
                {blog.cat == 'project' && <h2>{blog.cat}</h2>}
            </div>
        })}



        {Object.keys(blogs).map((item) => {
            return <div key={blogs[item].sno}></div>
        })}


        <input onChange={handleChange} name="name" value={name} id="name" type="text" placeholder="ENTER YOUR NAME"/>
        <input onChange={handleChange} name="age" value={age} type="number" id="age" placeholder="ENTER YOUR NAME"/>
        <button onClick={getData}>Submit</button>
    </>
}


export async function getServerSideProps(context) {
    const res = await fetch("jdnfvnd")
    const data = await res.json()
    const blogs = data.blogs
    return { porps: { blogs } }

}



export default blogs