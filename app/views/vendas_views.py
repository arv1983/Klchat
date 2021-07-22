from app.models.status_model import Status
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
from ipdb import set_trace


bp = Blueprint("vendas_route", __name__)


@bp.patch("/vendas/<int:venda_id>/aprovar")
@jwt_required()
def aprovar_venda(venda_id):

    return alterar_venda(venda_id, get_jwt_identity(), "aprovar")


@bp.patch("/vendas/<int:venda_id>/despachar")
@jwt_required()
def despachar_venda(venda_id):

    return alterar_venda(venda_id, get_jwt_identity(), "despachar")


@bp.patch("/vendas/<int:venda_id>/cancelar")
@jwt_required()
def cancelar_venda(venda_id):

    return alterar_venda(venda_id, get_jwt_identity(), "cancelar")


@bp.get("/vendas/<int:venda_id>")
@jwt_required()
def ver_venda_by_id(venda_id):
    return ver_venda(venda_id, get_jwt_identity(), "ver")


@bp.get("/vendas")
@jwt_required()
def get_vendas():
    try:
        status = request.args.get("status", None)
        if status:
            status_query = Status.query.filter_by(situacao=status.capitalize()).first()
        
        lojista = ValidatorVendas.check_lojista(get_jwt_identity())
        
        vendas = Vendas.query.filter(
            Vendas.lojista_id == lojista.id,
            Vendas.status_id == status_query.id if status else Vendas.status_id > 0,
            )
        data = []

        for item in vendas:
            data.append(item.serialized)
        return jsonify(data)
        
    except InputError as err:
        return err.args

    except AttributeError as err:
        return err.args
