export default function GeometricPattern({ className = '', opacity = 0.1 }) {
  return (
    <div className={`absolute inset-0 overflow-hidden pointer-events-none ${className}`}>
      <svg
        className="w-full h-full"
        xmlns="http://www.w3.org/2000/svg"
        style={{ opacity }}
      >
        <defs>
          {/* Padrão repetível de 100x100px */}
          <pattern
            id="athos-pattern"
            x="0"
            y="0"
            width="100"
            height="100"
            patternUnits="userSpaceOnUse"
          >
            {/* Quadrado azul */}
            <rect x="0" y="0" width="50" height="50" fill="#0055FF" />
            
            {/* Triângulo superior direito */}
            <polygon points="50,0 100,0 100,50" fill="#0055FF" />
            
            {/* Círculo inferior esquerdo */}
            <circle cx="25" cy="75" r="25" fill="#0055FF" />
            
            {/* Triângulo inferior direito */}
            <polygon points="50,50 100,50 75,100" fill="#0055FF" />
            
            {/* Semicírculo superior */}
            <path d="M 0,50 Q 25,25 50,50" fill="#0055FF" />
            
            {/* Quadrado pequeno rotacionado */}
            <rect
              x="60"
              y="60"
              width="20"
              height="20"
              fill="#0099FF"
              transform="rotate(45 70 70)"
            />
          </pattern>
        </defs>
        
        {/* Aplicar o padrão em toda a área */}
        <rect width="100%" height="100%" fill="url(#athos-pattern)" />
      </svg>
    </div>
  )
}
