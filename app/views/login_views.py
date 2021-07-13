from flask import Blueprint,request
from http import HTTPStatus

from werkzeug.utils import redirect
from app.models.clientes_model import Clientes
from app.models.lojistas import Logistas

def create_user():

    email_user = request.get_json("email")
    cliente = Clientes.query.filter_by(email=email_user).first()
    lojista = Logistas.query.filter_by(email=email_user).first()
    msg={"Usuário não encontrado"}
    if cliente:
        user = cliente
    elif lojista:
        user = lojista
    if user and user.check_password(password_user):
        return redirect("/"), HTTPStatus.OK
    return msg, HTTPStatus.NOT_FOUND
    