import Link from 'next/link'
export default function Header() {
return (
<header className="bg-blue-600 text-white p-4">
<nav className="container mx-auto flex justify-between items-center">
<Link href="/" className="text-2xl font-bold">
GUIA.ME
</Link>
<ul className="flex space-x-4">
<li><Link href="/">Início</Link></li>
<li><Link href="/pontos-turisticos">Pontos Turísticos</Link></li>
<li><Link href="/sobre">Sobre</Link></li>
</ul>
</nav>
</header>
)
}
