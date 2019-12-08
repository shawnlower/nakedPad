#!/usr/bin/env python
#
# Development server runner
#
# Invoke w/: FLASK_ENV=development flask run
##############################################################################

NAME="nakedpad_api"

import os

from flask import Flask
#from flask_marshmallow import Marshmallow
from flask_rebar import Rebar

# Need to setup rebar before importing decorated routes
rebar = Rebar()

# All handler URL rules will be prefixed by '/v1'
registry = rebar.create_handler_registry(prefix='/api/v1')

# Import controllers for flask_rebar
from .controllers import (
        documents,
        health,
    )

# Import database
from . import database

# Factory method to create our application
def create_app(config_file=None):
    # create and configure the app

    app = Flask(NAME, instance_relative_config=True)
    if config_file:
        app.logger.warning("Using config file: " + config_file)
        app.config.from_pyfile(config_file)
    elif os.path.exists(os.path.join(app.instance_path, "config.py")):
        app.logger.warning("Using instance config.")
        app.config.from_pyfile('config.py')
    else:
        raise Exception("No config file found in instance dir")


    rebar.init_app(app)

    # Perform DB setup
    database.db.init_app(app)
    #Marshmallow(app)
    with app.app_context():
        database.db.create_all()

    return app
