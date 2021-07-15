from flask import Blueprint
from sqlalchemy.sql.elements import Null
from app.models.produtos_model import Produtos

bp = Blueprint("produto_route",__name__)




@bp.get("/produto/pesquisar/<string:query>")
def get_produto(query):
    produto = Produtos.query.filter_by(descricao=query)
    return "", 404

