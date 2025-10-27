async function getPontos() {
const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'
const res = await fetch(`${apiUrl}/api/pontos-turisticos`, {
cache: 'no-store'
})
if (!res.ok) {
throw new Error('Failed to fetch')
}
return res.json()
}
export default async function PontosTuristicos() {
const pontos = await getPontos()
return (
<div className="p-8">
<h1 className="text-3xl font-bold mb-4">Pontos Turísticos</h1>
<div className="grid gap-4">
{pontos.map((ponto) => (
<div key={ponto.id} className="border p-4 rounded">
<h2 className="font-bold text-xl">{ponto.nome}</h2>
<p className="text-gray-600">{ponto.categoria}</p>
</div>
))}
</div>
</div>
)
}
