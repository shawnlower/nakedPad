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
    status = fields.String(
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
    text = fields.String(missing=False)
    created = fields.DateTime(missing=False)
    updated = fields.DateTime(missing=False)


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
    title = fields.String(missing=False)
    text = fields.String(missing=False)


class PostDocumentResponseSchema(Schema):
    document = fields.Nested(DocumentSchema())
    errors = fields.Nested(ErrorSchema(), many=True)


class PutDocumentRequestSchema(Schema, DisallowExtraFieldsMixin):
    """
    An HTTP PUT of a document may or may not include the doc_id
    There are several use cases, which should all be idempotent:
    1) PUT /documents
        Create a new resource and return 'HTTP 201 Created' with a 'Content-Location'
        header specifying the new location: /documents/<doc_id>
    2) PUT /documents/<doc_id>
        Update a specific document and return 'HTTP 204 No content' with a
        'Content-Location' header specifying the existing location
    """
    doc_id = fields.String()
    title = fields.String(missing=False)
    text = fields.String(missing=False)
