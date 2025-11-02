from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
import json
from app.database.connection import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse
from app.schemas.token import Token
from app.schemas.response import ResponseModel
from app.core.security import verify_password, get_password_hash, create_access_token
from app.core.config import settings
from app.core.security import get_current_active_user

router = APIRouter(prefix="/auth", tags=["Autenticação"])

@router.post("/register", response_model=ResponseModel[UsuarioResponse])
def register(usuario_data: UsuarioCreate, db: Session = Depends(get_db)):
    """Registra um novo usuário."""
    # 1. Verificar se email já existe
    existing_user = db.query(Usuario).filter(Usuario.email == usuario_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )
        
    # 2. Hash da senha
    hashed_password = get_password_hash(usuario_data.senha)
    
    # 3. Converter a lista de preferências em JSON string
    preferencias_json = json.dumps(usuario_data.preferencias_categorias) if usuario_data.preferencias_categorias else None
    
    novo_usuario = Usuario(
        nome=usuario_data.nome,
        email=usuario_data.email,
        senha_hash=hashed_password,
        telefone=usuario_data.telefone
    )
    
    # Definir preferencias_categorias manualmente
    novo_usuario._preferencias_categorias = preferencias_json
    
    # 4. Salvar no banco
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    
    # 5. Converter para dict e ajustar preferencias_categorias
    usuario_dict = {
        "id": novo_usuario.id,
        "nome": novo_usuario.nome,
        "email": novo_usuario.email,
        "telefone": novo_usuario.telefone,
        "foto_perfil": novo_usuario.foto_perfil,
        "preferencias_categorias": json.loads(novo_usuario._preferencias_categorias) if novo_usuario._preferencias_categorias else [],
        "pontos_totais": novo_usuario.pontos_totais,
        "nivel": novo_usuario.nivel,
        "criado_em": novo_usuario.criado_em
    }
    
    return ResponseModel(
        success=True,
        message="Usuário cadastrado com sucesso",
        data=usuario_dict
    )

@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """Faz login e retorna token JWT."""
    user = db.query(Usuario).filter(Usuario.email == form_data.username).first()
    
    if not user or not verify_password(form_data.password, user.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    if not user.ativo:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuário inativo"
        )
        
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    
    access_token = create_access_token(
        data={"sub": user.email, "user_id": user.id},
        expires_delta=access_token_expires
    )
    
    return Token(access_token=access_token, token_type="bearer")

@router.get("/me", response_model=UsuarioResponse)
def get_current_user_info(
    current_user: Usuario = Depends(get_current_active_user) 
):
    """Retorna informações do usuário logado (requer token JWT)."""
    return current_user
