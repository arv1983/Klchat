from app.models.lojistas_model import Lojistas
from flask_jwt_extended import jwt_required
from app.models.clientes_model import Clientes


from flask import Blueprint, jsonify

bp = Blueprint("bp_perfil", __name__)


@bp.get("/lojistas/<int:lojista_id>")
@jwt_required()
def get_lojista_id(lojista_id):
    lojista = Lojistas.query.filter_by(id=lojista_id).first()
    if not lojista:
        return {"Error": "Lojista não encontrado."}, 404
    return jsonify(lojista.serialized)

@bp.get("/clientes/<int:cliente_id>")
@jwt_required()
def get_cliente_id(cliente_id):
    cliente = Clientes.query.filter_by(id=cliente_id).first()
    if not cliente:
        return {"Error": "Cliente não encontrado."}, 404
    return jsonify(cliente.serialized)

@bp.get("/clientes")
@jwt_required()
def get_all_clientes():
    clientes = Clientes.query.all()
    data = [cliente.serialized for cliente in clientes]
    return jsonify(data)

@bp.get("/lojistas")
@jwt_required()
def get_all_lojistas():
    lojistas = Lojistas.query.all()
    data = [lojista.serialized for lojista in lojistas]
    return jsonify(data)
