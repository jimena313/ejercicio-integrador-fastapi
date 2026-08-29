from fastapi import FastAPI

app = FastAPI()


@app.get("/precio")
def calcular_precio(precio: float, descuento: float = 0):
    precio_final = precio - (precio * descuento / 100)
    return {
        "precio_original": precio,
        "descuento": descuento,
        "precio_final": precio_final
    }