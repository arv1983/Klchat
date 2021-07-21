from flask import json
import pytest
import ipdb

from app import create_app
from app.services.gerator_data import GeratorData
from app.services.regex import ValidatorRegex


@pytest.fixture
def signup():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_signup_cliente_cpf(signup):

    """
    Teste Create Cliente PF
    """

    ger = GeratorData()
    val = ValidatorRegex()
    data = ger.create_client_cpf()
    url = "/signup"

    response = signup.post(url, json=data)

    res = response.get_json()

    data["cpf"] = val.cpf(data.get("cpf"))
    data["telefone"] = val.telefone(data.get("telefone"))

    except_dict = {
        "id": res.get("id"),
        "nome": data.get("nome"),
        "email": data.get("email"),
        "cpf": data.get("cpf"),
        "cnpj": None,
        "telefone": data.get("telefone"),
        "endereco_id": None,
    }
    assert type(response.get_json()) == dict
    assert response.get_json() == except_dict
    assert response.status_code == 201


def test_signup_cliente_cnpj(signup):
    """
    Teste Create Cliente PJ
    """
    ger = GeratorData()
    val = ValidatorRegex()
    data = ger.create_client_cnpj()
    url = "/signup"

    response = signup.post(url, json=data)

    res = response.get_json()

    data["cnpj"] = val.cnpj(data.get("cnpj"))

    data["telefone"] = val.telefone(data.get("telefone"))

    except_dict = {
        "id": res.get("id"),
        "nome": data.get("nome"),
        "email": data.get("email"),
        "cnpj": data.get("cnpj"),
        "cpf": None,
        "telefone": data.get("telefone"),
        "endereco_id": None,
    }
    assert type(response.get_json()) == dict
    assert response.get_json() == except_dict
    assert response.status_code == 201


def test_signup_lojista(signup):
    """
    Teste create Lojista
    """
    ger = GeratorData()
    val = ValidatorRegex()
    data = ger.create_client_cnpj()
    url = "/signup"

    response = signup.post(url, json=data)

    res = response.get_json()

    data["cnpj"] = val.cnpj(data.get("cnpj"))

    data["telefone"] = val.telefone(data.get("telefone"))

    except_dict = {
        "id": res.get("id"),
        "nome": data.get("nome"),
        "email": data.get("email"),
        "cnpj": data.get("cnpj"),
        "cpf": None,
        "telefone": data.get("telefone"),
        "endereco_id": None,
    }
    assert type(response.get_json()) == dict
    assert response.get_json() == except_dict
    assert response.status_code == 201


def test_signup_dados_faltantes(signup):
    """
    Teste Cliente - dados faltantes
    """
    data = dict(tipo_usuario="cliente")

    url = "/signup"
    response = signup.post(url, json=data)

    except_dict = {
        "Error": "Faltam campos obrigatórios",
        "recebido": ["tipo_usuario"],
        "faltantes": {
            "Campos": ["nome", "email", "senha", "telefone"],
            "pessoa Física": "cpf",
            "pessoa Jurídica": "cnpj",
        },
    }

    assert type(response.get_json()) == dict
    assert response.get_json() == except_dict
    assert response.status_code == 400
