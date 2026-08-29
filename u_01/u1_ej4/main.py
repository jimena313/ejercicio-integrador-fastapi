from fastapi import FastAPI

app = FastAPI()

materias = [
    {"nombre": "Estadistica"},
    {"nombre": "Algebra"},
    {"nombre": "Informatica"},
    {"nombre": "Diseno de Sistemas"},
]


@app.get("/materias")
def listar_materias(inicio: int = 0, cantidad: int = 10):
    return materias[inicio:inicio + cantidad]


@app.get("/materias/{materia_id}")
def buscar_materia(materia_id: int, detalle: str | None = None):
    resultado = {"id": materia_id}

    if detalle:
        resultado["detalle"] = detalle

    return resultado


@app.get("/alumnos/{alumno_id}/materias/{materia_id}")
def materia_alumno(
    alumno_id: int,
    materia_id: int,
    observacion: str | None = None,
    completo: bool = False,
):
    resultado = {
        "alumno_id": alumno_id,
        "materia_id": materia_id,
        "completo": completo,
    }

    if observacion:
        resultado["observacion"] = observacion

    return resultado