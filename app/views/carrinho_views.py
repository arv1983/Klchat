from app.exc import InputError
from app.services.validator_carrinho import ValidatorCarrinho
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
    
    try:
        cliente = ValidatorCarrinho.check_client(get_jwt_identity())
        data = ValidatorCarrinho.verify_request_data(request.get_json())
        produto = ValidatorCarrinho.found_product(data.get("produto_id"))
        ValidatorCarrinho.check_stock(produto, data.get("quantidade", 1))
        
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

    except InputError as err:
        return err.args

    except AttributeError as err:
        return err.args
    
    
    

@bp.get("/carrinho")
@jwt_required()
def ver_carrinho():

    try:   
        cliente = ValidatorCarrinho.check_client(get_jwt_identity())
        
    except AttributeError as err:
        return err.args
    
    itens_carrinho = Carrinho_Produto.query.filter_by(carrinho_id=cliente.carrinho_id).all()
    produtos = []
    for item in itens_carrinho:
        produto = Produtos.query.filter_by(id=item.produto_id).first()
        produto_atual = {
            "id": produto.id,
            "descricao": produto.descricao,
            "marca": produto.marca,
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

bp.route("/carrinho/<int:produto_id>", methods=["PATCH", "PUT"])
@jwt_required()
def alterar_carrinho(produto_id):
    data = request.get_json()
    
    try:   
        cliente = ValidatorCarrinho.check_client(get_jwt_identity())
        
    except AttributeError as err:
        return err.args
    
    produto = Carrinho_Produto.query.filter_by(
        carrinho_id=cliente.carrinho_id, 
        produto_id=produto_id
        ).first()

    produto.quantidade = data["quantidade"]

    add_commit(produto)

    return produto