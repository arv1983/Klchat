from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass

from sqlalchemy.sql.schema import ForeignKey

from app.configs.database import db


@dataclass
class Carrinho(db.Model):

    id: int
    cliente_id: int
    carrinho_cliente: int

    __tablename__ = "carrinho"

    id = Column(Integer, primary_key=True)

    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)

    status_id = Column(Integer, ForeignKey("status.id"))

    carrinho_cliente = relationship("Clientes", backref=backref("cliente_carrinho"))
