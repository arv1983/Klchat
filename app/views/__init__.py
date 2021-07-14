from flask import Flask


def init_app(app: Flask):

    from app.views.signup_views import bp_signup
    app.register_blueprint(bp_signup)

    from app.views.login_views import bp_login
    app.register_blueprint(bp_login)
