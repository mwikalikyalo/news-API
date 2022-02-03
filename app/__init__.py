from flask import Flask

from config import config_options
from .main import main as main_blueprint
from .request import configure_request

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # register blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    
    configure_request(app)
    
    return app
    