'use client'
import useSWR from 'swr'
import MainLayout from '@/components/layout/MainLayout'
import ProtectedRoute from '@/components/auth/ProtectedRoute'
import useAuthStore from '@/store/authStore'
import { gamificacaoService } from '@/services/gamificacaoService'
import BadgeCard from '@/components/perfil/BadgeCard'

export default function PerfilPage() {
  const { user } = useAuthStore()

  const { data: pontuacao, error: errorPontuacao } = useSWR(
    'minhaPontuacao',
    gamificacaoService.getMinhaPontuacao
  )

  const { data: badges, error: errorBadges } = useSWR(
    'minhasBadges',
    gamificacaoService.getMinhasBadges
  )

  if (errorPontuacao || errorBadges) return <div>Falha ao carregar</div>
  if (!pontuacao || !badges) return <div>Carregando...</div>

  return (
    <ProtectedRoute>
      <MainLayout>
        <div className="container mx-auto px-4 py-12">
          <div className="text-center mb-12">
            <h1 className="text-4xl font-display font-bold">{user?.nome}</h1>
            <p className="text-lg text-gray-600">{user?.email}</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
            <div className="bg-primary-100 p-6 rounded-lg text-center">
              <p className="text-lg text-primary-800">Pontos Totais</p>
              <p className="text-5xl font-bold text-primary-600">
                {pontuacao.pontos_totais}
              </p>
            </div>

            <div className="bg-secondary-100 p-6 rounded-lg text-center">
              <p className="text-lg text-secondary-800">Nível</p>
              <p className="text-5xl font-bold text-secondary-600">
                {pontuacao.nivel}
              </p>
            </div>

            <div className="bg-accent-100 p-6 rounded-lg text-center">
              <p className="text-lg text-accent-800">Visitas</p>
              <p className="text-5xl font-bold text-accent-600">
                {pontuacao.visitas_realizadas}
              </p>
            </div>
          </div>

          <div>
            <h2 className="text-3xl font-bold mb-6">Minhas Conquistas</h2>
            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
              {badges.map((badge) => (
                <BadgeCard key={badge.id} badge={badge} />
              ))}
            </div>
          </div>
        </div>
      </MainLayout>
    </ProtectedRoute>
  )
}