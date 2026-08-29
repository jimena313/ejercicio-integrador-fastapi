from fastapi import FastAPI, HTTPException

app = FastAPI()

productos = {
    1: {"nombre": "Teclado", "precio": 25000},
    2: {"nombre": "Mouse", "precio": 15000},
    3: {"nombre": "Monitor", "precio": 180000},
}


@app.get("/productos/{producto_id}")
def buscar_producto(producto_id: int):
    if producto_id not in productos:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return productos[producto_id]