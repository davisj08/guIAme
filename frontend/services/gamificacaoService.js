import api from '@/lib/axios'

export const gamificacaoService = {
  async getMinhaPontuacao() {
    const response = await api.get('/gamificacao/minha-pontuacao')
    return response.data.data
  },

  async getMinhasBadges() {
    const response = await api.get('/gamificacao/minhas-badges')
    return response.data.data
  },

  async getRanking() {
    const response = await api.get('/gamificacao/ranking')
    return response.data.data
  },
}