from app.models.produtos_model import Produtos
from app.exc import InputError
from http import HTTPStatus


class ValidatorProdutos:

    campos = [
        "descricao",
        "marca",
        "modelo",
        "qtd_estoque",
        "valor_unitario",
        "categoria_id",
    ]

    def produto(self, data: dict):

        if not data:
            raise InputError(
                {"Error": "request sem dados", "Obrigatórios": self.campos},
                HTTPStatus.BAD_REQUEST,
            )

        requered = [req for req in self.campos if req not in data]
        if data:

            raise InputError(
                {
                    "Error": "Faltam campos obrigatórios",
                    "Recebido": [rec for rec in data],
                    "Faltante": [fal for fal in requered],
                },
                HTTPStatus.BAD_REQUEST,
            )

        produto = Produtos.query.filter_by(modelo=data.get("modelo")).first()

        if produto:
            raise InputError(
                {"Error": "Produto já Cadastrado", "Recebido": data["modelo"]},
                HTTPStatus.BAD_REQUEST,
            )
        return data

    def valida_patch(self, data: dict):

        check = [has for has in self.campos if has in data]

        if not check:
            print("entrei no raise no check")
            raise InputError(
                {
                    "Erro": "Dados enviados não fazem parte dos campos de Produto",
                    "Enviado": data,
                    "Alternativas": self.campos,
                },
                HTTPStatus.BAD_REQUEST,
            )

        if len(check) > 1:
            raise InputError(
                {
                    "Erro": "Este método PATCH só aceita 1 campo por vez",
                    "Enviado": data,
                },
                HTTPStatus.BAD_REQUEST,
            )

        return check
