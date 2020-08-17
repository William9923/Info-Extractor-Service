import os

from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import BadRequest
import logging

from apps.matcher_text.blueprint import text 
from apps.matcher_scraper.blueprint import scraper  
from apps.utils.model.error import ProcessException

def configure_logging():
    # register root logging
    logging.basicConfig(filename='logging.log',level=logging.DEBUG)
    logging.getLogger('werkzeug').setLevel(logging.DEBUG)
    

def create_app(test_config=None):
    # setup logger
    configure_logging()

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

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

    @app.errorhandler(BadRequest)
    def handle_bad_request(e):
        return jsonify({
            "message" : "Bad Request!",
            "code" : 400
        })

    # checking connection
    @app.route('/')
    def hello():
        return 'Welcome! Key Matcher Backend Service. Please check the <a href="https://info-extractor-docs.netlify.app/">documentation</a> for more info!'
    return app