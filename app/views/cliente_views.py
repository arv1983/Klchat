from app.models.clientes_model import Clientes
from app.service.services import add_commit
from app.models.lojistas_model import Logistas
from flask import request, Blueprint

bp = Blueprint("bp_clientes", __name__)

@bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    print(data)

    if data["tipo_usuario"] == "logista":
        print("losgita")
        new_losgista = Logistas(**data)

        add_commit(new_losgista)

    else:
        print(data["cliente"])
        
        new_cliente = Clientes(**data)
        add_commit(new_cliente)

    return {"mensagem": "clientes"}