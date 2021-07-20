from app.models.vendas_model import Vendas
from app.exc import InputError
from app.services.validator_vendas import ValidatorVendas
from app.models.produtos_model import Produtos
from app.services.services import add_commit
from flask import Blueprint,request, jsonify, current_app
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.pivo_carrinho_produto_model import Carrinho_Produto
from datetime import datetime


bp = Blueprint("vendas_route", __name__)

@bp.get("/vendas/<int:venda_id>/aprovar")
@jwt_required()
def aprovar_venda(venda_id):
    try:
        lojista = ValidatorVendas.check_lojista(get_jwt_identity())
        venda = Vendas.query.filter_by(id=venda_id).first()
        ValidatorVendas.check_venda(venda, lojista.id)
        ValidatorVendas.check_stock(venda.carrinho_id)
        venda.status_id = 3

        add_commit(venda)
        return jsonify(venda)
    except InputError as err:
        return err.args

    except AttributeError as err:
        return err.args


@bp.get("/vendas/<int:venda_id>/despachar")
@jwt_required()
def despachar_venda():
    ...

@bp.get("/vendas/<int:venda_id>/cancelar")
@jwt_required()
def cancelar_venda():
    ...

@bp.get("/vendas/<int:venda_id>")
@jwt_required()
def ver_venda_by_id():
    ...

@bp.get("/vendas")
@jwt_required()
def ver_vendas():
    ...