from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routers import auth, pontos_turisticos, recomendacoes, gamificacao , avaliacao
from app.routers import chat






app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API para o guia turístico de Brasília com IA"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth.router, prefix="/api")
app.include_router(pontos_turisticos.router, prefix="/api")  # ← ADICIONAR esta linha

@app.get("/")
def read_root():
    return {
        "message": f"Bem-vindo à API do {settings.app_name}",
        "version": settings.app_version,
        "status": "online",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(
 chat.router,
 prefix="/api",
 tags=["Chat com IA"]
)

app.include_router(
 recomendacoes.router,
 prefix="/api",
 tags=["Recomendações com IA"]
)

app.include_router(gamificacao.router)
app.include_router(avaliacao.router)



