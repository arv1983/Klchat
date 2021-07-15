from app.services.services import add_commit
from flask import Blueprint,request, jsonify
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.clientes_model import Clientes
from app.models.pivo_carrinho_produto_model import Carrinho_Produto
from datetime import date


bp = Blueprint("carrinho_route", __name__)

@bp.route("/carrinho", methods=["POST"])
@jwt_required()
def inserir_carrinho():
    data = request.get_json()
    email = get_jwt_identity()
    
    cliente = Clientes.query.filter_by(email=email).first()
    
    item = {
        "produto_id": data.get("produto_id", None),
        "quantidade": data.get("quantidade", 1),
        "carrinho_id": cliente.carrinho_id,
        "data_prod_inserida": date.today()
    }

    itens_carrinho = Carrinho_Produto(**item)
    add_commit(itens_carrinho)

    return {"msg": "Produto inserido"}