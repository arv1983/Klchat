from flask import Flask


def init_app(app: Flask):
    from .signup_views import bp as bp_signup
    from .perfil_cliente import bp as bp_perfil
    from .login_views import bp as bp_login    
    app.register_blueprint(bp_signup)
   
    from .login_views import bp as bp_login
    app.register_blueprint(bp_login)
    
    from .produtos_views import bp as bp_product
    app.register_blueprint(bp_product)
