'use client'

import useSWR from 'swr'
import MainLayout from '@/components/layout/MainLayout'
import ProtectedRoute from '@/components/auth/ProtectedRoute'
import { favoritoService } from '@/services/favoritoService'
import PontoTuristicoCard from '@/components/pontoturistico/PontoTuristicoCard'

export default function FavoritosPage() {
  const { data: favoritos, error } = useSWR(
    'meusFavoritos',
    favoritoService.getMeusFavoritos
  )

  if (error) return <div>Falha ao carregar</div>
  if (!favoritos) return <div>Carregando...</div>

  return (
    <ProtectedRoute>
      <MainLayout>
        <div className="container mx-auto px-4 py-12">
          <h1 className="text-4xl font-display font-bold mb-8">
            Meus Favoritos
          </h1>

          {favoritos.length > 0 ? (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
              {favoritos.map((fav) => (
                <PontoTuristicoCard
                  key={fav.ponto_turistico_id}
                  ponto={fav.ponto_turistico}
                />
              ))}
            </div>
          ) : (
            <p>Você ainda não tem pontos turísticos favoritos.</p>
          )}
        </div>
      </MainLayout>
    </ProtectedRoute>
  )
}
