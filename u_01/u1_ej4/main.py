from fastapi import FastAPI

app = FastAPI()


@app.get("/edad/{edad}")
def verificar_edad(edad: int):
    if edad >= 18:
        return {"resultado": "Es mayor de edad"}
    return {"resultado": "Es menor de edad"}