import os
from flask import Flask, request, g
from . import google_auth
from . import fdi

# Common configuration code
def create_app(test_config = None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Get stuff from environment
    app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)

    # Register blueprints
    app.register_blueprint(google_auth.app)
    app.register_blueprint(fdi.bp)

    # Configure database
    app.config['DATABASE'] = os.path.join(app.instance_path, 'adnifdi.sqlite')

    # Return the app
    return app
