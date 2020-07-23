import os

from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
import logging
from logging.config import dictConfig

from apps.matcher_text.blueprint import text 
from apps.matcher_scraper.blueprint import scraper  
from apps.utils.model.error import ProcessException

def configure_logging():
    # register root logging
    logging.basicConfig(filename='logging.log',level=logging.DEBUG)
    logging.getLogger('werkzeug').setLevel(logging.INFO)

def create_app(test_config=None):
    # setup logger
    configure_logging()

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # registering blueprint
    app.register_blueprint(text)
    app.register_blueprint(scraper)

    # use it on development
    @app.errorhandler(ProcessException)
    def handle_exception(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code 
        return response

    # use it on production
    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Return JSON instead of HTML for HTTP errors."""
        # start with the correct headers and status code from the error
        response = e.get_response()
        # replace the body with JSON
        response.data = jsonify({
            "code": e.code,
            "name": e.name,
            "description": e.description,
            })
        response.content_type = "application/json"
        return response

    # checking connection
    @app.route('/')
    def hello():
        return 'Welcome! Key Matcher Backend Service'
    return app