from fastapi import FastAPI

app = FastAPI()


@app.get("/producto/{producto_id}")
def obtener_producto(producto_id: int):
    return {
        "id": producto_id,
        "nombre": f"Producto {producto_id}"
    }