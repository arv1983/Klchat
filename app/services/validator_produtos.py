from app.models.produtos_model import Produtos
from app.exc import InputError
from http import HTTPStatus

class ValidatorProdutos:
    
    campos = ["descricao", "marca", "fabricante", "qut_estoque","valor_unitario", "lojista_id", "categoria_id"]

    def produto(self, data: dict):

        if not data:
            raise InputError(
                {
                    "Error":"request sem dados",
                    "Obrigatórios":self.campos
                },HTTPStatus.BAD_REQUEST
            )
        
        produto = Produtos.query.filter_by(modelo=data.get("modelo")).first()
        
        if produto:
            raise InputError(
                {
                    "Error": "Produto já Cadastrado",
                    "Recebido": {data.get("modelo")}
                },HTTPStatus.BAD_REQUEST,
            )
            