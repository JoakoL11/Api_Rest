from fastapi import APIRouter, Depends
from models import Servicio
from auth import validar_token

router = APIRouter()

@router.post("/registrar-servicio")
def registrar(servicio: Servicio, token = Depends(validar_token)):
    return {"mensaje": "Servicio registrado exitosamente"}

@router.get("/informacion-servicio/{id}")
def info(id: int, token = Depends(validar_token)):
    return {"id": id, "nombre": "Servicio Demo"}
