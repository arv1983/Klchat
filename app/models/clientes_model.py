from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass

from configs.database import db


@dataclass
class Clientes(db.Model):
    id: int
    nome: str
    email: str
    senha: str
    cpf: str
    cnpj: str
    telefone: str
    endereco_id: int

    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)

    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    cpf = Column(String(11))
    cnpj = Column(String(14))
    telefone = Column(String(11), nullable=False)

    endereco_id = Column(Integer, ForeignKey("endereco.id"), nullable=False)

    cliente_enderco = relationship("Endereco", backref=backref("endereco_cliente"))
