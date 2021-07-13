from flask import Flask


def init_app(app: Flask):
    from .cliente_views import bp as bp_cliente

    app.register_blueprint(bp_cliente)
