from marshmallow import Schema, fields

class InvoiceCreateSchema(Schema):
    amount = fields.Int(required=True)
    memo = fields.Str(required=False)
