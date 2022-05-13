from typing import Optional

from pydantic import BaseModel as SCBaseModel


class ListaCartasSchemas(SCBaseModel):
    id: Optional[int]
    nome: str

    class Config:
        orm_mode = True

