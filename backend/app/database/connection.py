import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Usar variável de ambiente ou localhost como padrão
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://guiame_user:guiame_pass@localhost:5432/guiame_db"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
