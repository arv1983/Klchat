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
    if not lojista:
        return {
        "msg": "Cadastro de produto não permitido para este tipo de usuário!"
         }, HTTPStatus.BAD_REQUEST
    data["lojista_id"] = lojista.id
    add_commit(Produtos(**data))
    return data, HTTPStatus.CREATED
    


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
        Produtos.valor_unitario <= maximo,
    ).order_by(Produtos.valor_unitario)
    data = [produto.serialized for produto in produtos]
    return jsonify(data), HTTPStatus.OK


@bp.patch("/produtos/<int:produto_id>")
@jwt_required()
def update_produto(produto_id):
    produto: Produtos
    produto = Produtos.query.filter_by(id=produto_id).first()

    validate = ValidatorProdutos()
    data = request.get_json()

    if not produto:
        return {"Error": "Produto não encontrado"}, HTTPStatus.NOT_FOUND

    lojista = Lojistas.query.filter_by(email=get_jwt_identity()).first()
    if produto.lojista_id != lojista.id:
        return {
            "Error": "Cadastro de produto não permitido para este tipo de usuário!",
            "lojista_id logado": lojista.id,
            "lojista_id do produto": produto.lojista_id,
        }, HTTPStatus.BAD_REQUEST

    if data.get("qtd_estoque"):
        qtd_nova = produto.qtd_estoque + float(data.get("qtd_estoque"))
        print(qtd_nova)
        data["qtd_estoque"] = qtd_nova

    try:
        elm = validate.valida_patch(data)

        for key, value in data.items():
            setattr(produto, key, value)

        add_commit(produto)

    except InputError as e:
        return e.args

    except Exception as e:
        return e.args, HTTPStatus.INTERNAL_SERVER_ERROR

    return {"inf": "Produto atualizado!"}, HTTPStatus.OK