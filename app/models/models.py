from sqlalchemy import Column, ForeignKey, Integer, String, column, Relationship, DECIMAL, Boolean

from config.config import settings



class ListaCartasModel(settings.DBBaseModel):
    __tabelename__ = 'listaCartas'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    cartas: any = Relationship('CartaModel', backref='ListaCartasModel')


class CartaModel(settings.DBBaseModel):
    __tabelename__ = 'cartas'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    edicao: str = Column(String(100))
    idioma: str = Column(String(50))
    foil: bool = column(Boolean(True))
    preco: DECIMAL = column(DECIMAL)
    cont_cartas: int = column(Integer)
    listaCartaId: int = column(Integer, ForeignKey('ListaCartasModel.id'))