from app.models.lojistas_model import Lojistas
from app.services.vendas import alterar_venda, ver_venda
from app.models.vendas_model import Vendas
from app.exc import InputError
from app.services.validator_vendas import ValidatorVendas
from app.models.produtos_model import Produtos
from app.services.services import add_commit
from flask import Blueprint, request, jsonify, current_app
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.pivo_carrinho_produto_model import Carrinho_Produto
from datetime import datetime


bp = Blueprint("vendas_route", __name__)


@bp.get("/vendas/<int:venda_id>/aprovar")
@jwt_required()
def aprovar_venda(venda_id):

    return alterar_venda(venda_id, get_jwt_identity(), "aprovar")


@bp.get("/vendas/<int:venda_id>/despachar")
@jwt_required()
def despachar_venda(venda_id):

    return alterar_venda(venda_id, get_jwt_identity(), "despachar")


@bp.get("/vendas/<int:venda_id>/cancelar")
@jwt_required()
def cancelar_venda(venda_id):

    return alterar_venda(venda_id, get_jwt_identity(), "cancelar")


@bp.get("/vendas/<int:venda_id>")
@jwt_required()
def ver_venda_by_id(venda_id):
    return ver_venda(venda_id, get_jwt_identity(), "ver")


@bp.get("/vendas")
@jwt_required()
def ver_vendas():
    data = request.get_json()

    print(data)

    if data:
        possible_vars = ["status"]
        if not all(name in possible_vars for name in data.keys()):
            keys_w = {value for value in data.keys() if not value in possible_vars}
            return {
                "available_keys": possible_vars,
                "wrong_keys_sended": list(keys_w),
            }, 422
        if data["status"] not in range(0, 6):
            return {"Valor do status deve ser": "1 a 5"}, 422

    query_empresa = Lojistas.query.filter_by(email=get_jwt_identity()).first()

    if not query_empresa:
        return {"Error": "Vendas não disponivel para clientes."}, 401

    carrinhos = []
    produtos_lojista = Carrinho_Produto.query.filter_by(
        lojista_id=query_empresa.id
    ).all()

    for item in produtos_lojista:
        if not item.carrinho_id in carrinhos:
            carrinhos.append(item.carrinho_id)

    retorna = []
    for compra in carrinhos:

        if not data:
            venda = Vendas.query.filter_by(carrinho_id=compra).all()
        else:
            venda = Vendas.query.filter_by(
                carrinho_id=compra, status_id=data["status"]
            ).all()

        if venda:
            for item in venda:

                retorna.append(item.serialized)
                venda = ""

    return jsonify(retorna)
