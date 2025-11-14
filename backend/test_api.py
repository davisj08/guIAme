import requests

# Configurações
BASE_URL = "http://localhost:8000"
EMAIL = "teste@example.com"
SENHA = "senha123"

# 1. Fazer login
print("1. Fazendo login..." )
response = requests.post(
    f"{BASE_URL}/api/auth/login",
    data={
        "grant_type": "password",
        "username": EMAIL,
        "password": SENHA
    }
)

if response.status_code == 200:
    token = response.json()["access_token"]
    print(f"✅ Login OK! Token obtido!")
else:
    print(f"❌ Erro no login: {response.text}")
    exit()

# 2. Configurar headers
headers = {
    "Authorization": f"Bearer {token}"
}

# 3. Testar chat
print("\n2. Testando chat...")
response = requests.post(
    f"{BASE_URL}/api/chat",
    json={"mensagem": "Olá! Me fale sobre Brasília"},
    headers=headers
)

if response.status_code == 200:
    resposta = response.json()["resposta"]
    print(f"✅ Chat OK!")
    print(f"Resposta: {resposta[:200]}...")
else:
    print(f"❌ Erro no chat: {response.text}")

# 4. Testar recomendações
print("\n3. Testando recomendações...")
response = requests.get(
    f"{BASE_URL}/api/recomendacoes?quantidade=2",
    headers=headers
)

if response.status_code == 200:
    recomendacoes = response.json()["recomendacoes"]
    print(f"✅ Recomendações OK!")
    for rec in recomendacoes:
        print(f"  - {rec['ponto']['nome']}: {rec['motivo'][:100]}...")
else:
    print(f"❌ Erro nas recomendações: {response.text}")

# 5. Testar perfil
print("\n4. Testando perfil...")
response = requests.get(
    f"{BASE_URL}/api/auth/me",
    headers=headers
)

if response.status_code == 200:
    usuario = response.json()
    print(f"✅ Perfil OK!")
    print(f"  Nome: {usuario['nome']}")
    print(f"  Email: {usuario['email']}")
    print(f"  Nível: {usuario['nivel']}")
else:
    print(f"❌ Erro no perfil: {response.text}")
