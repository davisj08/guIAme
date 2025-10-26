from pydantic_settings import BaseSettings
class Settings(BaseSettings):
# Database
database_url: str =
"postgresql://guiame_user:guiame_pass@localhost:5432/guiame_db"
# Redis
redis_url: str = "redis://localhost:6379"
# OpenAI
openai_api_key: str = ""
# JWT
jwt_secret_key: str = "sua-chave-secreta-aqui-mude-em-producao"
jwt_algorithm: str = "HS256"
access_token_expire_minutes: int = 30
# Environment
environment: str = "development"
class Config:
env_file = ".env"
settings = Settings()