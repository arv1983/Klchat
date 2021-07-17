from app.models.clientes_model import Clientes
from app.services.services import add_commit
from app.models.lojistas_model import Lojistas
from app.models.carrinho_model import Carrinho
from app.models.vendas_model import Vendas
from flask_jwt_extended import get_jwt_identity,jwt_required 

from flask import request, Blueprint, jsonify

bp = Blueprint("bp_vendas_andamento", __name__)
# provisorio
@bp.route("/vendas-andamento", methods=["GET"])
@jwt_required()
def venda():
    
    query_empresa = Lojistas.query.filter_by(email=get_jwt_identity()).first()
    query_cliente =  Clientes.query.filter_by(email=get_jwt_identity()).first()

    if query_cliente:
        query_carrinho = Carrinho.query.filter_by(cliente_id=query_cliente.id).all()
        # query_vendas = Vendas.query.filter_by(carrinho_id=query_carrinho.id).first()

        list_vendas = []
        for data in query_carrinho:
            query_vendas = Vendas.query.filter_by(carrinho_id=data.id).first()
            if not query_vendas:
                list_vendas.append(query_vendas)
        return jsonify(list_vendas)
    
    if query_empresa:
        query_carrinho = Vendas.query.filter_by(cliente_id=query_cliente.id).all()
        return {"empresa": "entrou"}
