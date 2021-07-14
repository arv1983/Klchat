from flask import request, Blueprint
from http import HTTPStatus
from app.services.services import add_commit
from sqlalchemy.sql.elements import BinaryExpression
from app.models.clientes_model import Clientes
from app.models.endereco_model import Endereco

from flask_jwt_extended import get_jwt_identity, jwt_required


bp = Blueprint("bp_perfil", __name__)

# @jwt_required()
@bp.route("/perfil", methods=["POST", "PATCH"])
def perfil():
    data = request.get_json()
    print(data)

    # if request.method == 'POST':
    #     possible_vars = ["logradouro", "numero", "complemento", "bairro", "cidade", "estado", "cep"]
    #     if not all(name in possible_vars for name in data.keys()):
    #         keys_w = {value for value in data.keys() if not value in possible_vars}
    #         return {"available_keys": possible_vars, "wrong_keys_sended": list(keys_w)},422

    #     cliente = Clientes.query.filter_by(email=get_jwt_identity).first()
    #     record_db = Endereco(**data)
    #     record_db['id'] = cliente['id']
    #     add_commit(record_db)
    #     print("endereco Cadastrado")