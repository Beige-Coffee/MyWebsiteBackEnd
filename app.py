from flask import Flask
from flask_smorest import abort, Api

import os
from db import db

from resources.invoice import blp as InvoiceBluePrint
from resources.stats import blp as StatsBluePrint
#from config import DB_URI
import models

def create_app(db_url=None):
    app = Flask(__name__)

    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['API_TITLE'] = "MyWebsiteBackend"
    app.config['API_VERSION'] = "v1"
    app.config['OPENAPI_VERSION'] = "3.0.3"
    app.config['OPENAPI_URL_PREFIX'] = "/"
    app.config['OPENAPI_SWAGGER_UI_PATH'] = "/swagger-ui"
    app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    #app.config['SQLALCHEMY_DATABASE_URI'] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    api = Api(app)

    @app.before_first_request
    def create_tables():
        # create tables if the table do not already exist
        db.create_all()

    api.register_blueprint(InvoiceBluePrint)
    api.register_blueprint(StatsBluePrint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8000)