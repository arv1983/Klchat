from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.configs.database import db


class Vendas(db.Model):
    __tablename__ = "vendas"

    id = Column(Integer, primary_key=True)
    valor_total = Column(Float, nullable=False)
    nota_fiscal = Column(String(255), nullable=False)
    status_id = Column(Integer, ForeignKey("status.id"), nullable=False)
    cliente_id = Column(Integer, Foreignkey("cliente.id"), nullable=False)
    logista_id = Column(Integer, Foreignkey("logista.id"), nullable=False)
    endereco_entrega_id = Column(
        Integer, Foreignkey("endereco_entrea.id"), nullable=False
    )
    itens_carrinho_id = Column(Integer, Foreignkey("itens_carrinho.id"), nullable=False)
    cupom_id = Column(Integer, Foreignkey("cupom.id"), nullable=False, default=0)
