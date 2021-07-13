from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass

from app.configs.database import db

@dataclass
class Lojistas(db.Model):
    id: int
    nome: str
    email: str
    senha: str
    cnpj: str
    telefone: str
    endereco_id: int

    __tablename__ = "lojistas"

    id = Column(Integer, nullable=False, primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    cnpj = Column(String(14), nullable=False)
    telefone = Column(String(11), nullable=False)
    endereco_id = Column(Integer, ForeignKey("endereco.id"), nullable=True)

    lojista_endereco = relationship("Enderecos", backref=backref("endereco_lojista"))
