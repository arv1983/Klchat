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
    def telefone(telefone: str) -> str:
        regex1 = r"\b([1-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})\b"

        _telefone = "".join(re.findall(r"\d", str(telefone)))

        if not re.match(regex1, _telefone):
            return False

        return _telefone

    @staticmethod
    def cpf(cpf: str) -> str:
        val_cpf = CPF()
        _cpf = "".join(re.findall(r"\d", str(cpf)))

        if not val_cpf.validate(_cpf):
            return False

        return _cpf

    @staticmethod
    def cnpj(cnpj: str) -> str:
        val_cnpj = CNPJ()

        _cnpj = "".join(re.findall(r"\d", str(cnpj)))

        if not val_cnpj.validate(_cnpj):
            return False

        return _cnpj
