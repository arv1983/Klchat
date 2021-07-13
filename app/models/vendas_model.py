from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass

from app.configs.database import db


@dataclass
class Vendas(db.Model):
    id: int
    valor_total: Float
    nota_fiscal: str
    status_id: int
    cliente_id: int
    lojista_id: int
    endereco_entrega_id: int
    itens_carrinho_id: int
    cupom_id: int

    __tablename__ = "vendas"

    id = Column(Integer, primary_key=True)
    valor_total = Column(Float, nullable=False)
    nota_fiscal = Column(String(255), nullable=False)
    status_id = Column(Integer, ForeignKey("status.id"), nullable=False)
    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    lojista_id = Column(Integer, ForeignKey("lojista.id"), nullable=False)
    endereco_entrega_id = Column(Integer, ForeignKey("endereco.id"), nullable=False)
    itens_carrinho_id = Column(Integer, ForeignKey("itens_carrinho.id"), nullable=False)
    cupom_id = Column(Integer, ForeignKey("cupom.id"), nullable=False, default=0)

    venda_status = relationship("Status", backref=backref("status_venda"))
    venda_cliente = relationship("Clientes", backref=backref("cliente_venda"))
    venda_lojista = relationship("Lojistas", backref=backref("cliente_venda"))
    venda_endereco = relationship("Enderecos", backref=backref("endereco_venda"))
    venda_item_carrinho = relationship(
        "ItensCarrinho", backref=backref("item_carrinho_venda")
    )
