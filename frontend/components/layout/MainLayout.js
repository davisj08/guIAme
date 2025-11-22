'use client'

import { Menu } from 'lucide-react'
import Link from 'next/link'

export default function MainLayout({ children }) {
  return (
    <div className="min-h-screen flex flex-col font-sans text-gray-900 bg-[#FAFAFA]">
      {/* Header Glassmorphism */}
      <header className="sticky top-0 z-50 w-full bg-white/80 backdrop-blur-xl border-b border-gray-100">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
          
          {/* Logo */}
          <div className="flex items-center gap-3 group cursor-pointer">
             <div className="w-10 h-10 bg-blue-700 rounded-xl flex items-center justify-center text-white shadow-lg shadow-blue-700/20 transition-transform group-hover:scale-105">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                    <path d="M12 2L2 7L12 12L22 7L12 2Z" />
                    <path d="M2 17L12 22L22 17" />
                    <path d="M2 12L12 17L22 12" />
                </svg>
             </div>
             <span className="font-bold text-2xl tracking-tight text-gray-900">
               Guia<span className="text-blue-700">Brasilia</span>
             </span>
          </div>
          
          {/* Navegacao Desktop */}
          <nav className="hidden md:flex items-center gap-8 text-sm font-semibold text-gray-600">
            <Link href="/" className="hover:text-blue-700 transition-colors">Home</Link>
            <Link href="/pontos" className="hover:text-blue-700 transition-colors">Pontos Turisticos</Link>
            <Link href="/historia" className="hover:text-blue-700 transition-colors">Historia</Link>
          </nav>
          
          {/* Botoes */}
          <div className="flex items-center gap-4">
            <button className="hidden sm:block text-sm font-bold text-gray-600 hover:text-blue-700 transition-colors">
              Entrar
            </button>
            <button className="bg-blue-700 text-white text-sm font-bold px-6 py-2.5 rounded-full hover:bg-blue-800 transition-all shadow-md hover:shadow-lg active:scale-95">
              Cadastrar
            </button>
            <button className="md:hidden text-gray-600 p-2">
              <Menu size={24} />
            </button>
          </div>
        </div>
      </header>
      
      <main className="flex-grow relative overflow-hidden">
        {children}
      </main>
      
      <footer className="bg-white border-t border-gray-100 py-12 mt-auto">
        <div className="container mx-auto px-4 text-center">
          <p className="text-gray-500 font-medium mb-3">2024 GuiaBrasilia.</p>
          <p className="text-gray-400 text-sm">
            Design inspirado na obra de <span className="text-blue-700 font-semibold">Athos Bulcao</span>.
          </p>
        </div>
      </footer>
    </div>
  )
}