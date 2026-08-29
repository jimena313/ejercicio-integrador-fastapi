from fastapi import FastAPI

app = FastAPI()


@app.get("/doble")
def calcular_doble(numero: int):
    return {"numero": numero, "doble": numero * 2}