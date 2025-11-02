from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Assumindo que 'app.core.config' existe
from app.core.config import settings 
# Assumindo que 'app.routers.auth' existe
from app.routers import auth
# Você pode incluir outros routers aqui, como 'pontos_turisticos'
# from app.routers import pontos_turisticos

# ---
## 🚀 Inicialização da Aplicação
# ---

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API para o guia turístico de Brasília com IA"
)

# ---
## ⚙️ Configuração de Middlewares
# ---

# Configurar CORS (Compartilhamento de Recursos de Origem Cruzada)
app.add_middleware(
    CORSMiddleware,
    # As origens permitidas devem vir das suas configurações (settings)
    allow_origins=settings.cors_origins, 
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"], # Permite todos os cabeçalhos
)

# ---
## 🔗 Inclusão de Routers (Rotas)
# ---

# O roteador 'auth' (autenticação) é incluído no prefixo /api
app.include_router(auth.router, prefix="/api")

# Se você tivesse um router de pontos turísticos:
# app.include_router(pontos_turisticos.router, prefix="/api")

# ---
## 🩺 Rotas de Teste e Raiz
# ---

@app.get("/")
def read_root():
    """Retorna informações básicas sobre a API."""
    return {
        "message": f"Bem-vindo à API do {settings.app_name}",
        "version": settings.app_version,
        "status": "online",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    """Endpoint para verificação de saúde (usado por serviços de monitoramento)."""
    return {"status": "healthy"}