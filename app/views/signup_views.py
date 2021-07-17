from http import HTTPStatus
from app.exc import InputError
from flask import request, Blueprint, jsonify

from app.models.clientes_model import Clientes
from app.services.services import add_commit
from app.models.lojistas_model import Lojistas
from app.models.carrinho_model import Carrinho

from app.services.validator_signup import ValidatorSignup
from app.services.regex import ValidatorRegex

bp = Blueprint("bp_signup", __name__)


@bp.route("/signup", methods=["POST"])
def signup():

    try:
        validator = ValidatorSignup()
        data = request.get_json()
        data = validator.signup(data)
    except InputError as err:
        return err.args

    if data["tipo_usuario"] == "lojista":

        lojista = {
            "nome": data.get("nome", None),
            "email": data.get("email", None),
            "cnpj": data.get("cnpj", None),
            "telefone": data.get("telefone", None),
        }

        new_lojista = Lojistas(**lojista)
        new_lojista.password = data.get("senha")

        add_commit(new_lojista)

        return jsonify(new_lojista)
    else:

        cliente = {
            "nome": data.get("nome", None),
            "email": data.get("email", None),
            "cpf": data.get("cpf", None),
            "cnpj": data.get("cnpj", None),
            "telefone": data.get("telefone", None),
        }

        new_cliente = Clientes(**cliente)
        new_cliente.password = data.get("senha")

        add_commit(new_cliente)
        new_carrinho = Carrinho(cliente_id=new_cliente.id, status_id=1)
        add_commit(new_carrinho)
        new_cliente.carrinho_id = new_carrinho.id
        add_commit(new_cliente)

        return new_cliente.serialized
