# Controller for /documents endpoint

from datetime import datetime

from flask import current_app as app
import flask_rebar
import flask_rebar.errors as err
from flask_rebar import get_validated_body
from sqlalchemy.exc import SQLAlchemyError

from app import registry
from app.schemas import (
        DocumentSchema,
        GetDocumentSchema,
        GetDocumentsSchema,
        PutDocumentRequestSchema,
        PostDocumentRequestSchema,
        PostDocumentResponseSchema,
    )
from app.database import db
from app.models import (
       Document
   )
from app.util import normalize_doc_id

@registry.handles(rule='/documents', method='GET', response_body_schema=GetDocumentsSchema())
def get_documents():
    errors = []
    results = []
    try:
        results = Document.query.all()
    except SQLAlchemyError as e:
        app.logger.error(str(e))
        errors.append(
            { 'error_code': 'db_error', 'error_description': 'Unable to access DB' }
        )

    return {
        'count': len(results),
        'results': results,
        'errors': errors, 
    }

@registry.handles(
        rule='/documents/<doc_id>',
        method='GET',
        response_body_schema={
            200: GetDocumentSchema(),
            404: GetDocumentSchema(),
            500: GetDocumentSchema(),
        }
)
def get_document(doc_id):
    errors = []
    document = None
    rc = 200

    try:
        document = Document.query.get(doc_id)
        if not document:
            rc = 404
            errors.append(
                { 'error_code': 'not_found', 'error_description':
                    f'Unable to find document with doc_id={doc_id}' }
            )
    except SQLAlchemyError as e:
        rc = 500
        failed = True
        app.logger.error(str(e))
        errors.append(
            { 'error_code': 'db_error',
                  'error_description': 'Unable to access DB' }
        )

    return {
        'document': document,
        'errors': errors, 
    }, rc


@registry.handles(
        rule='/documents',
        method='POST',
        response_body_schema={
            201: PostDocumentResponseSchema,
            400: PostDocumentResponseSchema},
        request_body_schema=PostDocumentRequestSchema(),
)
def post_documents():
    ###
    # Receive a posted document, and return the document id
    ##

    errors = []
    request = flask_rebar.get_validated_body()
    app.logger.debug(request)
    rc = 201

    # The API will be responsible for generating the document ID
    ## Normalize name. Note: this also commits the record, to avoid a race
    doc_id = normalize_doc_id(request['title'])

    # Create a new doc
    # app.logger.debug(f"Updated doc id {getattr(doc, 'doc_id', '')} -> {doc_id}")
    doc = Document(
            doc_id=doc_id,
            title=request['title'],
            text=request['text']
    )
    db.session.add(doc)
    db.session.commit()

    return {
        'document': doc,
        'errors': errors, 
    }, rc

@registry.handles(
        rule='/documents/<doc_id>',
        method='PUT',
        response_body_schema={
            201: PostDocumentResponseSchema,
            204: PostDocumentResponseSchema,
            404: PostDocumentResponseSchema},
        request_body_schema=PutDocumentRequestSchema(),
)
def put_document(doc_id: str):
    ###
    # Update a document by doc_id
    ##

    errors = []
    request = flask_rebar.get_validated_body()
    app.logger.debug(request)
    rc = 204

    # Get the document from the store by ID
    doc = Document.query.get(doc_id)

    if not doc:
        # Create a new doc
        #raise err.NotFound(f"Document with doc_id {doc_id} was not found")
        app.logger.debug(f'Creating new doc via PUT: {doc_id}')
        doc = Document(
                doc_id = doc_id,
                title = request['title'],
                text = request['text'],
                created = datetime.utcnow()
        )
        db.session.add(doc)
        db.session.commit()
        rc = 201
    else:
        # Update existing
        app.logger.debug(f'Updated existing doc via PUT: {doc_id}')
        doc.title = request['title']
        doc.text = request['text']
        doc.updated = datetime.utcnow()

        db.session.add(doc)
        db.session.commit()

    return {
        'errors': errors, 
    }, rc
