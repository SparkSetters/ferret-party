import os
from flask import Flask
from .routes import test_route
from .routes import auth_test


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(test_route.bp)
    app.register_blueprint(auth_test.auth_test)
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'

    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app
