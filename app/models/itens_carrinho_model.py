from . import db
from sqlalchemy import Column, Integer, ForeignKey, Float

class ItensCarrinho(db.Model):
    __tablename__="itens_carrinho"

    id = Column(Integer, primary_key=True)
    produto_id = Column(Integer, ForeignKey("produto.id"), nullable=False)
    quantidade = Column(Float, nullable=False)
    valor_unitario = Column(Float, nullable=False)