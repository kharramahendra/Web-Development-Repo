



const blogs = ({blogs})=>{
    


    return <>
    <h1>BLOGS </h1>
{/* maping blogs  */}
    {blogs.map((blog)=>{
        return <div key={blog.sno}>
            <h2>{blog.title}</h2>
            <h2>{blog.content}</h2>
            {/* conditionals */}
            {blog.cat=='project' && <h2>{blog.cat}</h2>}
        </div>
    })}


    {blogs.map((blog)=>{
        return <div key={blog.sno}>
            <h1>{blog.title}</h1>
            <h2>{blog.content}</h2>

            {blog.author=='kaluram' && <h1>{blog.author}</h1>}
        </div>
    })}
    </>
}


export async function getServerSideProps(context){
    const res = await fetch("jdnfvnd")
    const data = await res.json()
    const blogs = data.blogs
    return {porps:{blogs}}

}


export default blogs

