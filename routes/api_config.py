from fastapi import APIRouter

from .endpoits import lista_cartas_route, cartas_route


api_router = APIRouter()

api_router.include_router(cartas_route.router, prefix='/carta', tags=["carta"])
api_router.include_router(lista_cartas_route.router, prefix='/lista-cartas', tags=["lista-cartas"])