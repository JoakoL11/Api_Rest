from fastapi import APIRouter, Depends
from models import ReglasOrquestacion, PeticionOrquestar
from auth import validar_token

router = APIRouter()

@router.post("/orquestar")
def orquestar(peticion: PeticionOrquestar, token = Depends(validar_token)):
    return {"mensaje": f"Servicio {peticion.servicio_destino} orquestado"}

@router.put("/actualizar-reglas-orquestacion")
def actualizar_reglas(reglas: ReglasOrquestacion, token = Depends(validar_token)):
    return {"mensaje": "Reglas actualizadas"}
