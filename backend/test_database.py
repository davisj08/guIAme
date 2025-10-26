from app.database.connection import engine, SessionLocal, get_db
from sqlalchemy import text

# Teste 1: Verificar engine
print("🧪 Teste 1: Verificar Engine")
print(f"✅ Engine: {engine}")
print(f"   URL: {engine.url}")

# Teste 2: Testar conexão
print("\n🧪 Teste 2: Testar Conexão")
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("✅ Conexão com PostgreSQL funcionou!")
        print(f"   Resultado: {result.scalar()}")
except Exception as e:
    print(f"❌ Erro na conexão: {e}")

# Teste 3: Criar sessão
print("\n🧪 Teste 3: Criar Sessão")
db = SessionLocal()
print(f"✅ Sessão criada: {db}")
db.close()
print("✅ Sessão fechada!")

# Teste 4: Usar dependency
print("\n🧪 Teste 4: Dependency get_db")
for db_session in get_db():
    print(f"✅ Sessão via dependency: {db_session}")
    break

print("\n✅ Todos os testes de banco funcionaram!")
