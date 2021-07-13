from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass

from configs.database import db


@dataclass
class ItensCarrinho(db.Model):
    id: int
    quantidade: Float
    valor_unitario: Float
    produto_id: int

    __tablename__ = "itens_carrinho"

    id = Column(Integer, primary_key=True)
    quantidade = Column(Float, nullable=False)
    valor_unitario = Column(Float, nullable=False)
    produto_id = Column(Integer, ForeignKey("produto.id"), nullable=False)

    item_carrinho_produto = relationship(
        "Produtos", backref=backref("produto_item_carrinho")
    )
