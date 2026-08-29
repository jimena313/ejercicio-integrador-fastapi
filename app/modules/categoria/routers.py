from typing import List

from fastapi import APIRouter, HTTPException, Path, Query, status

from . import schemas, services


router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"],
)


@router.post(
    "/",
    response_model=schemas.CategoriaRead,
    status_code=status.HTTP_201_CREATED,
)
def crear_categoria(categoria: schemas.CategoriaCreate):
    return services.crear(categoria)


@router.get(
    "/",
    response_model=List[schemas.CategoriaRead],
)
def listar_categorias(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=50),
):
    return services.obtener_todas(skip, limit)


@router.get(
    "/{id}",
    response_model=schemas.CategoriaRead,
)
def obtener_categoria(id: int = Path(..., gt=0)):
    categoria = services.obtener_por_id(id)

    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail="Categoria no encontrada",
        )

    return categoria