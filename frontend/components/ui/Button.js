'use client'

import Link from 'next/link'

export default function Button({
  children,
  href,
  onClick,
  variant = 'primary',
  size = 'md',
  fullWidth = false,
  disabled = false,
  className = '',
}) {
  // Variantes de estilo
  const variants = {
    primary: 'bg-primary text-white hover:bg-blue-700 shadow-md hover:shadow-primary-lg',
    secondary: 'bg-white text-primary border-2 border-primary hover:bg-primary hover:text-white shadow-md hover:shadow-lg',
    outline: 'bg-transparent text-gray-700 border-2 border-gray-300 hover:border-primary hover:text-primary',
    ghost: 'bg-transparent text-gray-700 hover:bg-gray-100',
    danger: 'bg-red-600 text-white hover:bg-red-700 shadow-md hover:shadow-lg',
  }

  // Tamanhos
  const sizes = {
    sm: 'py-2 px-4 text-sm',
    md: 'py-3 px-6 text-base',
    lg: 'py-4 px-10 text-lg',
  }

  // Classes base
  const baseClasses = `
    inline-flex items-center justify-center
    font-bold rounded-full
    transition-all duration-300
    transform hover:scale-105 active:scale-95
    disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none
    ${variants[variant]}
    ${sizes[size]}
    ${fullWidth ? 'w-full' : ''}
    ${className}
  `

  // Se for link
  if (href && !disabled) {
    return (
      <Link href={href} className={baseClasses}>
        {children}
      </Link>
    )
  }

  // Se for botão
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className={baseClasses}
    >
      {children}
    </button>
  )
}
