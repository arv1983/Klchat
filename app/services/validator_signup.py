from http import HTTPStatus

from sqlalchemy.sql.elements import Null

from app.exc import InputError

from app.services.regex import ValidatorRegex

from app.models.clientes_model import Clientes
from app.models.lojistas_model import Lojistas


class ValidatorSignup:

    SIGNUP = ["nome", "email", "tipo_usuario", "senha", "telefone"]
    TYPE_USUARIO = ["lojista", "cliente"]

    def signup(self, data: dict) -> dict:
        validate = ValidatorRegex()

        if not data:
            raise InputError(
                {"Error": "request sem dados.", "Obrigatórios": self.TYPE_USUARIO},
                HTTPStatus.BAD_REQUEST,
            )

        # ver dados obrigatorios
        requered = [req for req in self.SIGNUP if req not in data]

        if requered:
            raise InputError(
                {
                    "Error": "Faltam campos obrigatórios",
                    "recebido": [inf for inf in data],
                    "faltante": [req for req in requered],
                },
                HTTPStatus.BAD_REQUEST,
            )

        if not data.get("tipo_usuario"):
            data["tipo_usuario"] = "cliente"

        # Se algum campo está sem dados (ex: nome="")
        empty_data = [elm for elm in data if data[elm] == ""]

        if empty_data:
            raise InputError(
                {
                    "Error": "Os campos tem não podem ser vázio",
                    "recebido": [inf for inf in data],
                    "vázios": [empty for empty in empty_data],
                },
                HTTPStatus.BAD_REQUEST,
            )

        # validar e formata telefone
        _telefone = validate.telefone(data.get("telefone"))

        if not _telefone:
            raise InputError(
                {
                    "Error": "Telefone com erro",
                    "recebido": _telefone,
                },
                HTTPStatus.BAD_REQUEST,
            )

        data["telefone"] = _telefone

        # validar senha minimo 4
        if len(data.get("senha")) < 4:
            raise InputError(
                {
                    "Error": "Senha precisa no mínimo 4 caracteres!",
                    "recebido": data.get("senha"),
                },
                HTTPStatus.BAD_REQUEST,
            )

        # valiar email
        if not ValidatorRegex.email(data.get("email")):
            raise InputError(
                {
                    "Error": "Email com erro",
                    "recebido": data.get("email"),
                },
                HTTPStatus.BAD_REQUEST,
            )

        # Validacao  se lojista
        if data.get("tipo_usuario") == "lojista":
            # cnpj
            _cnpj = validate.cnpj(data.get("cnpj"))
            if not _cnpj:
                raise InputError(
                    {
                        "Error": "cnpj com erro ou não enviado",
                        "recebido": _cnpj,
                    },
                    HTTPStatus.BAD_REQUEST,
                )
            data["cnpj"] = _cnpj

            # se email em db
            loj_email = Lojistas.query.filter_by(email=data.get("email")).first()

            loj_cnpj = Lojistas.query.filter_by(cnpj=data.get("cnpj")).first()

            if loj_cnpj or loj_email:
                raise InputError(
                    {
                        "Error": "Email ou cnpj já cadastrado",
                        "recebido": {"cnpj": _cnpj, "email": data.get("email")},
                    },
                    HTTPStatus.BAD_REQUEST,
                )

        # Validação se Cliente
        else:
            # cpf / cnpj
            _cpf = validate.cpf(data.get("cpf", None))
            _cnpj = validate.cnpj(data.get("cnpj", None))

            if not _cpf and not _cnpj:
                raise InputError(
                    {
                        "Error": "cpf ou cnpj com erro ou não enviado, obrigatório um dos dois.",
                        "recebido": _cpf if _cpf else _cnpj,
                    },
                    HTTPStatus.BAD_REQUEST,
                )

            cli_cpf = None
            cli_cnpj = None
            cli_email = None

            if _cpf:
                data["cpf"] = _cpf
                cli_cpf = Clientes.query.filter_by(cpf=_cpf).first()
            if _cnpj:
                data["cnpj"] = _cnpj
                cli_cnpj = Clientes.query.filter_by(cnpj=_cnpj).first()

            # email in db
            cli_email = Clientes.query.filter_by(email=data.get("email")).first()

            print("cnpj", cli_cnpj, "cpf", cli_cpf, "email", cli_email)

            if cli_email or cli_cpf or cli_cnpj:
                raise InputError(
                    {
                        "Error": "Email, cpf ou cnpj já cadastrado",
                        "recebido": {
                            "email": data.get("email", None),
                            "cpf": data.get("cpf", None),
                            "cnpj": data.get("cnpj", None),
                        },
                    },
                    HTTPStatus.BAD_REQUEST,
                )

        return data
