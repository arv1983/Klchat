from enum import unique
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass

from app.configs.database import db

@dataclass
class Produtos(db.Model):
    id: int
    modelo: str
    descricao: str
    marca: str
    qtd_estoque: float
    lojista_id: int

    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    modelo = Column(String(100), nullable=False, unique=True)
    descricao = Column(String(255), nullable=False)
    marca = Column(String(255), nullable=False)
    qtd_estoque = Column(Float, nullable=False)
    valor_unitario = Column(Float, nullable=False)
    lojista_id = Column(Integer, ForeignKey("lojistas.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)

    produto_lojista = relationship("Lojistas", backref=backref("lojista_produto"))
    produto_categoria = relationship("Categorias", backref=backref("categoria_produto"))

    @property
    def serialized(self):
        return {
            "id": self.id,
            "modelo": self.modelo,
            "descricao": self.descricao,
            "marca": self.marca,
            "qtd_estoque": self.qtd_estoque,
            "valor_unitario": self.valor_unitario,
            "categoria_id": self.categoria_id,
            "lojista_id": self.lojista_id,
        }
