import logging as logger
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .app import main
    app.register_blueprint(main)
    
    logger.debug("App registered")
    return app
