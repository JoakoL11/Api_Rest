from fastapi import FastAPI
from routers import orquestacion, servicios, seguridad


app = FastAPI(
    debug=True,
    title="API de Orquestación Logística",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API de Logística Global"}

app.include_router(servicios.router)
app.include_router(orquestacion.router)
app.include_router(seguridad.router)
 