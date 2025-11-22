import Link from 'next/link'

export default function Logo({ size = 'md' }) {
  const sizes = {
    sm: { icon: 'w-8 h-8', text: 'text-xl' },
    md: { icon: 'w-10 h-10', text: 'text-2xl' },
    lg: { icon: 'w-12 h-12', text: 'text-3xl' },
  }

  const currentSize = sizes[size]

  return (
    <Link href="/" className="flex items-center space-x-3 group">
        {/* Ícone Geométrico */}
        <div className={`${currentSize.icon} relative`}>
          <svg
            viewBox="0 0 40 40"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            className="w-full h-full transition-transform duration-300 group-hover:scale-110"
          >
            {/* Fundo branco */}
            <rect width="40" height="40" fill="white" rx="4" />
            
            {/* Quadrado azul superior esquerdo */}
            <rect x="2" y="2" width="16" height="16" fill="#0055FF" />
            
            {/* Triângulo superior direito */}
            <polygon points="20,2 38,2 38,20" fill="#0055FF" />
            
            {/* Círculo inferior esquerdo */}
            <circle cx="10" cy="30" r="8" fill="#0099FF" />
            
            {/* Triângulo inferior direito */}
            <polygon points="22,22 38,22 30,38" fill="#0099FF" />
          </svg>
        </div>

        {/* Texto do Logo */}
        <span className={`${currentSize.text} font-bold text-primary transition-colors duration-300 group-hover:text-blue-700`}>
          guIA-code
        </span>
    </Link>
  )
}
