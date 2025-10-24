import './globals.css'
import Header from '@/components/Header'
import Footer from '@/components/Footer'
export const metadata = {
title: 'GUIA.ME - Guia Turístico de Brasília',
description: 'Explore Brasília com inteligência artificial',
}
export default function RootLayout({ children }) {
return (
<html lang="pt-BR">
<body>
<Header />
<main className="min-h-screen">
{children}
</main>
<Footer />
</body>
</html>
)
}
