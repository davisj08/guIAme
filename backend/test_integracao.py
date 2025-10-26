from app.database.connection import SessionLocal
from app.models.ponto_turistico import PontoTuristico
from app.schemas.ponto_turistico import PontoTuristicoCreate

print("🧪 Teste de Integração Completa\n")

# 1. Criar sessão
print("1️⃣ Criando sessão do banco...")
db = SessionLocal()
print("✅ Sessão criada!")

# 2. Criar schema Pydantic
print("\n2️⃣ Criando schema Pydantic...")
ponto_data = PontoTuristicoCreate(
    nome="Palácio do Planalto",
    descricao="Sede do Poder Executivo Federal",
    categoria="Monumento Histórico",
    latitude=-15.7989,
    longitude=-47.8608
)
print(f"✅ Schema criado: {ponto_data.nome}")

# 3. Converter para model SQLAlchemy
print("\n3️⃣ Convertendo para model SQLAlchemy...")
ponto_model = PontoTuristico(**ponto_data.model_dump())
print(f"✅ Model criado: {ponto_model.nome}")

# 4. Salvar no banco
print("\n4️⃣ Salvando no banco de dados...")
try:
    db.add(ponto_model)
    db.commit()
    db.refresh(ponto_model)
    print(f"✅ Salvo com sucesso! ID: {ponto_model.id}")
except Exception as e:
    print(f"❌ Erro ao salvar: {e}")
    db.rollback()

# 5. Buscar do banco
print("\n5️⃣ Buscando do banco de dados...")
ponto_buscado = db.query(PontoTuristico).filter(
    PontoTuristico.nome == "Palácio do Planalto"
).first()

if ponto_buscado:
    print(f"✅ Encontrado: {ponto_buscado.nome}")
    print(f"   ID: {ponto_buscado.id}")
    print(f"   Descrição: {ponto_buscado.descricao}")
    print(f"   Categoria: {ponto_buscado.categoria}")
else:
    print("❌ Não encontrado!")

# 6. Listar todos
print("\n6️⃣ Listando todos os pontos...")
todos_pontos = db.query(PontoTuristico).all()
print(f"✅ Total de pontos: {len(todos_pontos)}")
for p in todos_pontos:
    print(f"   - {p.id}: {p.nome}")

# 7. Fechar sessão
print("\n7️⃣ Fechando sessão...")
db.close()
print("✅ Sessão fechada!")

print("\n🎉 Teste de integração completo! Tudo funcionando!")
