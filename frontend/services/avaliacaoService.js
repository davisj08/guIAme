import api from '@/lib/axios'

export const avaliacaoService = {
  async getByPonto(pontoId) {
    const response = await api.get(`/avaliacoes/ponto/${pontoId}`)
    return response.data.data
  },

  async create(data) {
    const response = await api.post('/avaliacoes', data)
    return response.data.data
  },
}