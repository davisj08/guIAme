import { StarIcon } from '@heroicons/react/20/solid'
import { format } from 'date-fns'
import ptBR from 'date-fns/locale/pt-BR'

export default function Avaliacao({ avaliacao }) {
  return (
    <div className="py-4 border-b">
      <div className="flex items-center mb-2">
        <div className="flex items-center">
          {[...Array(5)].map((_, i) => (
            <StarIcon
              key={i}
              className={`w-5 h-5 ${i < avaliacao.nota ? 'text-yellow-400' : 'text-gray-300'}`}
            />
          ))}
        </div>
        <p className="ml-4 font-bold">{avaliacao.usuario_nome}</p>
      </div>

      <p className="text-gray-700 mb-2">{avaliacao.comentario}</p>

      <p className="text-xs text-gray-500">
        {format(new Date(avaliacao.created_at), "dd 'de' MMMM 'de' yyyy", {
          locale: ptBR,
        })}
      </p>
    </div>
  )
}