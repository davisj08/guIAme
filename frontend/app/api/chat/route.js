import { NextResponse } from 'next/server'
import Groq from 'groq-sdk'

export async function POST(request ) {
  try {
    const { messages } = await request.json()
    
    const apiKey = process.env.GROQ_API_KEY || process.env.NEXT_PUBLIC_GROQ_API_KEY
    
    console.log('🔑 API Key:', apiKey ? 'Configurada' : 'NÃO CONFIGURADA')
    console.log('📨 Mensagens recebidas:', messages.length)

    if (!apiKey) {
      throw new Error('API Key não configurada')
    }

    const groq = new Groq({
      apiKey: apiKey,
    })

    const completion = await groq.chat.completions.create({
      model: 'llama-3.3-70b-versatile',
      messages: [
        {
          role: 'system',
          content: `Você é um guia turístico virtual especializado em Brasília atual 2025, Brasil. 
          Você conhece todos os pontos turísticos, restaurantes, bares, museus e atrações da cidade atual 2025.
          Na hora da sua resposta me de sem ** 
          Seja amigável, informativo e dê dicas práticas para turistas.
          Responda em português do Brasil de forma clara e objetiva.`
        },
        ...messages
      ],
      temperature: 0.7,
      max_tokens: 1024,
    })

    console.log('✅ Resposta gerada com sucesso')

    return NextResponse.json({
      message: completion.choices[0].message.content
    })
  } catch (error) {
    console.error('❌ Erro completo:', error)
    console.error('❌ Mensagem:', error.message)
    
    return NextResponse.json(
      { 
        error: 'Erro ao processar mensagem', 
        details: error.message,
        type: error.name
      },
      { status: 500 }
    )
  }
}
