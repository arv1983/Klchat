from flask import Flask


def init_app(app: Flask):
    from .signup_views import bp as bp_signup
    from .perfil_cliente import bp as bp_perfil
    from .login_views import bp as bp_login
    from .carrinho_views import bp as bp_carrinho
    from .produtos_views import bp as bp_product
    from .home_view import bp as bp_home
    from .vendas_views import bp as bp_vendas
    from .compras_views import bp as bp_compras
    from .categorias_views import bp as bp_categorias

    app.register_blueprint(bp_product)
    app.register_blueprint(bp_signup)
    app.register_blueprint(bp_login)
    app.register_blueprint(bp_perfil)
    app.register_blueprint(bp_carrinho)
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_vendas)
    app.register_blueprint(bp_compras)
    app.register_blueprint(bp_categorias)
