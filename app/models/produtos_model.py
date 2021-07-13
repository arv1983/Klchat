from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass

from app.configs.database import db


@dataclass
class Produtos(db.Model):
    id: int
    descricao: str
    marca: str
    fabricante: str
    qtd_estoque: Float
    lojista_id: int

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    descricao = Column(String(255), nullable=False)
    marca = Column(String(255), nullable=False)
    fabricante = Column(String(255), nullable=False)
    qtd_estoque = Column(Float, nullable=False)
    lojista_id = Column(Integer, ForeignKey("lojista.id"), nullable=False)

    produto_logista = relationship("Produtos", backref=backref("logista_produto"))
