import Link from 'next/link'
const pontos = [
{ id: 1, nome: 'Catedral Metropolitana' },
{ id: 2, nome: 'Congresso Nacional' },
{ id: 3, nome: 'Palácio da Alvorada' },
]
export default function PontosTuristicos() {
return (
<div className="p-8">
<h1 className="text-3xl font-bold mb-4">Pontos Turísticos</h1>
<div className="grid gap-4">
{pontos.map((ponto) => (
<Link
key={ponto.id}
href={`/pontos-turisticos/${ponto.id}`}
className="border p-4 rounded hover:bg-gray-100"
>
<h2 className="font-bold">{ponto.nome}</h2>
</Link>
))}
</div>
</div>
)
}
