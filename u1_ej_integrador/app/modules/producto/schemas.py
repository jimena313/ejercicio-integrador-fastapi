from pydantic import BaseModel, Field


class ProductoBase(BaseModel):
    nombre: str = Field(..., min_length=3)
    codigo: str
    precio: float = Field(..., gt=0)
    stock_minimo: int = Field(..., ge=0)
    activo: bool = True


class ProductoCreate(ProductoBase):
    pass


class ProductoRead(ProductoBase):
    id: int