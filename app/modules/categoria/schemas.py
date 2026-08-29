from pydantic import BaseModel, Field


class CategoriaBase(BaseModel):
    codigo: str = Field(..., pattern=r"^[A-Z]{3}-\d{2}$")
    descripcion: str = Field(..., min_length=3)
    activo: bool = True


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaRead(CategoriaBase):
    id: int