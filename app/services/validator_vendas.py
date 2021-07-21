from app.models.status_model import Status
from app.models.vendas_model import Vendas
from app.services.services import add_commit
from app.models.carrinho_model import Carrinho
from app.models.pivo_carrinho_produto_model import Carrinho_Produto
from app.models.clientes_model import Clientes
from app.models.lojistas_model import Lojistas
from app.exc import InputError
from app.models.produtos_model import Produtos
from http import HTTPStatus
from ipdb import set_trace


class ValidatorVendas:
    def check_stock(carrinho_id):
        itens_carrinho = Carrinho_Produto.query.filter_by(carrinho_id=carrinho_id).all()
        for item in itens_carrinho:
            produto = Produtos.query.filter_by(id=item.produto_id).first()
            if produto.qtd_estoque < item.quantidade:
                raise AttributeError(
                    {
                        "Error": f"A loja não possui esta quantidade de {produto.descricao} no estoque.",
                        "Recebido": float(item.quantidade),
                        "Disponível": produto.qtd_estoque,
                    },
                    HTTPStatus.BAD_REQUEST,
                )
            produto.qtd_estoque -= item.quantidade
            add_commit(produto)

    def check_lojista(email):
        lojista = Lojistas.query.filter_by(email=email).first()

        if not lojista:
            raise AttributeError(
                {"Error": "Vendas não disponível para este usuário."},
                HTTPStatus.BAD_REQUEST,
            )

        return lojista

    def check_venda(venda, lojista_id, action):

        if action == "cancelar":
            text = "cancelada"
        elif action == "aprovar":
            text = "aprovada"
        elif action == "despachar":
            text = "despachada"
        else:
            text = None

        if not venda:
            raise AttributeError(
                {"Error": "Venda não encontrada."},
                HTTPStatus.BAD_REQUEST,
            )

        itens_carrinho = Carrinho_Produto.query.filter_by(
            carrinho_id=venda.carrinho_id
        ).first()

        if itens_carrinho.lojista_id != lojista_id:
            raise AttributeError(
                {"Error": "Venda não pertence a esta loja."},
                HTTPStatus.BAD_REQUEST,
            )

        if (
            (action == "aprovar" or action == "cancelar") and (venda.status_id != 2)
        ) or ((action == "despachar") and (venda.status_id != 3)):
            status = Status.query.filter_by(id=venda.status_id).first()
            raise AttributeError(
                {
                    "Error": f"Esta venda não pode ser {text}.",
                    "status_atual": {"situação": status.situacao},
                },
                HTTPStatus.BAD_REQUEST,
            )

    def finish_cart(carrinho_id, cliente_id):
        itens_carrinho = Carrinho_Produto.query.filter_by(carrinho_id=carrinho_id).all()
        if not itens_carrinho:
            raise AttributeError(
                {"Error": "Seu carrinho está vazio."},
                HTTPStatus.BAD_REQUEST,
            )

        carrinho_atual = Carrinho.query.filter_by(id=carrinho_id).first()
        carrinho_atual.status = 5
        add_commit(carrinho_atual)

        new_carrinho = Carrinho(cliente_id=cliente_id, status_id=1)
        add_commit(new_carrinho)

        cliente = Clientes.query.filter_by(id=cliente_id).first()
        cliente.carrinho_id = new_carrinho.id
        add_commit(cliente)

        return itens_carrinho
