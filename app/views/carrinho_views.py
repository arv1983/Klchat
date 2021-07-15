from flask import Blueprint,request, jsonify
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.clientes_model import Clientes
from app.models.lojistas_model import Lojistas
from app.models.produtos_model import Produtos
from app.models.carrinho_model import Carrinho
from datetime import date


bp = Blueprint("carrinho_route", __name__)

@bp.route("/carrinho", methods=["POST"])
@jwt_required
def inserir_carrinho():
    data = request.get_json()
    email = get_jwt_identity()
    cliente_id = Clientes.query.filter_by(email=email).first().id
    # carrinho_id = Carrinho.query.filter_by(cliente_id=cliente_id, status_id = 1).id
    item = {
        "produto_id": data.get("produto_id", None),
        "carrinho_id": "FALTA VER ISSO",
        "data": date.today(),
        "quantidade": data.get("quantidade", 1)
    }
