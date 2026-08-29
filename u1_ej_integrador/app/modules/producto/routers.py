from typing import List

from fastapi import APIRouter, HTTPException, Path, Query, status

from . import schemas, services


router = APIRouter(
    prefix="/productos",
    tags=["Productos"],
)


@router.post(
    "/",
    response_model=schemas.ProductoRead,
    status_code=status.HTTP_201_CREATED,
)
def crear_producto(producto: schemas.ProductoCreate):
    return services.crear(producto)


@router.get(
    "/",
    response_model=List[schemas.ProductoRead],
)
def listar_productos(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=50),
):
    return services.obtener_todos(skip, limit)


@router.get(
    "/{id}",
    response_model=schemas.ProductoRead,
)
def obtener_producto(id: int = Path(..., gt=0)):
    producto = services.obtener_por_id(id)

    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado",
        )

    return producto