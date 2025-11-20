/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Cores inspiradas em Brasília
        primary: {
          50: '#e6f2ff',
          100: '#b3d9ff',
          200: '#80c0ff',
          300: '#4da6ff',
          400: '#1a8cff',
          500: '#0073e6', // Azul Cerrado
          600: '#005bb3',
          700: '#004380',
          800: '#002b4d',
          900: '#00131a',
        },
        secondary: {
          50: '#fff9e6',
          100: '#ffecb3',
          200: '#ffe080',
          300: '#ffd34d',
          400: '#ffc61a',
          500: '#e6b800', // Dourado Planalto
          600: '#b38f00',
          700: '#806600',
          800: '#4d3d00',
          900: '#1a1400',
        },
        accent: {
          50: '#f0fdf4',
          100: '#dcfce7',
          200: '#bbf7d0',
          300: '#86efac',
          400: '#4ade80',
          500: '#22c55e', // Verde Cerrado
          600: '#16a34a',
          700: '#15803d',
          800: '#166534',
          900: '#14532d',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        display: ['Poppins', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        'soft': '0 2px 15px -3px rgba(0, 0, 0, 0.07), 0 10px 20px -2px rgba(0, 0, 0, 0.04)',
        'medium': '0 4px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 30px -5px rgba(0, 0, 0, 0.04)',
      },
    },
  },
  plugins: [],
}
