from app.core.openai_client import get_openai_client
from app.core.config import settings
from sqlalchemy.orm import Session
from app.models.ponto_turistico import PontoTuristico
from app.models.preferencia_usuario import PreferenciaUsuario
from typing import List, Dict
import json


class RecomendacaoService:

    @staticmethod
    def gerar_recomendacoes_ia(
        usuario_id: int,
        db: Session,
        quantidade: int = 5
    ) -> List[Dict]:
        """Gera recomendações personalizadas usando IA"""

        # 1. Buscar preferências do usuário
        preferencias = db.query(PreferenciaUsuario).filter(
            PreferenciaUsuario.usuario_id == usuario_id
        ).first()

        # 2. Buscar todos os pontos turísticos
        pontos = db.query(PontoTuristico).all()

        # 3. Preparar dados para a IA
        pontos_info = [
            {
                "id": p.id,
                "nome": p.nome,
                "categoria": p.categoria,
                "descricao": p.descricao[:200] if p.descricao else ""
            }
            for p in pontos
        ]

        # 4. Preparar prompt para a IA
        prompt = f"""Você é um especialista em turismo em Brasília.
Baseado nas seguintes informações, recomende os {quantidade} melhores pontos
turísticos para este usuário:

**Preferências do usuário:**
{RecomendacaoService._formatar_preferencias(preferencias) if preferencias else "Usuário novo, sem preferências definidas"}

**Pontos turísticos disponíveis:**
{json.dumps(pontos_info, ensure_ascii=False, indent=2)}

**Instruções:**
1. Analise as preferências do usuário
2. Selecione os {quantidade} pontos mais adequados
3. Retorne APENAS um JSON válido no formato:
[
 {{
 "ponto_id": 1,
 "motivo": "Razão da recomendação em português",
 "relevancia": 95
 }}
]
Retorne APENAS o JSON, sem texto adicional."""

        # 5. Chamar IA
        try:
            client = get_openai_client()
            response = client.chat.completions.create(
                model=settings.openai_model,
                messages=[
                    {"role": "system", "content": "Você é um assistente que retorna apenas JSON válido."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.7
            )

            resposta = response.choices[0].message.content

            # 6. Parsear JSON
            recomendacoes = json.loads(resposta)

            # 7. Enriquecer com dados do banco
            resultado = []
            for rec in recomendacoes[:quantidade]:
                ponto = db.query(PontoTuristico).filter(
                    PontoTuristico.id == rec["ponto_id"]
                ).first()

                if ponto:
                    resultado.append({
                        "ponto": {
                            "id": ponto.id,
                            "nome": ponto.nome,
                            "categoria": ponto.categoria,
                            "descricao": ponto.descricao,
                            "imagem_url": ponto.imagem_url,
                            "endereco": ponto.endereco
                        },
                        "motivo": rec["motivo"],
                        "relevancia": rec.get("relevancia", 50)
                    })

            return resultado

        except json.JSONDecodeError:
            # Fallback: recomendações básicas
            return RecomendacaoService._recomendacoes_basicas(db, quantidade)
        except Exception as e:
            raise Exception(f"Erro ao gerar recomendações: {str(e)}")

    @staticmethod
    def _formatar_preferencias(preferencias: PreferenciaUsuario) -> str:
        """Formata preferências para o prompt"""
        if not preferencias:
            return "Nenhuma preferência definida"

        texto = []

        if preferencias.categorias_favoritas:
            texto.append(f"- Categorias favoritas: {preferencias.categorias_favoritas}")

        if preferencias.tipos_atividade:
            texto.append(f"- Tipos de atividade: {preferencias.tipos_atividade}")

        texto.append(f"- Interesse em história: {preferencias.nivel_interesse_historia}/10")
        texto.append(f"- Interesse em natureza: {preferencias.nivel_interesse_natureza}/10")
        texto.append(f"- Interesse em gastronomia: {preferencias.nivel_interesse_gastronomia}/10")

        return "\n".join(texto)

    @staticmethod
    def _recomendacoes_basicas(db: Session, quantidade: int) -> List[Dict]:
        """Recomendações básicas sem IA (fallback)"""
        pontos = db.query(PontoTuristico).limit(quantidade).all()

        return [
            {
                "ponto": {
                    "id": p.id,
                    "nome": p.nome,
                    "categoria": p.categoria,
                    "descricao": p.descricao,
                    "imagem_url": p.imagem_url,
                    "endereco": p.endereco
                },
                "motivo": "Ponto turístico popular em Brasília",
                "relevancia": 50
            }
            for p in pontos
        ]