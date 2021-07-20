from datetime import date
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass

from sqlalchemy.sql.sqltypes import Date

from app.configs.database import db


@dataclass
class Vendas(db.Model):
    id: int
    valor_total: Float
    nota_fiscal: str
    cupom_id: int
    data_venda: date
    status_id: int
    endereco_entrega_id: int
    carrinho_id: int

    __tablename__ = "vendas"

    id = Column(Integer, primary_key=True)
    valor_total = Column(Float, nullable=False)
    nota_fiscal = Column(String(255))
    cupom_id = Column(Integer, nullable=False, default=0)
    data_venda = Column(Date, nullable=False)

    endereco_entrega_id = Column(Integer, ForeignKey("endereco.id"), nullable=False)
    status_id = Column(Integer, ForeignKey("status.id"), nullable=False)
    carrinho_id = Column(Integer, ForeignKey("carrinho.id"), nullable=False)

    venda_status = relationship("Status", backref=backref("status_venda"))
    venda_endereco = relationship("Endereco", backref=backref("endereco_venda"))
    venda_carrinho = relationship("Carrinho", backref=backref("carrinho_venda"))
