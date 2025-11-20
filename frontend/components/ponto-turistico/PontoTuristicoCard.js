import Link from 'next/link'
import Image from 'next/image'
import Card from '@/components/ui/Card'
import Badge from '@/components/ui/Badge'

export default function PontoTuristicoCard({ ponto }) {
  return (
    <Link href={`/pontos-turisticos/${ponto.id}`}>
      <Card hover>
        <div className="relative h-48 w-full mb-4">
          <Image
            src={ponto.imagem_url || '/placeholder.jpg'}
            alt={ponto.nome}
            layout="fill"
            objectFit="cover"
            className="rounded-lg"
          />
        </div>
        <h3 className="text-lg font-bold mb-2 truncate">{ponto.nome}</h3>
        <Badge>{ponto.categoria}</Badge>
      </Card>
    </Link>
  )
}
