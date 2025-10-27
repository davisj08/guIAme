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
# Verificar status
git status
# Adicionar arquivos
git add .
# Commit
git commit -m "Descrição da mudança"
# Ver histórico
git log --oneline



URLs Importantes
Frontend: http://localhost:3000
Backend API: http://localhost:8000
Swagger Docs: http://localhost:8000/docs
PostgreSQL: localhost:5432
Redis: localhost:6379
