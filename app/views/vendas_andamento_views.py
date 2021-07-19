from app.models.clientes_model import Clientes
from app.services.services import add_commit
from app.models.lojistas_model import Lojistas
from app.models.carrinho_model import Carrinho
from app.models.vendas_model import Vendas
from app.models.produtos_model import Produtos
from app.models.pivo_carrinho_produto_model import Carrinho_Produto
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

        
        produtos_lojista = Produtos.query.filter_by(lojista_id=query_empresa.id).all()

        Carrinho_Produto.query.filter_by(produto_id=)
        print(produtos_lojista)



        # query_pivo = Carrinho_Produto.query.filter_by(cliente_id=query_cliente.id).all()
        # query_carrinho = Vendas.query.filter_by(cliente_id=query_cliente.id).all()
        # lojista - lojista id 1
        # produtos - cujo lojista_id e igual ao do lojista
        # pivo_carrinho_produtos - filtrar todos os produtos(que vao ser do lojista)
        # vendas - filtrar todos os id carrinho da tabela pivo_carrinho_produtos
        return {"empresa": "entrou"}


# @bp.route("/compras-andamento", methods=["GET"])
# @jwt_required()
# def compra():
#     query_cliente =  Clientes.query.filter_by(email=get_jwt_identity()).first()
#     if query_cliente:
#         query_carrinho = Carrinho.query.filter_by(cliente_id=query_cliente.id).all()
#         # query_vendas = Vendas.query.filter_by(carrinho_id=query_carrinho.id).first()

#         list_vendas = []
#         for data in query_carrinho:
#             query_vendas = Vendas.query.filter_by(carrinho_id=data.id).first()
#             if not query_vendas:
#                 list_vendas.append(query_vendas)
#         return jsonify(list_vendas)