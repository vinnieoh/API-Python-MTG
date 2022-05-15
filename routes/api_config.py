import imp
from fastapi import APIRouter

from routes.api_endpoint_v1 import lista_cartas_route

from routes.api_endpoint_v1 import cartas_route


api_router = APIRouter()

api_router.include_router(cartas_route.router, prefix='/cartas', tags=["cartas"])
api_router.include_router(lista_cartas_route.router, prefix='/lista-cartas', tags=["lista-cartas"])