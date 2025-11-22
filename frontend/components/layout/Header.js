'use client'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import useAuthStore from '@/store/authStore'
import Button from '@/components/ui/Button'
import { UserCircleIcon, ArrowLeftOnRectangleIcon } from '@heroicons/react/24/outline'

export default function Header() {
  const router = useRouter()
  const { isAuthenticated, user, logout } = useAuthStore()

  const handleLogout = () => {
    logout()
    localStorage.removeItem('token')
    localStorage.removeItem('user')
    router.push('/login')
  }

  return (
    <header className="bg-white shadow-sm sticky top-0 z-50">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          
          {/* Logo */}
          <div className="flex items-center">
            <Link href="/" className="text-2xl font-bold text-primary hover:text-blue-700 transition-colors">
              guIA.ME
            </Link>
          </div>

          {/* Links de Navegação */}
          <nav className="hidden md:flex md:space-x-8">
            <Link href="/pontos-turisticos" className="text-gray-800 hover:text-primary transition-colors font-medium">
              Pontos Turísticos
            </Link>
            <Link href="/chat-ia" className="text-gray-800 hover:text-primary transition-colors font-medium">
              Chat com IA
            </Link>
          </nav>

          {/* Área de Autenticação/Usuário */}
          <div className="flex items-center space-x-4">
            {isAuthenticated ? (
              <>
                <div className="flex items-center space-x-2 text-gray-800">
                  <UserCircleIcon className="h-6 w-6 text-primary" />
                  <span className="hidden sm:inline font-medium">{user?.nome}</span>
                </div>
                <Button 
                  onClick={handleLogout} 
                  variant="ghost" 
                  size="sm" 
                  className="group text-gray-600 hover:text-red-600"
                >
                  <ArrowLeftOnRectangleIcon className="h-5 w-5 mr-1" />
                  Sair
                </Button>
              </>
            ) : (
              <>
                <Button 
                  onClick={() => router.push('/login')}
                  variant="outline" 
                  size="sm"
                  className="border-primary text-primary hover:bg-primary hover:text-white"
                >
                  Entrar
                </Button>
                <Button 
                  onClick={() => router.push('/cadastro')} 
                  size="sm"
                  className="bg-primary text-white hover:bg-blue-700"
                >
                  Cadastre-se
                </Button>
              </>
            )}
          </div>
        </div>
      </div>
    </header>
  )
}
