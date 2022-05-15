from fastapi.testclient import TestClient
import requests

from models.model import ListaCartasModel
from tests.utils.create_lista_cartas import lista_cartas_create
from main import app    


client = TestClient(app)

URL: str = "/api/v1/lista-cartas/"


def test_route_lista_cartas_get():
   response = client.get(URL)
   assert response.status_code == 200


def test_route_lista_cartas_post():

   list_cartas = lista_cartas_create

   response = client.post(url=URL, json=list_cartas)
   content = response.json()

   assert response.status_code == 201
   assert content["nome"] == list_cartas["nome"]


def test_route_lista_cartas_get_id():

   response = client.get("/lista-cartas/{1}")

   assert response.status_code == 404


def test_route_lista_cartas_put():
   ...


def test_route_lista_cartas_del():
   ...