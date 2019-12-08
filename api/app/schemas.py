from marshmallow import fields, Schema
from marshmallow.validate import ContainsOnly

from marshmallow_sqlalchemy import ModelSchema

from app import models
from app.database import db

####
# Common fields
# https://marshmallow.readthedocs.io/en/stable/api_reference.html
###
# Number
# Integer
# List
# String
# Tuple
# Set
# UUID
# Decimal
# Boolean
# Float
# DateTime
####

class HealthSchema(Schema):
    status = fields.Str(
            validate = ContainsOnly(
                choices=["ok", "error"]
            ),
    )


class DocumentSchema(ModelSchema):
    class Meta:
        model = models.Document
        sqla_session = db.session


class ErrorSchema(Schema):
    # Example: db_error
    error_code = fields.String()
    error_description = fields.String()


class GetDocumentSchema(Schema):
    document = fields.Nested(DocumentSchema(), many=False)
    errors = fields.Nested(ErrorSchema(), many=True)


class GetDocumentsSchema(Schema):
    count = fields.Integer()
    results = fields.Nested(DocumentSchema(), many=True)
    errors = fields.Nested(ErrorSchema(), many=True)


class PostDocumentRequestSchema(Schema):
    title = fields.Str()
    text = fields.Str()


class PostDocumentResponseSchema(Schema):
    doc_id = fields.String()
    errors = fields.Nested(ErrorSchema(), many=True)


