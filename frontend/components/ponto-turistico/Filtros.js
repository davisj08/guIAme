'use client'
import { useState, useEffect } from 'react'
import { useRouter, useSearchParams } from 'next/navigation'
import Input from '@/components/ui/Input'
import Button from '@/components/ui/Button'

export default function Filtros({ categorias }) {
  const router = useRouter()
  const searchParams = useSearchParams()

  const [busca, setBusca] = useState(searchParams.get('busca') || '')
  const [categoria, setCategoria] = useState(searchParams.get('categoria') || '')

  const handleFilter = () => {
    const params = new URLSearchParams()

    if (busca) params.set('busca', busca)
    if (categoria) params.set('categoria', categoria)

    router.push(`/pontos-turisticos?${params.toString()}`)
  }

  return (
    <div className="bg-white p-4 rounded-lg shadow-soft mb-8 flex flex-col md:flex-row gap-4 items-center">
      <Input
        placeholder="Buscar por nome..."
        value={busca}
        onChange={(e) => setBusca(e.target.value)}
        className="flex-grow"
      />

      <select
        value={categoria}
        onChange={(e) => setCategoria(e.target.value)}
        className="w-full md:w-auto px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
      >
        <option value="">Todas as categorias</option>
        {categorias.map(cat => (
          <option key={cat} value={cat}>{cat}</option>
        ))}
      </select>

      <Button onClick={handleFilter}>Filtrar</Button>
    </div>
  )
}