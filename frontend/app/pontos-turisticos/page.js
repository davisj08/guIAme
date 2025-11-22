'use client'

import { useEffect, useState } from 'react'
import { useSearchParams } from 'next/navigation'
import useSWR from 'swr'
import toast from 'react-hot-toast'
import MainLayout from '@/components/layout/MainLayout'
import PontoTuristicoCard from '@/components/ponto-turistico/PontoTuristicoCard'
import Filtros from '@/components/ponto-turistico/Filtros'
import { pontoTuristicoService } from '@/services/pontoTuristicoService'
import Pagination from '@/components/ui/Pagination'

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
  const { data: categoriasData, error: errorCategorias } = useSWR('categorias', pontoTuristicoService.getCategorias)
  console.log('🔍 categoriasData:', categoriasData)
const categorias = categoriasData?.data || []

  if (error || errorCategorias) {
    toast.error('Erro ao carregar dados')
    return (
      <div className="text-center py-12">
        <p className="text-red-500">Erro ao carregar. Tente novamente.</p>
      </div>
    )
  }

  if (!data) return (
    <div className="flex justify-center items-center min-h-screen">
      <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500"></div>
    </div>
  )

  return (
    <MainLayout>
      <div className="container mx-auto px-4 py-12">
        <h1 className="text-4xl font-display font-bold mb-8">Pontos Turísticos</h1>
        <Filtros categorias={categorias} />
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {data.items.map(ponto => (
            <PontoTuristicoCard key={ponto.id} ponto={ponto} />
          ))}
        </div>
        
        <Pagination totalPages={data.total_pages} />
      </div>
    </MainLayout>
  )
}
