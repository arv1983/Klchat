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
    cli_lojista = AppGroup("lojista")
    cli_categoria = AppGroup("categoria")
    cli_status = AppGroup("status")
    cli_produto = AppGroup("produto")
    fake = Faker()

    @cli_cliente.command("list_clientes")
    def cli_get_clients():
        """
        List clients in db
        """
        click.echo("consulting db to get clientes...\n")

        result = Clientes.query.all()

        if not result:
            click.echo("Table Clientes is empty!")

        for cliente in result:
            click.echo(
                f"id: {cliente.id}, nome: {cliente.nome}, email: {cliente.email}"
            )

        print()

    @cli_lojista.command("list_lojistas")
    def cli_get_logistas():
        """
        List lojistas in db
        """
        click.echo("consulting db to get lojistas...\n")

        result = Lojistas.query.all()

        if not result:
            click.echo("Table lojistas is empty!")

        for lojistas in result:
            click.echo(
                f"id: {lojistas.id}, nome: {lojistas.nome}, email: {lojistas.email}"
            )
        print()

    @cli_categoria.command("list_categorias")
    def cli_get_categories():
        """
        List categoria in db
        """
        click.echo("consulting db to get categoria...\n")
        result = Categorias.query.all()

        if not result:
            click.echo("Table Clientes is empty!")

        for categoria in result:
            click.echo(f"id: {categoria.id}, descricao: {categoria.descricao}")

        print()

    @cli_status.command("list_status")
    def cli_get_status():
        """
        List status in db
        """
        click.echo("consulting db to get status...\n")
        result = Status.query.all()

        if not result:
            click.echo("Table status is empty!")

        for status in result:
            click.echo(f"id: {status.id}, situacao: {status.situacao}")

        print()

    @cli_produto.command("list_produtos")
    def cli_get_status():
        """
        List produto in db
        """
        click.echo("consulting db to get produto...\n")
        result = Produtos.query.all()

        if not result:
            click.echo("Table produto is empty!")

        produto: Produtos = []
        for produto in result:
            click.echo(f"{produto}")

        print()

    app.cli.add_command(cli_cliente)
    app.cli.add_command(cli_lojista)
    app.cli.add_command(cli_categoria)
    app.cli.add_command(cli_status)
    app.cli.add_command(cli_produto)


def init_app(app: Flask):
    cli_heroku(app)
