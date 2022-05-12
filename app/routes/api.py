from fastapi import APIRouter

from app.routes import carta_route, lista_cartas_route


api_router = APIRouter()
api_router.include_router(carta_route.router, prefix='/carta', tags=["carta"])
api_router.include_router(lista_cartas_route, prefix='/lista-cartas', tags=["lista-cartas"])