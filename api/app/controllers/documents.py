# Controller for /documents endpoint

from flask import current_app as app
import flask_rebar
from sqlalchemy.exc import SQLAlchemyError

from app import registry
from app.schemas import (
        DocumentSchema,
        GetDocumentSchema,
        GetDocumentsSchema,
        PostDocumentRequestSchema,
        PostDocumentResponseSchema,
    )
from app.database import db
from app.models import (
       Document
   )
from app.util import normalize_doc_id

@registry.handles(rule="/documents", method="GET", response_body_schema=GetDocumentsSchema())
def get_documents():
    errors = []
    results = []
    try:
        results = Document.query.all()
    except SQLAlchemyError as e:
        app.logger.error(str(e))
        errors.append(
            { "error_code": "db_error", "error_description": "Unable to access DB" }
        )

    return {
        "count": len(results),
        "results": results,
        "errors": errors, 
    }

@registry.handles(rule="/documents/<doc_id>", method="GET", response_body_schema=GetDocumentSchema())
def get_document(doc_id):
    errors = []
    document = {}

    try:
        document = Document.query.get(doc_id)
    except SQLAlchemyError as e:
        app.logger.error(str(e))
        errors.append(
            { "error_code": "db_error", "error_description": "Unable to access DB" }
        )

    return {
        "document": document,
        "errors": errors, 
    }


@registry.handles(
        rule="/documents",
        method="POST",
        response_body_schema={201: PostDocumentResponseSchema},
        request_body_schema=PostDocumentRequestSchema(),
)
def post_documents():
    ###
    # Receive a posted document, and return the document id
    ##

    errors = []
    body = flask_rebar.get_validated_body()
    rc = 201

    doc = body['document']
    # The API will be responsible for generating the document ID

    ## Normalize name. Note: this also commits the record, to avoid a race
    doc_id = normalize_doc_id(doc)

    if doc.doc_id != doc_id:
        # Create a new doc
        app.logger.debug(f"Updating doc id {doc.doc_id} -> {doc_id}")
        new_doc = Document(title=doc.title, doc_id=doc_id, text=doc.text,
            created=doc.created)
        db.session.add(new_doc)
    else:
        # Use existing
        db.session.add(doc)
        app.logger.debug(f"Not updating doc id {doc.doc_id} -> {doc_id}")

    db.session.commit()

    return {
        "doc_id": doc_id,
        "errors": errors, 
    }, rc
