from app.services.services import add_commit
from flask import Blueprint, request, jsonify
from sqlalchemy.sql.elements import Null
from werkzeug.utils import append_slash_redirect
from app.models.produtos_model import Produtos
from flask_jwt_extended import get_jwt_identity,jwt_required 
from http import HTTPStatus
bp = Blueprint("produto_route",__name__)


@bp.post("/produtos")
# @jwt_required()
def create_product():
    produto= request.get_json()
    add_commit(Produtos(**produto))
    return produto, HTTPStatus.CREATED
    
@bp.get("/produtos")
def get_produtos():
    produtos = Produtos.query.all()
    data = [produto.serialized for produto in produtos]
    return jsonify(data), HTTPStatus.OK


@bp.get("/produto")
def get_produto():
    from ipdb import set_trace
    produto = Produtos.query.filter(Produtos.descricao.in_("Fone")).all()
    set_trace()
    return jsonify(produto.serialized), HTTPStatus.OK





# @bp.get("/produto/pesquisar/<string:query>")
# def get_produto(query):
#     produto = Produtos.query.filter_by(descricao=query)
#     return "", 404

