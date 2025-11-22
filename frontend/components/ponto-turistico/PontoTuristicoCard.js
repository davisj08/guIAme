import Link from 'next/link'

export default function PontoTuristicoCard({ ponto }) {
  return (
    <Link href={`/pontos-turisticos/${ponto.id}`}>
      <a className="block bg-white rounded-lg shadow-md overflow-hidden group transition-all duration-300 transform hover:-translate-y-1 hover:shadow-xl">
        <div className="relative h-48 w-full">
          {/* Imagem com fallback */}
          <img
            src={ponto.imagem_url || 'https://via.placeholder.com/400x300?text=guIA-code'}
            alt={ponto.nome}
            className="w-full h-full object-cover transition-transform duration-300 group-hover:scale-110"
            onError={(e ) => {
              e.target.onerror = null // Previne loop infinito
              e.target.src = 'https://via.placeholder.com/400x300?text=guIA-code'
            }}
          />
          <div className="absolute inset-0 bg-black bg-opacity-20 group-hover:bg-opacity-10 transition-all duration-300"></div>
        </div>
        <div className="p-4">
          <span className="inline-block bg-primary-light bg-opacity-20 text-primary text-xs font-semibold px-2 py-1 rounded-full mb-2">
            {ponto.categoria}
          </span>
          <h3 className="text-lg font-bold text-gray-800 truncate">{ponto.nome}</h3>
          <p className="text-sm text-gray-500 mt-1 line-clamp-2">
            {ponto.descricao || 'Descrição não disponível.'}
          </p>
        </div>
      </a>
    </Link>
   )
}