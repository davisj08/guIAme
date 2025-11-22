// D:\guIA-code\frontend\components\layout\MainLayout.js

import Navbar from './Navbar'  // ← MUDANÇA 1
import Footer from './Footer'

export default function MainLayout({ children }) {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />  {/* ← MUDANÇA 2 */}
      
      <main className="flex-1">
        {children}
      </main>
      
      <Footer />
    </div>
  )
}
