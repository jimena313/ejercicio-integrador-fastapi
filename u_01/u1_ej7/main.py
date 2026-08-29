from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Usuario(BaseModel):
    nombre: str
    edad: int


@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return {
        "mensaje": "Usuario creado correctamente",
        "usuario": usuario
    }