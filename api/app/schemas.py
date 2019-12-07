from marshmallow import fields, Schema
from marshmallow.validate import ContainsOnly

class HealthSchema(Schema):
    status = fields.Str(
            validate = ContainsOnly(
                choices=["ok", "error"]
            )
    )

