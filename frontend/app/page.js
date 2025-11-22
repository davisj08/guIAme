'use client'

import { useState, useEffect } from 'react'
import MainLayout from '@/components/layout/MainLayout'
import GeometricPattern from '@/components/ui/GeometricPattern'
import TouristSpotCard from '@/components/ui/TouristSpotCard'
import Button from '@/components/ui/Button'
import LoadingSpinner from '@/components/ui/LoadingSpinner'
import useScrollReveal from '@/hooks/useScrollReveal'

export default function HomePage() {
  const [featuredSpots, setFeaturedSpots] = useState([])
  const [loading, setLoading] = useState(true)

  // Scroll reveal para seção de cards
  const [cardsRef, cardsVisible] = useScrollReveal({ threshold: 0.2 })

  // Buscar pontos turísticos em destaque
  useEffect(() => {
    async function fetchFeaturedSpots() {
      try {
        const response = await fetch('http://localhost:8000/api/pontos-turisticos?limit=6')
        const data = await response.json()
        setFeaturedSpots(data.data || [])
      } catch (error) {
        console.error('Erro ao buscar pontos turísticos:', error)
        // Dados mockados para fallback
        setFeaturedSpots([
          {
            id: 1,
            nome: 'Catedral de Brasília',
            descricao: 'Obra-prima modernista projetada por Oscar Niemeyer',
            categoria: 'Arquitetura',
            likes: 243,
            localizacao: 'Eixo Monumental',
          },
          {
            id: 2,
            nome: 'Congresso Nacional',
            descricao: 'Sede do Poder Legislativo brasileiro',
            categoria: 'Política',
            likes: 189,
            localizacao: 'Praça dos Três Poderes',
          },
          {
            id: 3,
            nome: 'Palácio da Alvorada',
            descricao: 'Residência oficial do Presidente da República',
            categoria: 'Arquitetura',
            likes: 156,
            localizacao: 'SGAN',
          },
          {
            id: 4,
            nome: 'Torre de TV',
            descricao: 'Vista panorâmica de 360° de Brasília',
            categoria: 'Turismo',
            likes: 134,
            localizacao: 'Eixo Monumental',
          },
          {
            id: 5,
            nome: 'Ponte JK',
            descricao: 'Ponte estaiada sobre o Lago Paranoá',
            categoria: 'Arquitetura',
            likes: 201,
            localizacao: 'Lago Sul',
          },
          {
            id: 6,
            nome: 'Memorial JK',
            descricao: 'Homenagem ao fundador de Brasília',
            categoria: 'História',
            likes: 178,
            localizacao: 'Eixo Monumental',
          },
        ])
      } finally {
        setLoading(false)
      }
    }

    fetchFeaturedSpots()
  }, [])

  return (
    <MainLayout>
      {/* Hero Section */}
      <section className="relative bg-white min-h-[calc(100vh-4rem)] flex items-center overflow-hidden">
        {/* Padrão Geométrico de Fundo */}
        <GeometricPattern opacity={0.08} />
        
        {/* Container Principal */}
        <div className="relative z-10 container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            
            {/* Lado Esquerdo: Conteúdo */}
            <div className="text-left space-y-6 animate-fadeIn">
              {/* Título Principal */}
              <h1 className="text-6xl sm:text-7xl lg:text-8xl font-bold text-primary leading-tight">
                Brasília
              </h1>
              
              {/* Subtítulo */}
              <p className="text-lg sm:text-xl text-gray-600 max-w-xl animate-fadeIn" style={{ animationDelay: '0.2s' }}>
                Discover the citys landmarks and learn about its history with our interactive guide.
              </p>
              
              {/* Botões CTA */}
              <div className="flex flex-col sm:flex-row gap-4 pt-4 animate-fadeIn" style={{ animationDelay: '0.4s' }}>
                <Button href="/cadastro" variant="primary" size="lg">
                  Get Started
                </Button>
                <Button href="/pontos-turisticos" variant="secondary" size="lg">
                  Explore Landmarks
                </Button>
              </div>

              {/* Stats */}
              <div className="grid grid-cols-3 gap-6 pt-8 animate-fadeIn" style={{ animationDelay: '0.6s' }}>
                <div className="text-center">
                  <div className="text-3xl font-bold text-primary">50+</div>
                  <div className="text-sm text-gray-600 mt-1">Landmarks</div>
                </div>
                <div className="text-center">
                  <div className="text-3xl font-bold text-primary">1000+</div>
                  <div className="text-sm text-gray-600 mt-1">Visitors</div>
                </div>
                <div className="text-center">
                  <div className="text-3xl font-bold text-primary">4.8★</div>
                  <div className="text-sm text-gray-600 mt-1">Rating</div>
                </div>
              </div>
            </div>
            
            {/* Lado Direito: Card Flutuante */}
            <div className="relative hidden lg:block animate-fadeIn" style={{ animationDelay: '0.2s' }}>
              {/* Card de Ponto Turístico */}
              <div className="relative bg-white rounded-2xl shadow-2xl overflow-hidden transform hover:scale-105 transition-all duration-300 animate-float">
                {/* Padrão Geométrico no Card */}
                <div className="absolute inset-0 opacity-5">
                  <GeometricPattern opacity={1} />
                </div>
                
                {/* Conteúdo do Card */}
                <div className="relative z-10 p-8">
                  <h3 className="text-2xl font-bold text-gray-800 mb-2">
                    Cathedral
                  </h3>
                  <h3 className="text-2xl font-bold text-gray-800 mb-4">
                    of Brasilia
                  </h3>
                  
                  <p className="text-gray-600 mb-6">
                    A modernist masterpiece designed by Oscar Niemeyer
                  </p>
                  
                  {/* Likes */}
                  <div className="flex items-center space-x-2 text-primary">
                    <svg
                      className="w-6 h-6 fill-current"
                      viewBox="0 0 24 24"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path d="M7 22V11M2 13V20C2 21.1046 2.89543 22 4 22H17.4262C18.907 22 20.1662 20.9197 20.3914 19.4562L21.4683 12.4562C21.7479 10.6389 20.3418 9 18.5032 9H15V4C15 2.89543 14.1046 2 13 2C12.4477 2 12 2.44772 12 3V3.5C12 4.03153 11.7891 4.53782 11.4142 4.91287L7.58579 8.74129C7.21071 9.11637 7 9.62266 7 10.1542V11M7 11H4C2.89543 11 2 11.8954 2 13Z" />
                    </svg>
                    <span className="text-lg font-semibold">243</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        {/* Padrão Geométrico Extra no Canto Inferior Direito */}
        <div className="absolute bottom-0 right-0 w-1/2 h-1/2 opacity-5 pointer-events-none">
          <GeometricPattern opacity={1} />
        </div>
      </section>

      {/* Seção de Pontos Turísticos em Destaque */}
      <section ref={cardsRef} className="relative bg-gray-50 py-20">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          
          {/* Cabeçalho da Seção */}
          <div className={`text-center mb-12 transition-all duration-800 ${cardsVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`}>
            <h2 className="text-4xl sm:text-5xl font-bold text-gray-800 mb-4">
              Featured Landmarks
            </h2>
            <p className="text-lg text-gray-600 max-w-2xl mx-auto">
              Explore the most iconic tourist attractions in Brasília
            </p>
          </div>

          {/* Grid de Cards */}
          {loading ? (
            <div className="flex justify-center py-20">
              <LoadingSpinner size="xl" />
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {featuredSpots.map((spot, index) => (
                <div
                  key={spot.id}
                  className={`transition-all duration-600 ${
                    cardsVisible 
                      ? 'opacity-100 translate-y-0' 
                      : 'opacity-0 translate-y-10'
                  }`}
                  style={{ 
                    transitionDelay: cardsVisible ? `${index * 100}ms` : '0ms' 
                  }}
                >
                  <TouristSpotCard spot={spot} />
                </div>
              ))}
            </div>
          )}

          {/* Botão Ver Todos */}
          <div className={`text-center mt-12 transition-all duration-800 ${cardsVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`} style={{ transitionDelay: '600ms' }}>
            <Button href="/pontos-turisticos" variant="secondary" size="lg">
              View All Landmarks
            </Button>
          </div>
        </div>
      </section>
    </MainLayout>
  )
}
