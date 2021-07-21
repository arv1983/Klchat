from flask import current_app
from flask import request, Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from http import HTTPStatus
from sqlalchemy.sql.elements import BinaryExpression
from sqlalchemy.sql.functions import user

from app.exc import InputError
from app.services.services import add_commit
from app.services.validator_perfil import ValidatorPerfil

from app.models.clientes_model import Clientes
from app.models.endereco_model import Endereco
from app.models.lojistas_model import Lojistas


bp = Blueprint("bp_endereco", __name__)


@bp.route("/endereco", methods=["POST", "GET", "PUT"])
@jwt_required()
def criar_endereco():
    data = request.get_json()

    cliente = Clientes.query.filter_by(email=get_jwt_identity()).first()
    empresa = Lojistas.query.filter_by(email=get_jwt_identity()).first()
    user = cliente if cliente else empresa

    validator = ValidatorPerfil()

    if request.method == "POST":
        try:
            data = validator.check_data(data, user)

        except InputError as err:
            return err.args

        novo_endereco = Endereco(**data)
        add_commit(novo_endereco)
        user.endereco_id = novo_endereco.id
        setattr(user, "endereco_id", novo_endereco.id)
        add_commit(user)

        return {"Ok": "Endereço cadastrado."}, HTTPStatus.CREATED

    if request.method == "GET":

        address = Endereco.query.filter_by(id=user.endereco_id).first()

        if address:
            return (
                jsonify(address),
                HTTPStatus.OK,
            )

        return {"Info": "Endereço não cadastrado"}, HTTPStatus.NOT_FOUND

    if request.method == "PUT":

        try:
            data = validator.check_data(data)
        except InputError as err:
            return err.args

        update_endereco = Endereco(**data)
        add_commit(update_endereco)
        user.endereco_id = update_endereco.id
        setattr(user, "endereco_id", update_endereco.id)
        add_commit(user)

        return jsonify({"Endereco": "Atualizado!"}), HTTPStatus.OK
