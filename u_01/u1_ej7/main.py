from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int


@app.post("/productos")
def crear_producto(producto: Producto):
    return {
        "mensaje": "Producto creado correctamente",
        "producto": producto,
    }


@app.get("/buscar")
def buscar_producto(
    nombre: str = Query(..., min_length=2),
    precio_maximo: float | None = None,
):
    return {
        "nombre": nombre,
        "precio_maximo": precio_maximo,
    }