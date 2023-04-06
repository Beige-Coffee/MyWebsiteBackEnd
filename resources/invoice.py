import json
import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from models import LightningTipsModel
from utils import create_lnbits_invoice
from config import LNBITS_API_KEY, LNBITS_URL
from schemas import InvoiceCreateSchema
from db import payments, db

blp = Blueprint("invoice", __name__, description="Operations on invoices")

@blp.route('/invoice/<string:invoice_id>')
class Invoice(MethodView):
    def get(self, invoice_id):
        try:
            return payments[invoice_id]
        except KeyError:
            return abort(404, message= "invoice not found")

@blp.route('/invoice')
class InvoiceList(MethodView):
    def get(self):
        return {"invoices": list(payments.values())}

    @blp.arguments(InvoiceCreateSchema)
    def post(self, request_data):
        amount = request_data['amount']
        memo = request_data['memo']

        lnbits_invoice = create_lnbits_invoice(amount, memo, LNBITS_URL, LNBITS_API_KEY)

        payment_hash = lnbits_invoice["payment_hash"]
        payment_request = lnbits_invoice["payment_request"]

        save_invoice(payment_hash, payment_request, memo, amount)

        response = {'hash': payment_hash, 'request': payment_request}

        return json.dumps(response), 200


def save_invoice(payment_hash, payment_request, memo, amount):
    tip_id = uuid.uuid4().hex
    tip = {
        'id': tip_id,
        'payment_hash' : payment_hash,
        "payment_request" : payment_request,
        "memo" : memo,
        "amount" : amount
    }
    payments[tip_id] = (tip)

    tip = LightningTipsModel(
        payment_hash = payment_hash,
        payment_request = payment_request,
        memo = memo,
        amount = amount,
        paid_at = None
        )
    try:
        db.session.add(tip)
        db.session.commit()
    except SQLAlchemyError:
        abort(500, message="An error occurred while inserting a tip in to the database.")



