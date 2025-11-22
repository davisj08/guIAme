'use client'

import { MapPin, Star, ArrowRight } from 'lucide-react'

export default function TouristSpotCard({ spot }) {
  return (
    <div className="bg-white rounded-[2rem] shadow-sm hover:shadow-xl transition-all duration-300 h-full flex flex-col border border-gray-100 group overflow-hidden">
      
      {/* Area da Imagem (Placeholder com gradiente azulado) */}
      <div className="h-56 bg-gray-100 relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-blue-50 to-indigo-50 flex flex-col items-center justify-center text-gray-400 group-hover:scale-105 transition-transform duration-700">
           <MapPin size={32} className="mb-2 opacity-30 text-blue-600" />
           <span className="text-xs font-bold uppercase tracking-widest text-blue-900/40">{spot.categoria}</span>
        </div>
        
        {/* Tag Flutuante */}
        <div className="absolute top-4 left-4">
          <span className="inline-block px-3 py-1.5 rounded-full bg-white/90 backdrop-blur-sm text-blue-700 text-xs font-bold shadow-sm border border-blue-100">
            {spot.categoria}
          </span>
        </div>
      </div>
      
      {/* Conteudo */}
      <div className="p-8 flex flex-col flex-grow">
        <div className="flex justify-between items-start mb-3">
          <h3 className="text-2xl font-bold text-gray-900 leading-tight group-hover:text-blue-700 transition-colors">
            {spot.nome}
          </h3>
          <div className="flex items-center bg-gray-50 text-gray-600 px-2 py-1 rounded-lg text-sm font-bold ml-4 shrink-0 border border-gray-200">
             <Star size={16} className="fill-current text-amber-400 mr-1" />
             4.8
          </div>
        </div>
        
        <p className="text-gray-600 text-base mb-6 flex-grow leading-relaxed line-clamp-3">
          {spot.descricao}
        </p>
        
        <div className="flex items-center justify-between pt-6 border-t border-gray-50 mt-auto">
          <div className="flex items-center text-gray-500 text-sm font-medium">
            <MapPin size={16} className="mr-2 text-gray-400" />
            <span className="truncate max-w-[140px]">{spot.localizacao}</span>
          </div>
          
          <button className="text-blue-700 text-sm font-bold flex items-center group/btn hover:underline decoration-2 underline-offset-4 transition-all">
            Ver Detalhes
            <ArrowRight size={16} className="ml-1 group-hover/btn:translate-x-1 transition-transform" />
          </button>
        </div>
      </div>
    </div>
  )
}