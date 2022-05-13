from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.model import ListaCartasModel
from schemas.lista_cartas_schemas import ListaCartasSchemas
from config.deps import get_session


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ListaCartasSchemas)
async def post_lista_cartas(listaCarta: ListaCartasSchemas, db: AsyncSession=Depends(get_session)):
    novo_lista_carta = ListaCartasModel(nome=listaCarta.nome)

    db.add(novo_lista_carta)
    await db.commit()

    return novo_lista_carta


@router.get('/', response_model=List[ListaCartasSchemas])
async def get_lista_cartas(db: AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(ListaCartasModel)
        result = await session.execute(query)
        listaCartas: List[ListaCartasModel] = result.scalars().all()

        return listaCartas


@router.get('/{listaCartas_id}', response_model=ListaCartasSchemas, status_code=status.HTTP_200_OK)
async def get_lista_cartas(listaCartas_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ListaCartasModel).filter(ListaCartasModel.id == listaCartas_id)
        result = await session.execute(query)
        lista_cartas = result.scalar_one_or_none()

        if lista_cartas:
            return lista_cartas
        else:
            raise HTTPException(detail='Curso não encontrado.',status_code=status.HTTP_404_NOT_FOUND)


@router.put('/{listaCartas_id}', response_model=ListaCartasSchemas, status_code=status.HTTP_202_ACCEPTED)
async def put_lista_cartas(listaCartas_id: int, lista_cartas: ListaCartasSchemas, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ListaCartasModel).filter(ListaCartasModel.id == listaCartas_id)
        result = await session.execute(query)
        lista_cartas_up = result.scalar_one_or_none()

        if lista_cartas_up:
            lista_cartas_up.nome = lista_cartas.nome

            await session.commit()

            return lista_cartas_up
        else:
            raise HTTPException(detail='Curso não encontrado.',status_code=status.HTTP_404_NOT_FOUND)



@router.delete('/{listaCartas_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_lista_cartas(listaCartas_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ListaCartasModel).filter(ListaCartasModel.id == listaCartas_id)
        result = await session.execute(query)
        listaCartas_del = result.scalar_one_or_none()

        if listaCartas_del:
            await session.delete(listaCartas_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Curso não encontrado.',status_code=status.HTTP_404_NOT_FOUND)
