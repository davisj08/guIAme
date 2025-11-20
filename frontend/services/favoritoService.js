import api from '@/lib/axios'

export const favoritoService = {
  async getMeusFavoritos() {
    const response = await api.get('/favoritos/meus')
    return response.data.data
  },

  async adicionar(pontoId) {
    const response = await api.post('/favoritos', {
      ponto_turistico_id: pontoId,
    })
    return response.data.data
  },

  async remover(pontoId) {
    await api.delete(`/favoritos/${pontoId}`)
  },

  async check(pontoId) {
    const response = await api.get(`/favoritos/check/${pontoId}`)
    return response.data.data
  },
}
