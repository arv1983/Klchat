from flask import Flask


def init_app(app: Flask):
    from .signup_views import bp as bp_signup
    from .perfil_cliente import bp as bp_perfil
    from .login_views import bp as bp_login
    from .carrinho_views import bp as bp_carrinho    
    app.register_blueprint(bp_signup)
   
    from .login_views import bp as bp_login
    app.register_blueprint(bp_login)
    app.register_blueprint(bp_perfil)
    app.register_blueprint(bp_carrinho)

