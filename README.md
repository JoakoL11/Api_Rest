# 🚛 API REST - Orquestación de Servicios Logísticos

Esta es una API REST desarrollada con **FastAPI** para el caso de estudio de **automatización y orquestación de servicios en una empresa de logística**, como parte de un trabajo académico.

## 📦 Características

- Gestión de servicios REST internos y externos
- Orquestación de servicios con parámetros personalizados
- Autenticación con token de acceso (tipo Bearer)
- Control de acceso según roles (`Administrador`, `Orquestador`, etc.)
- Documentación interactiva con Swagger

## 🚀 Tecnologías utilizadas

- Python 3.11+
- FastAPI
- Uvicorn (para servir la app)
- Pydantic
- Railway (para despliegue en la nube)

## 🧑‍💻 Endpoints principales

| Método | Ruta                             | Descripción |
|--------|----------------------------------|-------------|
| POST   | `/autenticar-usuario`           | Autenticación de usuario |
| POST   | `/autorizar-acceso`             | Validación de acceso según rol |
| POST   | `/orquestar`                    | Ejecuta la orquestación de servicios |
| GET    | `/informacion-servicio/{id}`    | Obtiene detalles de un servicio |
| POST   | `/registrar-servicio`           | Registra un nuevo servicio |
| PUT    | `/actualizar-reglas-orquestacion` | Actualiza las reglas de orquestación |
| GET    | `/`                             | Página de bienvenida |

## 🛠 Cómo ejecutar localmente

1. Clona este repositorio:

```bash
git clone https://github.com/JoakoL11/Api_Rest.git
cd ApiRest
```
2.Crea y activa un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```
3.Instala las dependencias:
```bash
pip install -r requirements.txt
```
4.Ejecuta el servidor:
```bash
uvicorn main:app --reload

https://railway.com/project/69d2bf7c-0771-4cb6-b2f8-f3955f56bbbc/service/e263de6b-e081-4162-b7ca-d71dbf776640?environmentId=6ee4c60c-5c63-4866-826b-32f8706f66b4&id=6b513bbe-051f-4a68-85e3-83ce2173e024#details
