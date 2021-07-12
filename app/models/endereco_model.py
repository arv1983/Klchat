from ast import Str
from . import db
from sqlalchemy import Column, Integer, String

class Endereco(db.Model):
    __tablename__="endereco"

    endereco_int = Column(Integer, primary_key=True)
    logadouro=Column(String(255), nullable=False)
    numero=Column(String(255), nullable=False)
    complemento=Column(String(255), nullable=False)
    bairro = Column(String(255), nullable=False) 
    cidade = Column(String(255), nullable=False) 
    estado = Column(String(2), nullable=False) 
    cep = Column(String(8), nullable=False) 