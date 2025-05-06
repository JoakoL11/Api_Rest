from fastapi import Header, HTTPException

def validar_token(token: str = Header(...)):
    if token != "token_valido":
        raise HTTPException(status_code=401, detail="Token inválido")
    return {"rol": "Administrador"}  # o "Orquestador", etc.
