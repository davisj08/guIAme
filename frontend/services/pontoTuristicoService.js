import api from '@/lib/axios'

export const pontoTuristicoService = {
  async getAll(params) {
    const response = await api.get('/pontos-turisticos', { params })  // ← api.get já adiciona /api/
    return response.data
  },

  async getById(id) {
    const response = await api.get(`/pontos-turisticos/${id}`)
    return response.data
  },

  async getCategorias() {
    const response = await api.get('/pontos-turisticos/categorias')
    return response.data
  },
}
