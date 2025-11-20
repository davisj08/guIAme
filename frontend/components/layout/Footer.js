import Link from 'next/link'

export default function Footer() {
  const currentYear = new Date().getFullYear()

  return (
    <footer className="bg-gray-800 text-white mt-12">
      <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        
        {/* Grid Principal do Rodapé */}
        <div className="grid grid-cols-2 gap-8 md:grid-cols-4">
          
          {/* Coluna 1: Informações da Empresa */}
          <div>
            <h3 className="text-xl font-bold text-indigo-400 mb-4">
              GUIA.ME
            </h3>
            <p className="text-sm text-gray-400">
              Explore Brasília de forma inteligente com nosso guia turístico alimentado por IA.
            </p>
          </div>

          {/* Coluna 2: Links Rápidos */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Links Rápidos</h3>
            <ul className="space-y-3">
              <li>
                <Link href="/pontos-turisticos" className="text-gray-300 hover:text-indigo-400 transition-colors">
                  Pontos Turísticos
                </Link>
              </li>
              <li>
                <Link href="/chat-ia" className="text-gray-300 hover:text-indigo-400 transition-colors">
                  Chat com IA
                </Link>
              </li>
              <li>
                <Link href="/sobre" className="text-gray-300 hover:text-indigo-400 transition-colors">
                  Sobre Nós
                </Link>
              </li>
            </ul>
          </div>

          {/* Coluna 3: Categorias */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Categorias</h3>
            <ul className="space-y-3">
              <li>
                <Link href="/categorias/arquitetura" className="text-gray-300 hover:text-indigo-400 transition-colors">
                  Arquitetura
                </Link>
              </li>
              <li>
                <Link href="/categorias/cultura" className="text-gray-300 hover:text-indigo-400 transition-colors">
                  Cultura
                </Link>
              </li>
              <li>
                <Link href="/categorias/gastronomia" className="text-gray-300 hover:text-indigo-400 transition-colors">
                  Gastronomia
                </Link>
              </li>
            </ul>
          </div>

          {/* Coluna 4: Contato */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Contato</h3>
            <p className="text-gray-400">Brasília - DF, Brasil</p>
            <p className="text-gray-400 mt-1">contato@guia.me</p>
          </div>

        </div>

        {/* Separador e Copyright */}
        <div className="mt-12 pt-8 border-t border-gray-700">
          <p className="text-center text-sm text-gray-400">
            © {currentYear} GUIA.ME. Todos os direitos reservados.
          </p>
        </div>
        
      </div>
    </footer>
  )
}