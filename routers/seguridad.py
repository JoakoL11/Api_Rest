from fastapi import APIRouter
from models import UsuarioLogin, AutorizacionAcceso

router = APIRouter()

@router.post("/autenticar-usuario")
def autenticar(datos: UsuarioLogin):
    return {"token": "token_valido", "rol": "Administrador"}

@router.post("/autorizar-acceso")
def autorizar(datos: AutorizacionAcceso):
    return {"autorizado": datos.rol_usuario in ["Administrador", "Orquestador"]}
