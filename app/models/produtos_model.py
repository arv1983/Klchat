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
    lojista_id = Column(Integer, ForeignKey("lojistas.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)

    produto_lojista = relationship("Lojistas", backref=backref("lojista_produto"))
    produto_categoria = relationship("Categorias", backref=backref("categoria_produto"))

