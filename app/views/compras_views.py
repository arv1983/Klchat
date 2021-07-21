from app.models.status_model import Status
from app.models.clientes_model import Clientes
from app.models.carrinho_model import Carrinho
from app.models.vendas_model import Vendas
from flask_jwt_extended import get_jwt_identity, jwt_required
from ipdb import set_trace

from flask import request, Blueprint, jsonify

bp = Blueprint("bp_compras", __name__)


@bp.get("/compras")
@jwt_required()
def compra():
    status = request.args.get("status", None)
    
    query_cliente = Clientes.query.filter_by(email=get_jwt_identity()).first()

    if not query_cliente:
        return {"Error": "Compras não disponível para lojistas."}, 401
    list_id = [item.id for item in Carrinho.query.filter_by(cliente_id=query_cliente.id).all()]
    
    if status:
        status_query = Status.query.filter_by(situacao=status.capitalize()).first()

    query_vendas = Vendas.query.filter(
        Vendas.carrinho_id.in_(list_id),
        Vendas.status_id == status_query.id if status else Vendas.status_id > 0,
        )

    list_vendas = []
    for item in query_vendas:
        list_vendas.append(item.serialized)

    return jsonify(list_vendas)