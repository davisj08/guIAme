async function getData() {
const res = await fetch('https://jsonplaceholder.typicode.com/posts')
if (!res.ok) {
throw new Error('Failed to fetch data')
}
return res.json()
}
export default async function TesteAPI() {
const posts = await getData()
return (
<div className="p-8">
<h1 className="text-3xl font-bold mb-4">Teste de API</h1>
<div className="grid gap-4">
{posts.slice(0, 5).map((post) => (
<div key={post.id} className="border p-4 rounded">
<h2 className="font-bold">{post.title}</h2>
<p className="text-gray-600">{post.body}</p>
</div>
))}
</div>
</div>
)
}