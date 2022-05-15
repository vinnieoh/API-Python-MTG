from models.model import ListaCartasModel

from sqlalchemy_utils import assert_nullable, assert_non_nullable, assert_max_length



def test_model_nullable():
    lista_carta = ListaCartasModel(nome="vinicius")
    

    assert_max_length(lista_carta, 'nome')



