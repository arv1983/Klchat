from app.models.produtos_model import Produtos
from app.services.services import add_commit
from flask import Blueprint,request, jsonify
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.clientes_model import Clientes
from app.models.pivo_carrinho_produto_model import Carrinho_Produto
from datetime import date


bp = Blueprint("carrinho_route", __name__)

@bp.post("/carrinho")
@jwt_required()
def inserir_carrinho():
    data = request.get_json()
    email = get_jwt_identity()
    
    cliente = Clientes.query.filter_by(email=email).first()
    produto = Produtos.query.filter_by(id=data.get("produto_id", None)).first()
    item = {
        "produto_id": produto.id,
        "quantidade": data.get("quantidade", 1),
        "carrinho_id": cliente.carrinho_id,
        "lojista_id": produto.lojista_id,
        "data_prod_inserida": date.today()
    }

    itens_carrinho = Carrinho_Produto(**item)
    add_commit(itens_carrinho)

    return {"msg": "Produto inserido"}

@bp.get("/carrinho")
@jwt_required()
def ver_carrinho():

    email = get_jwt_identity()
    
    cliente = Clientes.query.filter_by(email=email).first()
    
    itens_carrinho = Carrinho_Produto.query.filter_by(carrinho_id=cliente.carrinho_id).all()
    produtos = []
    for item in itens_carrinho:
        produto = Produtos.query.filter_by(id=item.produto_id).first()
        produto_atual = {
            "id": produto.id,
            "descricao": produto.descricao,
            "marca": produto.marca,
            "fabricante": produto.fabricante,
            "quantidade": item.quantidade,
            "valor_unitario": produto.valor_unitario,
            "lojista_id": produto.lojista_id
            
        }
        produtos.append(produto_atual)
    data = {
        "carrinho_id": cliente.carrinho_id,
        "produtos": produtos
    }
    

    return (jsonify(data))