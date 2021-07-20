from http import HTTPStatus
from app.exc import InputError
from flask import request, Blueprint, jsonify

from app.models.clientes_model import Clientes
from app.services.services import add_commit
from app.models.lojistas_model import Lojistas
from app.models.carrinho_model import Carrinho

from app.services.validator_signup import ValidatorSignup

import ipdb
import json

bp = Blueprint("bp_signup", __name__)


@bp.route("/signup", methods=["POST"])
def signup():

    try:
        validator = ValidatorSignup()
        data = request.get_json()
        data = validator.signup(data)
    except InputError as err:
        return err.args

    # Salva dado em lojista ou cliente.
    if data["tipo_usuario"] == "lojista":

        data.pop("tipo_usuario")

        new_lojista = Lojistas(**data)
        new_lojista.password = data.get("senha")
        add_commit(new_lojista)

        return jsonify(new_lojista), HTTPStatus.CREATED
    else:

        data.pop("tipo_usuario")

        new_cliente = Clientes(**data)
        new_cliente.password = data.get("senha")

        add_commit(new_cliente)

        # Quando cria cliente ele recebe um carrinho_id;
        new_carrinho = Carrinho(cliente_id=new_cliente.id, status_id=1)
        add_commit(new_carrinho)
        new_cliente.carrinho_id = new_carrinho.id
        add_commit(new_cliente)

        return jsonify(new_cliente), HTTPStatus.CREATED
