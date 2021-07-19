from flask import Blueprint 


bp = Blueprint("bp_home",__name__)


@bp.get("/")
def home_page():
    page = """
            <h1 style="text-align: center">Seja bem vindo ao Klchat</h1>
            <br/>
            <p style="text-align: center"> Nossa documentação ainda não está pronta! </p>
            <p style="text-align: center">  Em breve teremos todas as instruções aqui! </p>
    """

    return page