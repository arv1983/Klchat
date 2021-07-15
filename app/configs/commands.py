from flask import Flask, current_app
from flask.cli import AppGroup
from faker import Faker
from werkzeug.security import generate_password_hash
import click

from app.models.clientes_model import Clientes
from app.models.lojistas_model import Lojistas
from app.models.endereco_model import Endereco
from app.models.categorias_model import Categorias
from app.models.produtos_model import Produtos
from app.models.carrinho_model import Carrinho
from app.models.pivo_carrinho_produto_model import Carrinho_Produto
from app.models.vendas_model import Vendas
from app.models.status_model import Status


def cli_heroku(app: Flask):

    cli_cliente = AppGroup("cliente")
    fake = Faker()

    @cli_cliente.command("delete_all_clientes")
    def cli_delete_clientes():
        click.echo("Deleting all clientes, please wait ...")
        session = current_app.db.session

        try:
            session.query(Clientes).delete()
            session.commit()
        except:
            session.rollback()
            return click.echo("oops something wrong when trying to delete clientes")

        return click.echo("All users have been deleted")

    @cli_cliente.command("list_clientes")
    def cli_get_users():
        click.echo("consulting db to get clientes...")
        session = current_app.db.session

        result = Clientes.query.all()
        session.commit()

        if not result:
            click.echo("Table Clientes is empty!")

        for user in result:
            click.echo(f"id: {user.id}, login: {user.login}, admin: {user.is_admin}")

    @cli_cliente.command("create")
    @click.argument("qty")
    @click.argument("is_admin")
    def cli_create_n_clientes(qty: str, is_admin: bool):

        qty = int(qty)
        is_admin = True if int(is_admin) == 1 else False

        session = current_app.db.session
        if qty < 1:
            return click.echo(
                {
                    "Error": "Required at least qty >= 1 in argument, example: flask user create 1"
                }
            )

        click.echo("Creating users, please wait.")

        for i in range(qty):
            data = create_faker_user()
            data["is_admin"] = is_admin
            try:
                user: Clientes = Clientes(**data)
                session.add(user)
                session.commit()
                click.echo(
                    f"login: {user.login}, email: {user.email}, admin: {user.is_admin}"
                )

            except:
                click.echo(f"ops, algo deu errado qto tenta gravar {user}")

    # services
    def create_faker_user() -> dict:
        login = fake.name()
        email = fake.email()

        password_hash = generate_password_hash(fake.password(length=10))
        return dict(login=login, email=email, password_hash=password_hash)

    app.cli.add_command(cli_cliente)


def init_app(app: Flask):
    cli_heroku(app)
