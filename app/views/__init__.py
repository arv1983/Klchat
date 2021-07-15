from flask import Flask


def init_app(app: Flask):
    from .signup_views import bp as bp_signup
    from .perfil_cliente import bp as bp_perfil
    from .login_views import bp as bp_login    
    app.register_blueprint(bp_signup)
    app.register_blueprint(bp_login)
    app.register_blueprint(bp_perfil)

