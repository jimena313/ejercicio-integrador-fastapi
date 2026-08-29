from typing import List, Optional

from .schemas import CategoriaCreate, CategoriaRead


db_categorias: List[CategoriaRead] = [
    CategoriaRead(
        id=1,
        codigo="MUE-01",
        descripcion="Muebles de Oficina",
        activo=True,
    ),
    CategoriaRead(
        id=2,
        codigo="ELE-02",
        descripcion="Electronica",
        activo=True,
    ),
]

id_counter = 3


def crear(data: CategoriaCreate) -> CategoriaRead:
    global id_counter

    nueva = CategoriaRead(
        id=id_counter,
        **data.model_dump(),
    )

    db_categorias.append(nueva)
    id_counter += 1

    return nueva


def obtener_todas(skip: int = 0, limit: int = 10) -> List[CategoriaRead]:
    return db_categorias[skip : skip + limit]


def obtener_por_id(id: int) -> Optional[CategoriaRead]:
    for categoria in db_categorias:
        if categoria.id == id:
            return categoria

    return None