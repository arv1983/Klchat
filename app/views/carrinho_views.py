from flask import Blueprint,request, jsonify
from http import HTTPStatus
from flask_jwt_extended import create_access_token
from app.models.clientes_model import Clientes
from app.models.lojistas_model import Lojistas


bp = Blueprint("carrinho_route", __name__)

@bp.route("/carrinho", methods=["POST"])
def inserir_carrinho():
    ...