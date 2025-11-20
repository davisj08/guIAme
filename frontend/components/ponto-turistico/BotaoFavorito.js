'use client'

import { useState, useEffect } from 'react'
import { HeartIcon } from '@heroicons/react/24/solid'
import { favoritoService } from '@/services/favoritoService'
import toast from 'react-hot-toast'

export default function BotaoFavorito({ pontoId }) {
  const [isFavorito, setIsFavorito] = useState(false)
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    favoritoService.check(pontoId).then((data) => {
      setIsFavorito(data.is_favorito)
      setIsLoading(false)
    })
  }, [pontoId])

  const handleToggle = async () => {
    setIsLoading(true)

    try {
      if (isFavorito) {
        await favoritoService.remover(pontoId)
        toast.success('Removido dos favoritos')
      } else {
        await favoritoService.adicionar(pontoId)
        toast.success('Adicionado aos favoritos')
      }

      setIsFavorito(!isFavorito)
    } catch (error) {
      toast.error('Erro ao atualizar favoritos')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <button
      onClick={handleToggle}
      disabled={isLoading}
      className={`p-2 rounded-full transition-colors ${
        isFavorito
          ? 'text-red-500 bg-red-100'
          : 'text-gray-400 bg-gray-100 hover:bg-gray-200'
      }`}
    >
      <HeartIcon className="w-6 h-6" />
    </button>
  )
}
