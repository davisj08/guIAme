'use client'
import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import useAuthStore from '@/store/authStore'
export default function ProtectedRoute({ children }) {
 const router = useRouter()
 const { isAuthenticated } = useAuthStore()
 useEffect(() => {
 if (!isAuthenticated) {
 router.push('/login')
 }
 }, [isAuthenticated, router])
 if (!isAuthenticated) {
 return null // ou um spinner de carregamento
 }
 return children
}