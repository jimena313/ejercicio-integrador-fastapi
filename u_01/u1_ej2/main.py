from fastapi import FastAPI

app = FastAPI()


@app.get("/perfil/actual")
def perfil_actual():
    return {"usuario": "actual"}


@app.get("/perfil/{nombre}")
def perfil_por_nombre(nombre: str):
    return {"nombre": nombre}


@app.get("/numero/{numero}")
def numero_por_id(numero: int):
    return {"numero": numero}