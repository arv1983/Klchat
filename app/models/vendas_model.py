from app.models.clientes_model import Clientes
from app.models.produtos_model import Produtos
from app.models.carrinho_model import Carrinho
from app.models.endereco_model import Endereco
from app.models.status_model import Status
from app.models.pivo_carrinho_produto_model import Carrinho_Produto
import datetime

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass


from app.configs.database import db


@dataclass
class Vendas(db.Model):
    id: int
    valor_total: Float
    nota_fiscal: str
    cupom_id: int
    data_venda: datetime
    status_id: int
    endereco_entrega_id: int
    carrinho_id: int

    __tablename__ = "vendas"

    id = Column(Integer, primary_key=True)
    valor_total = Column(Float, nullable=False)
    nota_fiscal = Column(String(255))
    cupom_id = Column(Integer, nullable=False, default=0)
    data_venda = Column(DateTime, default=datetime.datetime.now )
    lojista_id = Column(Integer)
    endereco_entrega_id = Column(Integer, ForeignKey("endereco.id"), nullable=False)
    status_id = Column(Integer, ForeignKey("status.id"), nullable=False)
    carrinho_id = Column(Integer, ForeignKey("carrinho.id"), nullable=False)

    venda_status = relationship("Status", backref=backref("status_venda"))
    venda_endereco = relationship("Endereco", backref=backref("endereco_venda"))
    venda_carrinho = relationship("Carrinho", backref=backref("carrinho_venda"))

    @property
    def serialized(self):

        itens_carrinho = Carrinho_Produto.query.filter_by(
        carrinho_id=self.carrinho_id
        ).all()

        produtos = []

        for item in itens_carrinho:
            produto = Produtos.query.filter_by(id=item.produto_id).first()
            produto_atual = {
                "id": produto.id,
                "descricao": produto.descricao,
                "marca": produto.marca,
                "quantidade": item.quantidade,
                "valor_unitario": produto.valor_unitario,
            }
            produtos.append(produto_atual)
        status = Status.query.filter_by(id = self.status_id).first()
        carrinho = Carrinho.query.filter_by(id=self.carrinho_id).first()
        cliente = Clientes.query.filter_by(id = carrinho.cliente_id).first()
        endereco = Endereco.query.filter_by(id = self.endereco_entrega_id).first()
        data = {
            "venda_id": self.id,
            "valor_total": self.valor_total,
            "nota_fiscal": self.nota_fiscal,
            "data": self.data_venda,
            "status": status,
            "nome_cliente": cliente.nome,
        }
        endereco_entrega = {
            "Logradouro": endereco.logradouro,
            "Numero": endereco.numero,
            "Bairro": endereco.bairro,
            "Complemento": endereco.complemento,
            "Cidade": endereco.cidade,
            "Estado": endereco.estado,
            "CEP": endereco.cep
            }

        if cliente.cnpj:
            data["cnpj_cliente"] = cliente.cnpj
        if cliente.cpf:
            data["cpf_cliente"] = cliente.cpf

        data["endereco_entrega"] = endereco_entrega
        data["produtos"] = produtos
        return data
