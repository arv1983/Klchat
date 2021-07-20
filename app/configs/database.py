from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.endereco_model import Endereco
    from app.models.status_model import Status
    from app.models.categorias_model import Categorias

    from app.models.clientes_model import Clientes
    from app.models.lojistas_model import Lojistas

    from app.models.carrinho_model import Carrinho

    from app.models.pivo_carrinho_produto_model import Carrinho_Produto

    from app.models.produtos_model import Produtos

    from app.models.vendas_model import Vendas
