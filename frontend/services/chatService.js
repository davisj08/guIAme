import api from '@/lib/axios'

export const chatService = {
  async sendMessage(message) {
    const response = await api.post('/chat', { content: message })
    return response.data
  },
}
