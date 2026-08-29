from typing import List, Optional

from .schemas import ProductoCreate, ProductoRead


db_productos: List[ProductoRead] = [
    ProductoRead(
        id=1,
        nombre="Silla de Oficina",
        codigo="MUE-01",
        precio=150.0,
        stock_minimo=5,
        activo=True,
    ),
]

id_counter = 2


def crear(data: ProductoCreate) -> ProductoRead:
    global id_counter

    nuevo = ProductoRead(
        id=id_counter,
        **data.model_dump(),
    )

    db_productos.append(nuevo)
    id_counter += 1

    return nuevo


def obtener_todos(skip: int = 0, limit: int = 10) -> List[ProductoRead]:
    return db_productos[skip : skip + limit]


def obtener_por_id(id: int) -> Optional[ProductoRead]:
    for producto in db_productos:
        if producto.id == id:
            return producto

    return None