from app.models.vendas_model import Vendas
from app.exc import InputError
from app.services.validator_carrinho import ValidatorCarrinho
from app.models.produtos_model import Produtos
from app.services.services import add_commit
from flask import Blueprint, request, jsonify, current_app
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.pivo_carrinho_produto_model import Carrinho_Produto
from datetime import datetime
from ipdb import set_trace


bp = Blueprint("carrinho_route", __name__)


@bp.post("/carrinho")
@jwt_required()
def inserir_carrinho():

    try:
        cliente = ValidatorCarrinho.check_client(get_jwt_identity())
        data = ValidatorCarrinho.verify_request_data(request.get_json())
        try:
            verify = ValidatorCarrinho.check_prod_in_cart(
                cliente.carrinho_id, data.get("produto_id", None)
            )
            if verify:
                return {
                    "Error": "Este produto já está no carrinho"
                }, HTTPStatus.BAD_REQUEST
        except:

            produto = ValidatorCarrinho.found_product(data.get("produto_id"))
            ValidatorCarrinho.check_lojista(cliente.carrinho_id, produto.lojista_id)
            ValidatorCarrinho.check_stock(produto, data.get("quantidade", 1))

            item = {
                "produto_id": produto.id,
                "quantidade": data.get("quantidade", 1),
                "carrinho_id": cliente.carrinho_id,
                "lojista_id": produto.lojista_id,
                "data_prod_inserida": datetime.now(),
            }

            itens_carrinho = Carrinho_Produto(**item)
            add_commit(itens_carrinho)

            return {"msg": "Produto inserido"}

    except InputError as err:
        return err.args

    except AttributeError as err:
        return err.args


@bp.get("/carrinho")
@jwt_required()
def ver_carrinho():

    try:
        cliente = ValidatorCarrinho.check_client(get_jwt_identity())

    except AttributeError as err:
        return err.args

    itens_carrinho = Carrinho_Produto.query.filter_by(
        carrinho_id=cliente.carrinho_id
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
            "lojista_id": produto.lojista_id,
        }
        produtos.append(produto_atual)
    data = {"carrinho_id": cliente.carrinho_id, "produtos": produtos}

    return jsonify(data)


@bp.route("/carrinho/<int:produto_id>", methods=["PATCH", "PUT"])
@jwt_required()
def alterar_carrinho(produto_id):

    try:
        cliente = ValidatorCarrinho.check_client(get_jwt_identity())
        produto = ValidatorCarrinho.check_prod_in_cart(cliente.carrinho_id, produto_id)
        produto.quantidade = ValidatorCarrinho.check_data_edit_cart(request.get_json())
        prod_estoque = Produtos.query.filter_by(id=produto_id).first()
        ValidatorCarrinho.check_stock(prod_estoque, produto.quantidade)
    except AttributeError as err:
        return err.args
    except InputError as err:
        return err.args

    add_commit(produto)

    return jsonify(produto)


@bp.route("/carrinho/<int:produto_id>", methods=["DELETE"])
@jwt_required()
def delete_produto_carrinho(produto_id):
    try:
        cliente = ValidatorCarrinho.check_client(get_jwt_identity())
        produto = ValidatorCarrinho.check_prod_in_cart(cliente.carrinho_id, produto_id)
        session = current_app.db.session
        session.delete(produto)
        session.commit()
    except AttributeError as err:
        return err.args
    except InputError as err:
        return err.args

    return {}, HTTPStatus.NO_CONTENT


@bp.route("/carrinho", methods=["DELETE"])
@jwt_required()
def esvaziar_carrinho():
    try:
        session = current_app.db.session
        cliente = ValidatorCarrinho.check_client(get_jwt_identity())
        itens_carrinho = Carrinho_Produto.query.filter_by(
            carrinho_id=cliente.carrinho_id
        ).all()
        for item in itens_carrinho:
            session.delete(item)

        session.commit()
    except AttributeError as err:
        return err.args
    except InputError as err:
        return err.args

    return {}, HTTPStatus.NO_CONTENT


@bp.get("/finalizar-carrinho")
@jwt_required()
def home():

    try:
        cliente = ValidatorCarrinho.check_client(get_jwt_identity())
        carrinho_id = cliente.carrinho_id
        endereco_id = ValidatorCarrinho.check_endereco(cliente.endereco_id)
        itens_compra = ValidatorCarrinho.finish_cart(carrinho_id, cliente.id)
        carrinho = Carrinho_Produto.query.filter_by(carrinho_id = carrinho_id).first()
        valor_total = 0

        for item in itens_compra:
            produto_atual = Produtos.query.filter_by(id=item.produto_id).first()
            valor_total += produto_atual.valor_unitario

        data_venda = datetime.now()
        venda = {
            "valor_total": valor_total,
            "cupom_id": 0,
            "data_venda": data_venda,
            "endereco_entrega_id": endereco_id,
            "status_id": 2,
            "carrinho_id": carrinho_id,
            "lojista_id": carrinho.lojista_id
        }

        nova_venda = Vendas(**venda)
        add_commit(nova_venda)

        return jsonify(nova_venda.serialized), HTTPStatus.OK

    except AttributeError as err:
        return err.args
    except InputError as err:
        return err.args
