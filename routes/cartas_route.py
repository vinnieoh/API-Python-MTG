from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.model import CartaModel
from schemas.cartas_schemas import CartaSchemas
from config.dependencies import get_session

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CartaSchemas)
async def post_cartas(carta: CartaSchemas, db: AsyncSession=Depends(get_session)):
    carta = CartaModel(nome=carta.nome, 
                       edicao=carta.edicao, 
                       idioma=carta.idioma, 
                       foil=carta.foil, 
                       preco=carta.preco, 
                       cont_cartas=carta.cont_cartas, 
                       listaCartaId=carta.listaCartaId)

    db.add(carta)
    await db.commit()

    return carta


@router.get('/{fk_id}', response_model=List[CartaSchemas])
async def get_cartas(fk_id: int,db: AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(CartaModel).filter(CartaModel.listaCartaId == fk_id )
        result = await session.execute(query)
        cartas: List[CartaModel] = result.scalars().all()

        return cartas


@router.get('/{cartas_id}', response_model=CartaSchemas, status_code=status.HTTP_200_OK)
async def get_cartas(cartas_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CartaModel).filter(CartaModel.id == cartas_id)
        result = await session.execute(query)
        lista_cartas = result.scalar_one_or_none()

        if lista_cartas:
            return lista_cartas
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.put('/{fk_id}/{cartas_id}', response_model=CartaSchemas, status_code=status.HTTP_202_ACCEPTED)
async def put_cartas( fk_id: int, cartas_id: int,cartas: CartaSchemas, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CartaModel).filter(CartaModel.id == cartas_id)
        result = await session.execute(query)
        cartas_up = result.scalar_one_or_none()

        if cartas_up:
            if cartas_up.listaCartaId == fk_id:
                cartas_up.nome = cartas.nome
                cartas_up.edicao = cartas.edicao
                cartas_up.idioma = cartas.idioma
                cartas_up.foil = cartas.foil
                cartas_up.preco = cartas.preco
                cartas_up.cont_cartas = cartas.cont_cartas
                cartas_up.listaCartaId = cartas.listaCartaId

                await session.commit()

                return cartas_up
            else:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete('/{cartas_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_cartas(cartas_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CartaModel).filter(CartaModel.id == cartas_id)
        result = await session.execute(query)
        cartas_del = result.scalar_one_or_none()

        if cartas_del:
            await session.delete(cartas_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)