import os

from flask import Flask

from apps.matcher_text.text import text 
from apps.matcher_scraper.scraper import scraper  

def create_app(test_config=None):
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

    # checking connection
    @app.route('/')
    def hello():
        return 'Welcome! Testing page'

    return app