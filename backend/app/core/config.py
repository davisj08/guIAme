from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    # Informações da Aplicação
    app_name: str = "GUIA.ME API"
    app_version: str = "1.0.0"
    app_description: str = "API do guia turístico inteligente de Brasília"
    
    # Banco de Dados
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql://guiame_user:guiame_pass@localhost:5432/guiame_db"
    )
    
    # Redis
    redis_url: str = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379"
    )
    redis_ttl: int = 3600
    
    # OpenAI
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    openai_model: str = "gpt-4"
    
    # Segurança / JWT
    secret_key: str = os.getenv(
        "SECRET_KEY",
        "sua-chave-secreta-super-segura-aqui"
    )
    jwt_secret_key: str = os.getenv(
        "JWT_SECRET_KEY",
        "sua_chave_secreta_super_segura_aqui_mude_em_producao"
    )
    jwt_algorithm: str = "HS256"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # CORS - Lista fixa (não lê do .env)
    cors_origins: list = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
    
    # Ambiente
    environment: str = os.getenv("ENVIRONMENT", "development" )
    debug: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    class Config:
        env_file: str = ".env"
        env_file_encoding: str = "utf-8"
        case_sensitive: bool = False


settings = Settings()
