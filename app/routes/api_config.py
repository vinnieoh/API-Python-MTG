from fastapi import APIRouter

from . import cartas_route, lista_cartas_route


api_router = APIRouter()

#api_router.include_router(carta_route.router, prefix='/carta', tags=["carta"])
api_router.include_router(lista_cartas_route.router, prefix='/lista-cartas', tags=["lista-cartas"])