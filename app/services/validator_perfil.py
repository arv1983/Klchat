from http import HTTPStatus
import re

from app.exc import InputError

from app.services.regex import ValidatorRegex

from app.models.endereco_model import Endereco
from app.models.clientes_model import Clientes
from app.models.lojistas_model import Lojistas


class ValidatorPerfil:

    POSSIBLE_VAR = ["logradouro", "numero", "bairro", "cidade", "estado", "cep"]
    UF = ["RO","AC","AM","RR","PA","AP","TO","MA","PI","CE","RN","PB","PE","AL","SE","BA","MG","ES",
    "RJ","SP","PR","SC","RS","MS","MT","GO","DF"]


    def check_data(self, data: dict, user: object = False) -> dict:
        keys_w = [value for value in self.POSSIBLE_VAR if not value in data]
        
        
        if data.get("estado") not in self.UF:
            raise InputError({
              "Error UF": "UF inválida",
              "UF recebido":data.get("estado"),
              "Valores aceitos":self.UF,
        }, HTTPStatus.BAD_REQUEST)



        if keys_w:
            raise InputError(
                {
                    "error": "Falta dados obrigatórios",
                    "obrigatórios": self.POSSIBLE_VAR,
                    "faltante": keys_w,
                },
                HTTPStatus.BAD_REQUEST,
            )

        # Caso não venha o user, é uma atualização.
        if user:
            check = ValidatorPerfil.has_address(user)
            if check:
                address = Endereco.query.filter_by(id=user.endereco_id).first()
                raise InputError(
                    {
                        "Error": "Usuário já possui endereço",
                        "Info": "Para alterar use PUT",
                        "Endereco": address,
                    },
                    HTTPStatus.UNPROCESSABLE_ENTITY,
                )

        data["logradouro"] = data.get("logradouro").title()
        data["bairro"] = data.get("bairro").title()
        data["cidade"] = data.get("cidade").title()
        data["estado"] = data.get("estado").upper()
        _cep = "".join(re.findall(r"\d", str(data.get("cep"))))
        data["cep"] = _cep

        return data

    @staticmethod
    def has_address(user: object) -> bool:
        return user.endereco_id
