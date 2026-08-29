from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Alumno(BaseModel):
    nombre: str
    edad: int
    carrera: str


@app.post("/alumnos")
def crear_alumno(alumno: Alumno):
    return {
        "mensaje": "Alumno creado correctamente",
        "alumno": alumno,
    }


@app.put("/alumnos/{alumno_id}")
def actualizar_alumno(alumno_id: int, alumno: Alumno):
    return {
        "id": alumno_id,
        "alumno": alumno,
    }