from flask import Blueprint,request
from http import HTTPStatus

from werkzeug.utils import redirect
from app.models.clientes_model import Clientes
from app.models.lojistas_model import Lojistas

def create_user():

    email_user = request.get_json("email")
    cliente = Clientes.query.filter_by(email=email_user).first()
    lojista = Lojistas.query.filter_by(email=email_user).first()
    msg={"Usuário não encontrado"}
    if cliente:
        user = cliente
    elif lojista:
        user = lojista
    if user and user.check_password(user.password):
        return redirect("/"), HTTPStatus.OK
    return msg, HTTPStatus.NOT_FOUND
    