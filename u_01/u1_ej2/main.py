from fastapi import FastAPI

app = FastAPI()


@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"Hola {nombre}"}