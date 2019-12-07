#!/usr/bin/env python
#
# Development server runner
#
# Invoke w/: FLASK_ENV=development flask run
##############################################################################

NAME="nakedpad_api"

import os

from flask import Flask
from flask_rebar import Rebar

# Need to setup rebar before importing decorated routes
rebar = Rebar()

# All handler URL rules will be prefixed by '/v1'
registry = rebar.create_handler_registry(prefix='/api/v1')

# Import controllers for flask_rebar
from .controllers import health


# Factory method to create our application
def create_app():
    # create and configure the app
    app = Flask(NAME, instance_relative_config=True)
    if os.path.exists(os.path.join(app.instance_path, "config.py")):
        app.config.from_pyfile('config.py')
    else:
        app.config.from_mapping(
                SECRET_KEY='dev',
                DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
                )

    rebar.init_app(app)
    return app

