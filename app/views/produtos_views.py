from app.services.validator_produtos import ValidatorProdutos
from app.exc import InputError
from app.services.services import add_commit
from flask import Blueprint, request, jsonify, current_app
from app.models.produtos_model import Produtos
from app.models.lojistas_model import Lojistas
from flask_jwt_extended import get_jwt_identity, jwt_required
from http import HTTPStatus

bp = Blueprint("produtos_route", __name__)


@bp.post("/produtos")
@jwt_required()
def create_product():
    try:
        produto = ValidatorProdutos()
        data = request.get_json()
        data = produto.produto(data)
    except InputError as e:
        return e.args

    lojista = Lojistas.query.filter_by(email=get_jwt_identity()).first()
    if lojista:
        data = request.get_json()
        data["lojista_id"] = lojista.id
        add_commit(Produtos(**data))
        return data, HTTPStatus.CREATED
    return {
        "msg": "Cadastro de produto não permitido para este usuário!"
    }, HTTPStatus.BAD_REQUEST

@bp.get("/produtos")
def search_produto():
    marca = request.args.get("marca", "")
    modelo = request.args.get("modelo", "")
    descricao = request.args.get("descricao", "")
    minimo = request.args.get("valor_min", 0)
    maximo = request.args.get("valor_max", 1000000000)
    lojista = request.args.get("lojista_id", None)

    produtos = Produtos.query.filter(
        Produtos.descricao.like(f"%{descricao}%"),
        Produtos.marca.like(f"%{marca}%"),
        Produtos.modelo.like(f"%{modelo}%"),
        Produtos.lojista_id == (lojista) if lojista else Produtos.lojista_id > 0,
        Produtos.valor_unitario >= minimo,
        Produtos.valor_unitario <= maximo
    ).order_by(Produtos.valor_unitario)
    data = [produto.serialized for produto in produtos]
    return jsonify(data), HTTPStatus.OK
