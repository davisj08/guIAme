'use client'

import { useEffect, useState } from 'react'
import { useSearchParams } from 'next/navigation'
import useSWR from 'swr'
import MainLayout from '@/components/layout/MainLayout'
import PontoTuristicoCard from '@/components/pontoturistico/PontoTuristicoCard'
import Filtros from '@/components/ponto-turistico/Filtros'
import { pontoTuristicoService } from '@/services/pontoTuristicoService'

const fetcher = (params) => pontoTuristicoService.getAll(params)

export default function PontosTuristicosPage() {
  const searchParams = useSearchParams()
  const [params, setParams] = useState({})

  useEffect(() => {
    const newParams = {
      page: searchParams.get('page') || 1,
      busca: searchParams.get('busca') || '',
      categoria: searchParams.get('categoria') || '',
    }
    setParams(newParams)
  }, [searchParams])

  const { data, error } = useSWR(params, fetcher)
  const { data: categoriasData } = useSWR('categorias', pontoTuristicoService.getCategorias)

  if (error) return <div>Falha ao carregar</div>
  if (!data || !categoriasData) return <div>Carregando...</div>

  return (
    <MainLayout>
      <div className="container mx-auto px-4 py-12">
        <h1 className="text-4xl font-display font-bold mb-8">Pontos Turísticos</h1>
        <Filtros categorias={categoriasData} />
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {data.items.map(ponto => (
            <PontoTuristicoCard key={ponto.id} ponto={ponto} />
          ))}
        </div>
        {/* TODO: Adicionar paginação */}
      </div>
    </MainLayout>
  )
}
