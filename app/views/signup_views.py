from app.models.clientes_model import Clientes
from app.services.services import add_commit
from app.models.lojistas_model import Lojistas
from flask import request, Blueprint

bp = Blueprint("bp_clientes", __name__)

@bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    if data["tipo_usuario"] == "lojista":

        
        
        lojista = {
            "nome": data["nome"],
            "email": data["email"],
            "cnpj": data["cnpj"],
            "telefone": data["telefone"] 
        }
        
        
        new_lojista = Lojistas(**lojista)
        
        new_lojista.password(data["senha"])


        add_commit(new_lojista)

        print("Lojistas Cadastrado")
    else:
        cliente = {
            "nome": data["nome"],
            "email": data["email"],
            "cpf": data["cpf"] or "-",
            "cnpj": data["cnpj"] or "-",
            "telefone": data["telefone"] 
        }
        
        new_cliente = Clientes(**cliente)

        new_cliente.password(data["senha"])

        add_commit(new_cliente)

        print("Cliente Cadastrado")

    return {"mensagem": "clientes"}