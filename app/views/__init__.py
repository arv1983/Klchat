from flask import Flask


def init_app(app: Flask):
    from .signup_views import bp as bp_signup
    from .perfil_cliente import bp as bp_perfil
    from .login_views import bp as bp_login
    from .carrinho_views import bp as bp_carrinho 
    from .produtos_views import bp as bp_product
    from .gerar_vendas_views import bp as bp_gerar_vendas
    from .home_view import bp as bp_home
    from .vendas_andamento_views import bp as bp_venda_andamento
    app.register_blueprint(bp_product)
    app.register_blueprint(bp_signup)
    app.register_blueprint(bp_login)
    app.register_blueprint(bp_perfil)
    app.register_blueprint(bp_carrinho)
    app.register_blueprint(bp_gerar_vendas)
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_venda_andamento)

