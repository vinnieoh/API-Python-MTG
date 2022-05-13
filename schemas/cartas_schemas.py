from typing import Optional
from decimal import Decimal

from pydantic import BaseModel as SCBaseModel



class CartaSchemas(SCBaseModel):
    id: Optional[int]
    nome: str
    edicao: str
    idioma: str
    foil: bool
    preco: Decimal
    cont_cartas: int
    listaCartaId: Optional[int]

    class Config:
        orm_mode = True