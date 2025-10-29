from app.database.connection import engine, Base
from app.models.usuario import Usuario
from app.models.ponto_turistico import PontoTuristico
from app.models.avaliacao import Avaliacao
from app.models.conquista import Conquista
from app.models.visita import Visita

def init_db():
    """
    Cria todas as tabelas no banco de dados
    """
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tabelas criadas com sucesso!")


def drop_db():
    """
    Remove todas as tabelas (use com cuidado!)"
    """
    print("ATENÇÃO: Removendo todas as tabelas...")
    Base.metadata.drop_all(bind=engine)
    print("🗑️ Tabelas removidas!")

if __name__ == "__main__":
    init_db()
