import re
from http import HTTPStatus

from app.exc import InputError


class ValidatorRegex:
    @staticmethod
    def email(email: str) -> bool:
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        if re.match(regex, email):
            return True

        return False

    @staticmethod
    def telefone(telefone: str) -> bool:
        regex1 = r"\b([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})\b"

        if re.match(regex1, telefone):
            return True

        return False

    @staticmethod
    def cpf(cpf: str) -> bool:

        cpf = "".join(re.findall(r"\d", str(cpf)))

        if not cpf or len(cpf) < 11:
            raise InputError(
                {"Error": "CPF inválido, precisa minimo 11 números", "Recebido": cpf},
                HTTPStatus.BAD_REQUEST,
            )

        antigo = [int(d) for d in cpf]

        novo = antigo[:9]
        while len(novo) < 11:
            resto = sum([v * (len(novo) + 1 - i) for i, v in enumerate(novo)]) % 11

            digito_verificador = 0 if resto <= 1 else 11 - resto

            novo.append(digito_verificador)

        if novo != antigo:
            raise InputError(
                {"Error": "CPF inválido, número cpf inválido", "Recebido": cpf},
                HTTPStatus.BAD_REQUEST,
            )

        return cpf

    @staticmethod
    def cnpj(cnpj: str) -> bool:
        pass
