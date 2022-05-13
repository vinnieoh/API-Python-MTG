from sqlalchemy import Column, ForeignKey, Integer, String, column, DECIMAL, Boolean
from sqlalchemy.orm import relationship

from config.config import settings



class ListaCartasModel(settings.DBBaseModel):
    __tablename__ = 'lista_cartas'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    cartas: any = relationship('CartaModel', backref='ListaCartasModel')


class CartaModel(settings.DBBaseModel):
    __tablename__ = 'cartas'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    edicao: str = Column(String(100))
    idioma: str = Column(String(50))
    foil: bool = Column(Boolean)
    preco: DECIMAL = Column(DECIMAL)
    cont_cartas: int = Column(Integer)
    listaCartaId: int = Column(Integer, ForeignKey(ListaCartasModel.id), primary_key=True)