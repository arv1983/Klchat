from sqlalchemy.sql.elements import Null
from app.models.clientes_model import Clientes
from app.services.services import add_commit
from app.models.lojistas_model import Lojistas
from app.models.carrinho_model import Carrinho
from app.models.vendas_model import Vendas
from app.models.produtos_model import Produtos
from app.models.pivo_carrinho_produto_model import Carrinho_Produto
from flask_jwt_extended import get_jwt_identity, jwt_required

from flask import request, Blueprint, jsonify

bp = Blueprint("bp_vendas_andamento", __name__)
# provisorio
@bp.route("/vendas-andamento", methods=["GET"])
@jwt_required()
def venda():
    data = request.get_json()
    
    print(data)

    if data:
        possible_vars = ["status"]
        if not all(name in possible_vars for name in data.keys()):
            keys_w = {value for value in data.keys() if not value in possible_vars}
            return {"available_keys": possible_vars, "wrong_keys_sended": list(keys_w)},422
        if data['status'] not in range(0, 6):
            return {"Valor do status deve ser": "1 a 5"},422

    query_empresa = Lojistas.query.filter_by(email=get_jwt_identity()).first()

    if not query_empresa:
        return {'Error': 'Vendas não disponivel para clientes.'},401



    carrinhos = []
    produtos_lojista = Carrinho_Produto.query.filter_by(
        lojista_id=query_empresa.id
    ).all()

    for item in produtos_lojista:
        if not item.carrinho_id in carrinhos:
            carrinhos.append(item.carrinho_id)

    retorna = []
    for compra in carrinhos:

        if not data:
            venda = Vendas.query.filter_by(carrinho_id=compra).all()
        else:
            venda = Vendas.query.filter_by(
                carrinho_id=compra, status_id=data["status"]
            ).all()

        if venda:
            retorna.append(venda)
            venda = ""

    return jsonify(retorna)


@bp.route("/compras-andamento", methods=["GET"])
@jwt_required()
def compra():
    query_cliente = Clientes.query.filter_by(email=get_jwt_identity()).first()

    if not query_cliente:
        return {'Error': 'Vendas não disponível para clientes.'},401
    query_carrinho = Carrinho.query.filter_by(cliente_id=query_cliente.id).all()
    # query_vendas = Vendas.query.filter_by(carrinho_id=query_carrinho.id).first()

    list_vendas = []
    for data in query_carrinho:
        query_vendas = Vendas.query.filter_by(carrinho_id=data.id).first()
        if not query_vendas:
            list_vendas.append(query_vendas)
    return jsonify(list_vendas)
