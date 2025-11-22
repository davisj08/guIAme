'use client'

export default function GeometricPattern({ className = '', opacity = 0 }) {
  return (
    <div className={`absolute inset-0 overflow-hidden pointer-events-none ${className}`} style={{ opacity }}>
      {/* IMAGEM DE FUNDO */}
      {/* Substitua o 'src' abaixo pelo caminho da sua imagem local ou URL */}
      <img 
        src="https://images.unsplash.com/photo-1690831191065-eaf01e98d9a5?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" 
        alt="Padrao de Azulejos de Brasilia"
        className="w-full h-full object-cover object-center"
      />
      
      {/* Camada opcional para suavizar o contraste da imagem, se necessario */}
      <div className="absolute inset-0 bg-white/10 mix-blend-overlay"></div>
    </div>
  )
}