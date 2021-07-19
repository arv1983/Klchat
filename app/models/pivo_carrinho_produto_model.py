from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import Date

from app.configs.database import db


@dataclass
class Carrinho_Produto(db.Model):
    id: int
    quantidade: Float
    valor_unitario: Float
    produto_id: int

    __tablename__ = "pivo_carrinho_produtos"

    id = Column(Integer, primary_key=True)
    quantidade = Column(Float, nullable=False)
    valor_unitario = Column(Float, nullable=False, default=0)
    data_prod_inserida = Column(Date, nullable=False)

    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    carrinho_id = Column(Integer, ForeignKey("carrinho.id"), nullable=False)
    lojista_id = Column(Integer, nullable=False)


    pivo_produto = relationship("Produtos", backref=backref("produto_pivo"))
    pivo_carrinho = relationship("Carrinho", backref=backref("carrinho_pivo"))

    
    
