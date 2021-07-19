from app.models.pivo_carrinho_produto_model import Carrinho_Produto
from app.models.clientes_model import Clientes
from app.exc import InputError
from app.models.produtos_model import Produtos
from http import HTTPStatus



class ValidatorCarrinho:

    def found_product(produto_id: int):
        produto = Produtos.query.filter_by(id=produto_id).first()
        if not produto:
            raise AttributeError(
                {"Error": "Produto não encontrado."},
                HTTPStatus.BAD_REQUEST,
            )
        return produto

    def verify_request_data(data: dict) -> dict:
        if not data or not data.get("produto_id", None):
            raise InputError(
                {"Error": "Request faltando dados obrigatórios.", 
                "Obrigatórios": {"produto_id": "Um valor do tipo inteiro."},
                "Opcionais": {"quantidade": "Um valor do tipo inteiro ou float."}},
                HTTPStatus.BAD_REQUEST,
            )
        
        id = data.get("produto_id")
        quantidade = data.get("quantidade",1)

        try:
            data = {
                "produto_id": int(id),
                "quantidade": float(quantidade)
            }
        except:
            raise InputError(
                {"Error": "Valor informado é inválido.", 
                "Recebido": data,
                "Esperado": {
                    "produto_id": "Um valor do tipo inteiro.",
                    "quantidade": "Um valor do tipo inteiro ou float."
                    }},
                HTTPStatus.BAD_REQUEST,
            )

        return data

    def check_stock(produto: Produtos, quantidade):
        if quantidade <= 0:
            raise AttributeError(
                {"Error": "Quantidade precisa ser maior que 0."},
                HTTPStatus.BAD_REQUEST,
            )
        if produto.qtd_estoque < quantidade:
            raise AttributeError(
                {"Error": "A loja não possui esta quantidade no estoque.",
                "Recebido": float(quantidade),
                "Disponível": produto.qtd_estoque
                },
                HTTPStatus.BAD_REQUEST,
            )

    def check_client(email):
        cliente = Clientes.query.filter_by(email=email).first()
        if not cliente:
            raise AttributeError(
                {"Error": "Carrinho não disponível para este usuário."},
                HTTPStatus.BAD_REQUEST,
            )
        return cliente

    def check_data_edit_cart(data):
        quantidade = data.get("quantidade", None)
        if not data or not quantidade:
            raise InputError(
                {"Error": "Request faltando dados obrigatórios.", 
                "Obrigatórios": {"quantidade": "Um valor do tipo inteiro ou float."}},
                HTTPStatus.BAD_REQUEST,
            )

        try:
            data = {
                "quantidade": float(quantidade)
            }
        except:
            raise InputError(
                {"Error": "Valor informado é inválido.", 
                "Recebido": data,
                "Esperado": {
                    "quantidade": "Um valor do tipo inteiro ou float."
                    }},
                HTTPStatus.BAD_REQUEST,
            )

        return data["quantidade"]

    def check_prod_in_cart(carrinho_id, produto_id):
        produto = Carrinho_Produto.query.filter_by(
        carrinho_id=carrinho_id, 
        produto_id=produto_id
        ).first()
        if not produto:
            raise AttributeError(
                {"Error": "Este produto não se encontra neste carrinho."},
                HTTPStatus.BAD_REQUEST,
            )
        return produto


