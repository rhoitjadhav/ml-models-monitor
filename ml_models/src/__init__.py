# Packages
from flask import Flask

# Modules
from src.routes import routes


def create_app(config_file='config.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    
    # Blueprints
    app.register_blueprint(routes.bp)

    # Index page
    @app.route('/')
    def index():
        return 'ML-Models'

    return app
