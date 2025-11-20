'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'
import { useForm } from 'react-hook-form'
import toast from 'react-hot-toast'
import Button from '@/components/ui/Button'
import Input from '@/components/ui/Input'
import Card from '@/components/ui/Card'
import { authService } from '@/services/authService'

const CATEGORIAS = [
  'Arquitetura',
  'Cultura',
  'Natureza',
  'Política',
  'Gastronomia',
  'Religioso',
]

export default function RegistroPage() {
  const router = useRouter()
  const [isLoading, setIsLoading] = useState(false)
  const [categoriasSelecionadas, setCategoriasSelecionadas] = useState([])
  const { register, handleSubmit, formState: { errors }, watch } = useForm()
  const senha = watch('senha')

  const toggleCategoria = (categoria) => {
    setCategoriasSelecionadas(prev =>
      prev.includes(categoria)
        ? prev.filter(c => c !== categoria)
        : [...prev, categoria]
    )
  }

  const onSubmit = async (data) => {
    setIsLoading(true)
    try {
      await authService.register({
        nome: data.nome,
        email: data.email,
        senha: data.senha,
        telefone: data.telefone || null,
        preferencias_categorias: categoriasSelecionadas,
      })
      toast.success('Cadastro realizado com sucesso!')
      router.push('/login')
    } catch (error) {
      toast.error(error.response?.data?.detail || 'Erro ao cadastrar')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 to-secondary-50 flex items-center justify-center p-4">
      <Card className="w-full max-w-2xl">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-display font-bold text-gray-900 mb-2">
            Criar Conta
          </h1>
          <p className="text-gray-600">
            Junte-se a nós e explore Brasília
          </p>
        </div>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <Input
              label="Nome Completo"
              placeholder="João Silva"
              error={errors.nome?.message}
              {...register('nome', {
                required: 'Nome é obrigatório',
                minLength: {
                  value: 3,
                  message: 'Nome deve ter no mínimo 3 caracteres'
                }
              })}
            />
            <Input
              label="Telefone (opcional)"
              type="tel"
              placeholder="(61) 99999-9999"
              {...register('telefone')}
            />
          </div>
          <Input
            label="Email"
            type="email"
            placeholder="seu@email.com"
            error={errors.email?.message}
            {...register('email', {
              required: 'Email é obrigatório',
              pattern: {
                value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
                message: 'Email inválido'
              }
            })}
          />
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <Input
              label="Senha"
              type="password"
              placeholder="••••••••"
              error={errors.senha?.message}
              {...register('senha', {
                required: 'Senha é obrigatória',
                minLength: {
                  value: 6,
                  message: 'Senha deve ter no mínimo 6 caracteres'
                }
              })}
            />
            <Input
              label="Confirmar Senha"
              type="password"
              placeholder="••••••••"
              error={errors.confirmarSenha?.message}
              {...register('confirmarSenha', {
                required: 'Confirmação de senha é obrigatória',
                validate: value => value === senha || 'As senhas não coincidem'
              })}
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Interesses (opcional)
            </label>
            <div className="flex flex-wrap gap-2">
              {CATEGORIAS.map(categoria => (
                <button
                  key={categoria}
                  type="button"
                  onClick={() => toggleCategoria(categoria)}
                  className={`px-4 py-2 rounded-full text-sm font-medium transition-all ${
                    categoriasSelecionadas.includes(categoria)
                      ? 'bg-primary-500 text-white'
                      : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                  }`}
                >
                  {categoria}
                </button>
              ))}
            </div>
          </div>
          <Button
            type="submit"
            className="w-full"
            disabled={isLoading}
          >
            {isLoading ? 'Cadastrando...' : 'Criar Conta'}
          </Button>
        </form>
        <div className="mt-6 text-center">
          <p className="text-sm text-gray-600">
            Já tem uma conta?{' '}
            <Link href="/login" className="text-primary-500 hover:text-primary-600 font-medium">
              Faça login
            </Link>
          </p>
        </div>
      </Card>
    </div>
  )
}
