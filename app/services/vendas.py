from app.models.pivo_carrinho_produto_model import Carrinho_Produto
from app.models.vendas_model import Vendas
from app.services.validator_vendas import ValidatorVendas
from app.services.services import add_commit
from flask import jsonify
from app.exc import InputError


def alterar_venda(venda_id, email, action):
    try:
        lojista = ValidatorVendas.check_lojista(email)
        venda = Vendas.query.filter_by(id=venda_id).first()
        ValidatorVendas.check_venda(venda, lojista.id, action)

        if action == "aprovar":
            status_id = 3
        elif action == "despachar":
            status_id = 4
        elif action == "cancelar":
            status_id = 5

        venda.status_id = status_id

        add_commit(venda)
        return jsonify(venda.serialized)
    except InputError as err:
        return err.args

    except AttributeError as err:
        return err.args


def ver_venda(venda_id, email, action):
    try:
        lojista = ValidatorVendas.check_lojista(email)
        venda = Vendas.query.filter_by(id=venda_id).first()
        ValidatorVendas.check_venda(venda, lojista.id, action)
        venda = Vendas.query.filter_by(id=venda_id).first()
        return jsonify(venda.serialized)
    except InputError as err:
        return err.args

    except AttributeError as err:
        return err.args

def ver_vendas(email):
    try:
        lojista = ValidatorVendas.check_lojista(email)
        vendas = Vendas.query.filter_by(lojista_id=lojista.id).all()
        data = []
        for item in vendas:
            data.append(item.serialized)
        return jsonify(data)
    except InputError as err:
        return err.args

    except AttributeError as err:
        return err.args