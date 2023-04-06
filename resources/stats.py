from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

import requests

blp = Blueprint("stats", __name__, description="Operations on invoices")

@blp.route('/stats')
class Stats(MethodView):
    def get(self):
        try:
            return requests.get("https://api.blockchain.info/stats").json()
        except SQLAlchemyError:
            return abort(500, message= "Error retrieving Blockchain API Stats")