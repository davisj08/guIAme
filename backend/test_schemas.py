from app.schemas.ponto_turistico import (
    PontoTuristicoBase,
    PontoTuristicoCreate,
    PontoTuristicoResponse
)

# Teste 1: Criar schema base
print("🧪 Teste 1: PontoTuristicoBase")
base = PontoTuristicoBase(
    nome="Torre de TV",
    descricao="Torre de televisão de Brasília",
    categoria="Monumento",
    latitude=-15.7942,
    longitude=-47.8822
)
print(f"✅ Base criado: {base.nome}")
print(f"   Dados: {base.model_dump()}")

# Teste 2: Criar schema de criação
print("\n🧪 Teste 2: PontoTuristicoCreate")
create = PontoTuristicoCreate(
    nome="Ponte JK",
    descricao="Ponte Juscelino Kubitschek",
    categoria="Monumento",
    latitude=-15.8267,
    longitude=-47.8906
)
print(f"✅ Create criado: {create.nome}")

# Teste 3: Criar schema de resposta
print("\n🧪 Teste 3: PontoTuristicoResponse")
response = PontoTuristicoResponse(
    id=1,
    nome="Memorial JK",
    descricao="Memorial Juscelino Kubitschek",
    categoria="Museu",
    latitude=-15.8100,
    longitude=-47.9161
)
print(f"✅ Response criado: {response.nome} (ID: {response.id})")
print(f"   Dados completos: {response.model_dump()}")

print("\n✅ Todos os schemas funcionaram!")
