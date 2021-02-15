# Packages
from flask import Flask

# Modules
from src.routes import routes


def create_app(config_file: str = 'config.py') -> object:
    """Create instance of Flask and registers blueprints
    Args:
        config_file: path of configuration file
    
    Returns:
        object: Flask instance
    """

    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    # Blueprints
    app.register_blueprint(routes.bp)

    # Index page
    @app.route('/')
    def index():
        return 'ML-Monitor'

    return app
