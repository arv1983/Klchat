from app.services.services import add_commit
from flask import Blueprint, request, jsonify
from app.models.produtos_model import Produtos
from app.models.lojistas_model import Lojistas
from flask_jwt_extended import get_jwt_identity,jwt_required 
from http import HTTPStatus
bp = Blueprint("produtos_route",__name__)

@bp.post("/produtos")
@jwt_required()
def create_product():
    lojista = Lojistas.query.filter_by(email=get_jwt_identity()).first()
    if lojista:
        data = request.get_json()
        data["lojista_id"] = lojista.id
        add_commit(Produtos(**data))
        return data, HTTPStatus.CREATED
    return {"msg": "Cadastro de produto não permitido para este usuário!"}, HTTPStatus.BAD_REQUEST
    
@bp.get("/produtos")
def get_all():
    produtos = Produtos.query.all()
    data = [produto.serialized for produto in produtos]
    return jsonify(data), HTTPStatus.OK

@bp.get("/produtos/<int:lojista_id>")
def get_all_by_lojista_id(lojista_id):
    produtos = Produtos.query.all()
    
    data = [produto.serialized for produto in produtos if produto.lojista_id == lojista_id]
    return jsonify(data), HTTPStatus.OK

@bp.post("/produtos/busca")
def search_produto():
    search = request.json.get("search", None)
    produtos = Produtos.query.filter(
            Produtos.descricao.like((f'%{search}%')) 
            | (Produtos.marca.like(f'%{search}%'))
            | (Produtos.fabricante.like(f'%{search}%')))
    data = [produto.serialized for produto in produtos]
    return jsonify(data), HTTPStatus.OK

