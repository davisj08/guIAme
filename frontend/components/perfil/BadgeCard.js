export default function BadgeCard({ badge }) {
  return (
    <div className="bg-gray-100 p-4 rounded-lg text-center">
      <div className="text-4xl mb-2">{badge.icone}</div>
      <h3 className="font-bold">{badge.nome}</h3>
      <p className="text-sm text-gray-600">{badge.descricao}</p>
    </div>
  )
}