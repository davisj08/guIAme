from fastapi import FastAPI

app = FastAPI(
    title="GUIA.ME API",
    description="API do guia turístico inteligente de Brasília",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "message": "Bem-vindo à API do GUIA.ME",
        "version": "1.0.0",
        "status": "online"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "GUIA.ME API"
    }

@app.get("/pontos-turisticos")
def listar_pontos():
    return {
        "pontos": [
            {"id": 1, "nome": "Catedral Metropolitana"},
            {"id": 2, "nome": "Congresso Nacional"},
            {"id": 3, "nome": "Palácio da Alvorada"}
        ]
    }
