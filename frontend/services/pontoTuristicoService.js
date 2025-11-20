import api from '@/lib/axios'
    export const pontoTuristicoService = {
        async getAll(params) {
        const response = await api.get('/pontos-turisticos', { params })
    return response.data
 },
    async getById(id) {
    const response = await api.get(`/pontos-turisticos/${id}`)
     return response.data.data
 },
    async getCategorias() {
    const response = await api.get('/pontos-turisticos/categorias')
    return response.data.data
 },
}