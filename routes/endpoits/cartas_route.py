from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.model import CartaModel
from schemas.cartas_schemas import CartaSchemas
from config.deps import get_session

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CartaSchemas)
async def post_lista_cartas(listaCarta: CartaSchemas, db: AsyncSession=Depends(get_session)):
    novo_carta = CartaModel(nome=listaCarta.nome)

    db.add(novo_carta)
    await db.commit()

    return novo_carta


