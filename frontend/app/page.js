'use client'

import { useState, useEffect } from 'react'
import MainLayout from '@/components/layout/MainLayout'
import GeometricPattern from '@/components/ui/GeometricPattern'
import TouristSpotCard from '@/components/ui/TouristSpotCard'
import Link from 'next/link'
import { ArrowRight, Star, ThumbsUp } from 'lucide-react'

export default function HomePage() {
  const [featuredSpots, setFeaturedSpots] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function fetchFeaturedSpots() {
      // Simulacao de dados
      setFeaturedSpots([
          { id: 1, nome: 'Catedral Metropolitana', descricao: 'Icone da arquitetura moderna de Niemeyer com vitrais de Marianne Peretti.', categoria: 'Arquitetura', likes: 243, localizacao: 'Esplanada' },
          { id: 2, nome: 'Congresso Nacional', descricao: 'Sede do poder legislativo, famoso pelas cupulas e torres gemeas.', categoria: 'Politica', likes: 189, localizacao: 'Praca dos Tres Poderes' },
          { id: 3, nome: 'Palacio da Alvorada', descricao: 'Residencia oficial do Presidente, famosa pelas colunas flutuantes.', categoria: 'Design', likes: 156, localizacao: 'Peninsula Norte' },
          { id: 4, nome: 'Ponte JK', descricao: 'Obra de arte viaria com arcos assimetricos sobre o lago.', categoria: 'Engenharia', likes: 201, localizacao: 'Lago Sul' },
          { id: 5, nome: 'Memorial JK', descricao: 'Mausoleu dedicado ao fundador Juscelino Kubitschek.', categoria: 'Historia', likes: 178, localizacao: 'Eixo Monumental' },
          { id: 6, nome: 'Pontao do Lago Sul', descricao: 'Centro de lazer e gastronomia a beira do Lago Paranoa.', categoria: 'Lazer', likes: 134, localizacao: 'Lago Sul' },
      ])
      setLoading(false)
    }
    fetchFeaturedSpots()
  }, [])

  return (
    <MainLayout>
      {/* --- HERO SECTION --- */}
      <section className="relative bg-white min-h-[90vh] flex items-center">
        
        {/* PADRAO ATHOS: Pombas Azuis e Estrelas Pretas (Opacidade 0.15) */}
        <GeometricPattern opacity={0.35} />

        <div className="relative z-10 container mx-auto px-4 sm:px-6 lg:px-8 py-16 lg:py-0">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">
            
            {/* Texto */}
            <div className="lg:col-span-7 text-left space-y-8">
              <div className="inline-flex items-center gap-3 px-4 py-2 rounded-full bg-blue-50 border border-blue-100 text-blue-800 text-sm font-bold uppercase tracking-wider">
                Capital Modernista
              </div>
              
              <h1 className="text-5xl sm:text-7xl lg:text-8xl font-extrabold leading-[1.1] tracking-tight text-gray-900">
                Brasilia em <br/>
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-700 to-blue-500">
                  Cada Detalhe
                </span>
              </h1>

              <p className="text-xl text-gray-600 max-w-xl leading-relaxed font-medium">
                Redescubra os tracos de Niemeyer e os azulejos de Athos Bulcao em nosso guia completo.
              </p>

              <div className="flex flex-col sm:flex-row gap-5 pt-6">
                <button className="inline-flex items-center justify-center font-bold text-lg py-4 px-10 rounded-full bg-blue-700 text-white shadow-lg transition-all hover:bg-blue-800 hover:scale-[1.02]">
                  Comecar Agora
                </button>
                <button className="inline-flex items-center justify-center font-bold text-lg py-4 px-10 rounded-full border-2 border-gray-200 text-gray-700 bg-white transition-all hover:border-blue-300 hover:text-blue-700">
                  Ver Mapa
                </button>
              </div>
            </div>

            {/* Card Destaque */}
            <div className="hidden lg:block lg:col-span-5 relative pl-8 perspective-1000">
              
              {/* Fundo Solido Azulado atras do Card */}
              <div className="absolute top-8 -right-6 w-full h-[105%] rounded-[2.5rem] -z-10 transform rotate-3 bg-gradient-to-bl from-blue-100 to-indigo-50"></div>
              
              {/* O Card */}
              <div className="relative bg-white/95 backdrop-blur-sm rounded-[2rem] shadow-2xl overflow-hidden transform transition-all hover:-translate-y-2 border border-white/60">
                
                {/* Padrao interno sutil */}
                <div className="absolute inset-0 opacity-[0.03] pointer-events-none">
                  <GeometricPattern opacity={0} />
                </div>

                <div className="relative z-10 p-12">
                  <div className="mb-8">
                    <span className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold uppercase bg-amber-50 text-amber-600 mb-6 border border-amber-100">
                        <Star size={14} className="fill-current" />
                        Destaque
                    </span>
                    <h3 className="text-5xl font-black text-gray-900 leading-none tracking-tight mb-2">
                      Catedral
                    </h3>
                    <h3 className="text-5xl font-black text-blue-700 leading-none tracking-tight">
                      de Brasilia
                    </h3>
                  </div>
                  {/* ... conteudo restante do card ... */}
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </MainLayout>
  )
}