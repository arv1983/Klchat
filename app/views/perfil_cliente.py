from flask import request, Blueprint, jsonify
from http import HTTPStatus
from app.services.services import add_commit
from sqlalchemy.sql.elements import BinaryExpression
from app.models.clientes_model import Clientes
from app.models.endereco_model import Endereco
from app.models.lojistas_model import Lojistas
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import current_app


bp = Blueprint("bp_perfil", __name__)


@bp.route("/perfil", methods=["POST", "PATCH"])
@jwt_required()
def perfil():
    data = request.get_json()

    if request.method == 'POST':
        possible_vars = ["logradouro", "numero", "complemento", "bairro", "cidade", "estado", "cep"]
        if not all(name in possible_vars for name in data.keys()):
            keys_w = {value for value in data.keys() if not value in possible_vars}
            return {"available_keys": possible_vars, "wrong_keys_sended": list(keys_w)},422

        cliente = Clientes.query.filter_by(email=get_jwt_identity()).first()
        empresa = Lojistas.query.filter_by(email=get_jwt_identity()).first()
        
        
        novo_endereco = Endereco(**data)
        add_commit(novo_endereco)

        if empresa:
            empresa.endereco_id = novo_endereco.id
            setattr(empresa, "endereco_id", novo_endereco.id)
            add_commit(empresa)

        if cliente:
            cliente.endereco_id = novo_endereco.id
            setattr(cliente, "endereco_id", novo_endereco.id)
            add_commit(cliente)
        
    return {'endeco': 'cadastrado'}