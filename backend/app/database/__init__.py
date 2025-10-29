from app.database.connection import engine, Base
from app.models.ponto_turistico import PontoTuristico
from app.models.usuario import Usuario
from app.models.avaliacao import Avaliacao
from app.models.conquista import Conquista
from app.models.visita import Visita


def init_db():
    """Cria todas as tabelas no banco de dados"""
    Base.metadata.create_all(bind=engine)
    print("✅ Tabelas criadas com sucesso!")
    print("   - pontos_turisticos")
    print("   - usuarios")
    print("   - avaliacoes")
    print("   - conquistas")
    print("   - visitas")


def drop_db():
    """Deleta todas as tabelas do banco de dados"""
    Base.metadata.drop_all(bind=engine)
    print("🗑️ Tabelas deletadas!")


if __name__ == "__main__":
    init_db()
