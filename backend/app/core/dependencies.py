from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.core.security import decode_access_token
from app.models.usuario import Usuario
from app.schemas.token import TokenData # Importado, mas não usado diretamente, o que é comum.
from typing import Optional

# ---
## 🛡️ Configuração de Segurança
# ---

# Define o esquema OAuth2 e a URL onde o token deve ser obtido.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

# ---
## 👤 Funções de Dependência
# ---

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> Usuario:
    """
    Obtém o usuário atual a partir do token JWT. 
    Lança exceção se as credenciais forem inválidas.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # 1. Decodifica o token
    payload: Optional[dict] = decode_access_token(token)
    
    if payload is None:
        raise credentials_exception
    
    # 2. Extrai dados do payload
    # Usamos o `get` com uma chave de string, pois o payload JWT é um dicionário
    email: Optional[str] = payload.get("sub")
    user_id_raw: Optional[int] = payload.get("user_id")

    # 3. Validação básica (verificando se as chaves existem)
    if email is None or user_id_raw is None:
        raise credentials_exception

    # 4. Busca o usuário no banco de dados
    # O `user_id_raw` é garantido ser um int ou None. Se passou a validação acima, é int.
    user = db.query(Usuario).filter(Usuario.id == user_id_raw).first() 

    if user is None:
        raise credentials_exception

    # 5. Verifica se o usuário está ativo
    if not user.ativo:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuário inativo"
        )
        
    return user


async def get_current_active_user(
    current_user: Usuario = Depends(get_current_user)
) -> Usuario:
    """
    Dependência para rotas que exigem um usuário autenticado e ativo.
    É redundante, pois `get_current_user` já verifica a inatividade,
    mas garante a clareza da intenção.
    """
    # Esta verificação é tecnicamente redundante se já estiver em get_current_user,
    # mas serve como uma camada de segurança ou clareza em rotas específicas.
    if not current_user.ativo: 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Usuário inativo")
        
    return current_user