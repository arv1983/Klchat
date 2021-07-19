from sqlalchemy import Column, Integer, String
from dataclasses import dataclass

from app.configs.database import db


@dataclass
class Endereco(db.Model):
    id: int
    logradouro: str
    numero: str
    complemento: str
    bairro: str
    cidade: str
    estado: str
    cep: str

    __tablename__ = "endereco"

    id = Column(Integer, primary_key=True)
    logradouro = Column(String(255), nullable=False)
    numero = Column(String(255), nullable=False)
    complemento = Column(String(255))
    bairro = Column(String(255), nullable=False)
    cidade = Column(String(255), nullable=False)
    estado = Column(String(2), nullable=False)
    cep = Column(String(8), nullable=False)
