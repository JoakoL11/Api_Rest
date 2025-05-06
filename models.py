from pydantic import BaseModel, EmailStr
from typing import List, Dict

class UsuarioLogin(BaseModel):
    nombre_usuario: str
    contrasena: str

class AutorizacionAcceso(BaseModel):
    recursos: List[str]
    rol_usuario: str

class Servicio(BaseModel):
    nombre: str
    descripcion: str
    endpoints: List[str]

class ReglasOrquestacion(BaseModel):
    reglas: Dict[str, str]

class PeticionOrquestar(BaseModel):
    servicio_destino: str
    parametros_adicionales: Dict[str, str]
