#!/usr/bin/env python
#
# Development server runner
#
# Invoke w/ ...
##############################################################################

NAME="nakedpad_api"

import os

from flask import Flask

# Factory method to create our application
def create_app():
    # create and configure the app
    app = Flask(NAME, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
            )

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

