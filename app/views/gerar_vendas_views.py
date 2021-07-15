from flask.json import jsonify
from app.models.vendas_model import Vendas
from flask import Blueprint ,request
from app.services.services import add_commit

bp = Blueprint("bp_gerar_venda",__name__)


@bp.route("/gerar-venda", methods=["POST"])
def home():
    data = request.get_json()

    new_venda = Vendas(**data)
    add_commit(new_venda)

    cliente = new_venda.venda_carrinho.carrinho_cliente


    venda = {
        'venda': new_venda,
        'cliente': cliente
    }

    return venda,200