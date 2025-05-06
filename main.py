from fastapi import FastAPI
from routers import orquestacion, servicios, seguridad
from fastapi.responses import RedirectResponse

app = FastAPI(
    debug=True,
    title="API de Orquestación Logística",
    version="1.0.0"
)

@app.get("/")
def home():
    return RedirectResponse(url="/docs")

app.include_router(servicios.router)
app.include_router(orquestacion.router)
app.include_router(seguridad.router)
 