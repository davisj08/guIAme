'use client'
import { useState } from 'react'
import { useForm } from 'react-hook-form'
import toast from 'react-hot-toast'
import Button from '@/components/ui/Button'
import { avaliacaoService } from '@/services/avaliacaoService'
import { StarIcon } from '@heroicons/react/20/solid'

export default function FormularioAvaliacao({ pontoId, onAvaliacaoCriada }) {
  const [nota, setNota] = useState(0)
  const [hoverNota, setHoverNota] = useState(0)
  const [isLoading, setIsLoading] = useState(false)

  const { register, handleSubmit, reset } = useForm()

  const onSubmit = async (data) => {
    if (nota === 0) {
      toast.error('Por favor, selecione uma nota.')
      return
    }

    setIsLoading(true)

    try {
      const novaAvaliacao = await avaliacaoService.create({
        ponto_turistico_id: pontoId,
        nota: nota,
        comentario: data.comentario,
      })

      toast.success('Avaliação enviada com sucesso!')
      onAvaliacaoCriada(novaAvaliacao)
      reset()
      setNota(0)
    } catch (error) {
      toast.error(error.response?.data?.detail || 'Erro ao enviar avaliação')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="mt-8">
      <h3 className="text-xl font-bold mb-4">Deixe sua avaliação</h3>

      <div className="flex items-center mb-4">
        {[...Array(5)].map((_, i) => (
          <StarIcon
            key={i}
            className={`w-8 h-8 cursor-pointer ${i < (hoverNota || nota) ? 'text-yellow-400' : 'text-gray-300'}`}
            onClick={() => setNota(i + 1)}
            onMouseEnter={() => setHoverNota(i + 1)}
            onMouseLeave={() => setHoverNota(0)}
          />
        ))}
      </div>

      <textarea
        {...register('comentario', { required: true })}
        placeholder="Escreva seu comentário..."
        className="w-full p-2 border rounded-lg"
        rows={4}
      />

      <Button type="submit" disabled={isLoading} className="mt-4">
        {isLoading ? 'Enviando...' : 'Enviar Avaliação'}
      </Button>
    </form>
  )
}