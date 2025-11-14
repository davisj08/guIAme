from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.core.security import get_current_active_user
from app.models.usuario import Usuario
from app.schemas.recomendacao import RecomendacoesResponse, RecomendacaoItem
from app.services.recomendacao_service import RecomendacaoService

# Inicialização do router
router = APIRouter()


@router.get(
    "/recomendacoes",
    response_model=RecomendacoesResponse,
    summary="Obter Recomendações Personalizadas"
)
def obter_recomendacoes(
    quantidade: int = Query(
        5,
        ge=1,
        le=10,
        description="Quantidade de recomendações"
    ),
    current_user: Usuario = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Retorna recomendações personalizadas de pontos turísticos usando IA.

    A IA analisa as preferências do usuário e recomenda os pontos mais
    adequados.
    """
    try:
        recomendacoes = RecomendacaoService.gerar_recomendacoes_ia(
            usuario_id=current_user.id,
            db=db,
            quantidade=quantidade
        )

        items = [
            RecomendacaoItem(**rec)
            for rec in recomendacoes
        ]

        return RecomendacoesResponse(
            recomendacoes=items,
            total=len(items)
        )

    except Exception as e:
        # Registra o erro e retorna uma exceção HTTP 500
        # Em um ambiente de produção, o log do erro seria mais detalhado
        raise HTTPException(status_code=500, detail=str(e))