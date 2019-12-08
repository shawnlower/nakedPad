from marshmallow import fields, Schema
from marshmallow.validate import ContainsOnly
from flask_rebar.validation import DisallowExtraFieldsMixin

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


# Disabling the use of the ModelSchema as it limits the validation we can
# perform on fields, e.g.: title is set to nullable=False on the model
# but does not imply missing=False
#
#class DocumentSchema(ModelSchema):
#    class Meta:
#        model = models.Document
#        sqla_session = db.session

class DocumentSchema(Schema):
    doc_id = fields.String(missing=False)
    title = fields.String(missing=False)
    text = fields.Str(missing=False)
    created = fields.DateTime(missing=False)


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


class PostDocumentRequestSchema(Schema, DisallowExtraFieldsMixin):
    title = fields.Str(missing=False)
    text = fields.Str(missing=False)


class PostDocumentResponseSchema(Schema):
    document = fields.Nested(DocumentSchema())
    errors = fields.Nested(ErrorSchema(), many=True)


