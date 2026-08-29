from enum import Enum

from fastapi import FastAPI

app = FastAPI()


class TipoCurso(str, Enum):
    python = "python"
    java = "java"
    javascript = "javascript"


@app.get("/cursos/{tipo}")
def obtener_curso(tipo: TipoCurso):
    return {"curso": tipo}