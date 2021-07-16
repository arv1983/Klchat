from app.exc import InputError, OptionError
from flask import Flask, current_app
from http import HTTPStatus

from app.models.clientes_model import Clientes
from app.models.lojistas_model import Lojistas




class ValidatorSignup:

    SIGNUP = ["name", "email", "tipo_usuario", "senha"]
    TYPE_USUARIO = ["lojista", "cliente"]

    def signup(self,data: dict) -> bool:

        if not data:
            raise InputError(
                {"Error": "request sem dados.", "Obrigatórios": self.TYPE_USUARIO},
                HTTPStatus.BAD_REQUEST,
            )

        if not data.get("tipo_usuario") in self.TYPE_USUARIO:
            raise OptionError(
                {
                    "Error": "tip_usuario inválido!",
                    "recebido": data.get("tipo_usuario"),
                    "opções": self.TYPE_USUARIO,
                },
                HTTPStatus.BAD_REQUEST,
            )

        # ver dados obrigatorios
        requered = [req for req in data if not req in self.SIGNUP]

        # validar telefone

        # valiar email

        # validar senha minimo 4

        # Validacao  logista ou cliente
        if data.get("tipo_usuario") == "lojista":
            # cnpj obrigatorio
            pass

        else:
            pass

        return True
