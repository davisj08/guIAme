'use client'

import Link from 'next/link'
import { useState } from 'react'
import GeometricPattern from '@/components/ui/GeometricPattern'

export default function TouristSpotCard({ spot }) {
  const [imageError, setImageError] = useState(false)

  // Fallback para imagem
  const imageSrc = imageError || !spot.imagem_url
    ? 'https://via.placeholder.com/400x300/0055FF/FFFFFF?text=Brasília'
    : spot.imagem_url

  return (
    <Link href={`/pontos-turisticos/${spot.id}`}>
      <div className="group relative bg-white rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden cursor-pointer transform hover:-translate-y-2">
        
        {/* Padrão Geométrico Sutil */}
        <div className="absolute inset-0 opacity-0 group-hover:opacity-5 transition-opacity duration-300 pointer-events-none">
          <GeometricPattern opacity={1} />
        </div>

        {/* Imagem */}
        <div className="relative h-48 overflow-hidden bg-gray-100">
          <img
            src={imageSrc}
            alt={spot.nome}
            onError={() => setImageError(true)}
            className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
          />
          
          {/* Overlay Gradiente */}
          <div className="absolute inset-0 bg-gradient-to-t from-black/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
        </div>

        {/* Conteúdo */}
        <div className="relative p-6 space-y-3">
          
          {/* Categoria Badge */}
          {spot.categoria && (
            <span className="inline-block px-3 py-1 text-xs font-semibold text-primary bg-blue-50 rounded-full">
              {spot.categoria}
            </span>
          )}

          {/* Título */}
          <h3 className="text-xl font-bold text-gray-800 group-hover:text-primary transition-colors duration-300 line-clamp-2">
            {spot.nome}
          </h3>

          {/* Descrição */}
          <p className="text-gray-600 text-sm line-clamp-3">
            {spot.descricao || 'Descubra mais sobre este ponto turístico icônico de Brasília.'}
          </p>

          {/* Footer: Likes e Localização */}
          <div className="flex items-center justify-between pt-3 border-t border-gray-100">
            
            {/* Likes */}
            <div className="flex items-center space-x-2 text-primary">
              <svg
                className="w-5 h-5 fill-current"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path d="M7 22V11M2 13V20C2 21.1046 2.89543 22 4 22H17.4262C18.907 22 20.1662 20.9197 20.3914 19.4562L21.4683 12.4562C21.7479 10.6389 20.3418 9 18.5032 9H15V4C15 2.89543 14.1046 2 13 2C12.4477 2 12 2.44772 12 3V3.5C12 4.03153 11.7891 4.53782 11.4142 4.91287L7.58579 8.74129C7.21071 9.11637 7 9.62266 7 10.1542V11M7 11H4C2.89543 11 2 11.8954 2 13Z" />
              </svg>
              <span className="text-sm font-semibold">{spot.likes || 0}</span>
            </div>

            {/* Localização */}
            {spot.localizacao && (
              <div className="flex items-center space-x-1 text-gray-500">
                <svg
                  className="w-4 h-4"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                  />
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                </svg>
                <span className="text-xs truncate max-w-[120px]">{spot.localizacao}</span>
              </div>
            )}
          </div>
        </div>

        {/* Indicador de Hover */}
        <div className="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
          <div className="bg-primary text-white p-2 rounded-full shadow-lg">
            <svg
              className="w-4 h-4"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M9 5l7 7-7 7"
              />
            </svg>
          </div>
        </div>
      </div>
    </Link>
  )
}
