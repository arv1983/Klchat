from http import HTTPStatus

from sqlalchemy.sql.elements import Null

from app.exc import InputError

from app.services.regex import ValidatorRegex

from app.models.clientes_model import Clientes
from app.models.lojistas_model import Lojistas


class ValidatorSignup:

    SIGNUP = ["nome", "email", "tipo_usuario", "senha", "telefone"]
    TYPE_USUARIO = ["lojista", "cliente"]

    def signup(self, data: dict):
        validate = ValidatorRegex()

        if not data:
            raise InputError(
                {
                    "Error": "request sem dados no body.",
                    "São obrigatórios": {
                        "tipo_usuário": self.TYPE_USUARIO,
                        "Campos obrigatórios": self.SIGNUP,
                    },
                },
                HTTPStatus.BAD_REQUEST,
            )

        # ver dados obrigatorios
        requered = [req for req in self.SIGNUP if req not in data]

        if requered:
            raise InputError(
                {
                    "Error": "Faltam campos obrigatórios",
                    "recebido": [inf for inf in data],
                    "faltantes": {
                        "Campos": requered,
                        "pessoa Física": "cpf",
                        "pessoa Jurídica": "cnpj",
                    },
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
                    "Error": "Telefone inválido, precisa de 11 digitros",
                },
                HTTPStatus.BAD_REQUEST,
            )

        data["telefone"] = _telefone

        # validar senha minimo 4
        _senha = str(data.get("senha"))
        if len(data.get("senha")) < 4:
            raise InputError(
                {
                    "Error": "Senha com mínimo 4 caracteres!",
                },
                HTTPStatus.BAD_REQUEST,
            )
        data["senha"] = _senha

        # validar email
        _email = validate.email(data.get("email", None))
        if not _email:
            raise InputError(
                {
                    "Error": "Email com formato inválido.",
                },
                HTTPStatus.BAD_REQUEST,
            )

        # cpf / cnpj
        if not data.get("cpf", None) and not data.get("cnpj", None):
            raise InputError(
                {
                    "Error": "cpf e ou cnpj não enviado",
                    "pessoa Físcia": "Obrigatório cadastrar cpf",
                    "pessoa jurídica": "Obrigatório cadastrar cnpj",
                }
            )

        # Valida cpf e cnpj
        _cpf = validate.cpf(data.get("cpf", None))
        _cnpj = validate.cnpj(data.get("cnpj", None))

        # Validacao  se lojista
        if data.get("tipo_usuario") == "lojista":

            if not _cnpj:
                raise InputError(
                    {"Error": "cnpj inválido"},
                    HTTPStatus.BAD_REQUEST,
                )
            data["cnpj"] = _cnpj

            # verifica email e cnpj existe no db lojista
            loj_email = Lojistas.query.filter_by(email=data.get("email")).first()
            loj_cnpj = Lojistas.query.filter_by(cnpj=data.get("cnpj")).first()

            if loj_cnpj or loj_email:
                raise InputError(
                    {
                        "Error": "Email e ou cnpj já cadastrado",
                    },
                    HTTPStatus.BAD_REQUEST,
                )

        # Validação se Cliente
        else:

            if not _cpf and not _cnpj:
                raise InputError(
                    {
                        "Error": "cpf ou cnpj inválido.",
                    },
                    HTTPStatus.BAD_REQUEST,
                )

            cli_cpf = None
            cli_cnpj = None
            cli_email = None

            # Verifica se cpf, cnpj ou email existe no db cliente
            if _cpf:
                data["cpf"] = _cpf
                cli_cpf = Clientes.query.filter_by(cpf=_cpf).first()
            if _cnpj:
                data["cnpj"] = _cnpj
                cli_cnpj = Clientes.query.filter_by(cnpj=_cnpj).first()

            cli_email = Clientes.query.filter_by(email=_email).first()

            print("cnpj", cli_cnpj, "cpf", cli_cpf, "email", cli_email)

            if cli_email or cli_cpf or cli_cnpj:
                raise InputError(
                    {
                        "Error": "Email, cpf e ou cnpj já cadastrado",
                    },
                    HTTPStatus.BAD_REQUEST,
                )

        return data
