# Guia de Referência Rápida - GUIA.ME
## Comandos Docker
```bash
# Subir todos os serviços
docker-compose up
# Subir em background
docker-compose up -d
# Parar todos os serviços
docker-compose down
# Rebuild das imagens
docker-compose up --build
# Ver logs
docker-compose logs -f
# Executar comando no backend
docker-compose exec backend python -m app.database.init_db
# Acessar PostgreSQL
docker-compose exec db psql -U guiame_user -d guiame_db



Comandos Git
git pull origin main #Puxar as últimas alterações

git status  # Verificar status

git add .  # Adicionar arquivos

git commit -m "Descrição da mudança" # Commit

git log --oneline # Ver histórico

git push origin main #Enviar para o GitHub


URLs Importantes
Frontend: http://localhost:3000
Backend API: http://localhost:8000
Swagger Docs: http://localhost:8000/docs
PostgreSQL: localhost:5432
Redis: localhost:6379


🎯 Comandos Completos para Encerrar
Bash
# 1. Parar servidor (se estiver rodando)
# Ctrl + C no terminal do uvicorn

# 2. Ir para a raiz do projeto
cd /d/guIA-code

# 3. Salvar no Git
git add .
git commit -m "Dia 11 completo: Estrutura + Models + Tabelas"

# 4. Parar containers
docker-compose down

# 5. Desativar venv
deactivate

# 6. Fechar VS Code
# Alt + F4


🚀 Comandos Completos para Retomar
Bash
# 1. Abrir Docker Desktop (aguardar ficar verde)

# 2. Ir para o projeto
cd /d/guIA-code

# 3. Iniciar containers
docker-compose up -d db redis

# 4. Abrir VS Code
code .

# 5. Em novo terminal no VS Code:
cd backend
source venv/Scripts/activate
uvicorn main:app --reload

# 6. Abrir navegador
# http://localhost:8000/docs