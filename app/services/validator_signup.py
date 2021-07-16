from app.exc import InputError
from flask import Flask, current_app
from http import HTTPStatus

from app.models.clientes_model import Clientes
from app.models.lojistas_model import Lojistas


class ValidatorSignup:

    SIGNUP = ["nome", "email", "tipo_usuario", "senha", "cpf", "telefone"]
    TYPE_USUARIO = ["lojista", "cliente"]

    def signup(self, data: dict) -> bool:
        if not data:
            raise InputError(
                {"Error": "request sem dados.", "Obrigatórios": self.TYPE_USUARIO},
                HTTPStatus.BAD_REQUEST,
            )

        # ver dados obrigatorios
        requered = [req for req in data if not req in self.SIGNUP]

        # ver bug está, para resolver cpf / cnpj
        # if requered:
        #     raise InputError(
        #         {
        #             "Error": "Faltam campos obrigatórios",
        #             "recebido": [inf for inf in data],
        #             "faltante": [req for req in requered],
        #         },
        #         HTTPStatus.BAD_REQUEST,
        #     )

        if not data.get("tipo_usuario"):
            data["tipo_usuario"] = "cliente"

        # Se algum campo está sem dados (ex: nome="")
        empty_data = [error for error in data if data[error] == ""]

        if empty_data:
            raise InputError(
                {
                    "Error": "Os campos tem não podem ser vázio",
                    "recebido": [inf for inf in data],
                    "vázios": [empty for empty in empty_data],
                },
                HTTPStatus.BAD_REQUEST,
            )

        # validar telefone

        # validar senha minimo 4

        # Validacao  logista ou cliente
        if data.get("tipo_usuario") == "lojista":
            # valiar email
            # cnpj obrigatorio e se já existe
            pass

        else:
            pass

        return True
