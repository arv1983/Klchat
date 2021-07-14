from flask import Blueprint,request, jsonify
from http import HTTPStatus
from flask_jwt_extended import create_access_token
from app.models.clientes_model import Clientes
from app.models.lojistas_model import Lojistas


bp= Blueprint("login_route", __name__)

@bp.route("/login", methods=["POST"])
def login():
    user = False
    email = request.json.get("email", None)
    senha = request.json.get("senha", None)
    cliente = Clientes.query.filter_by(email=email).first()
    lojista = Lojistas.query.filter_by(email=email).first()
    if cliente:
        user = cliente
    elif lojista:
        user = lojista

    if user and user.check_password(senha):
        token = create_access_token(identity=email)
        return jsonify(access_token=token)
    return jsonify(msg="Usuário e/ou senha inválidos"), HTTPStatus.BAD_REQUEST