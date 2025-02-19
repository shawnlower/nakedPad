"""
This file tests the /documents endpoint
"""

def test_valid_post_succeeds(test_client):
    """
    GIVEN a Flask application
    WHEN POSTing a valid request to the /documents endpoint
    THEN it should return a valid response
    """

    request = {
        'title': 'A Tale of Two Cities',
        'text': 'It was the best of times, it was the worst of times'
    }

    response = test_client.post('/api/v1/documents', json=request)

    # Valid 201: created response
    assert response.status_code == 201

    # No errors were returned
    doc = response.json['document']
    assert not doc.get('errors')

    # All keys in our request match the response
    for key in request:
        assert doc.get(key) == request.get(key)

    # Creation date and doc_id were generated correctly
    assert doc.get('created')
    assert doc.get('doc_id')

def test_bad_posts(test_client):
    """
    GIVEN a Flask application
    WHEN POSTing invalid requests
    THEN it should return a '400 Bad Request' response with an error payload
    """
    requests = [
        # With empty data
        {},
        # Invalid keys
        { 'cats': 'are lazy', 'title': 'test2' },
        # More invalid keys
        { 'title': 'test3', 'text': 'foo', 'doc_id': 'should not be provided' },
        # Missing title key
        { 'title': '', 'text': 'test4'} ,
        # Bad data type
        { 'title': 'test5', 'text': None }
    ]
    responses = map(
            lambda req: test_client.post('/api/v1/documents', json=req),
            requests
    )
    for resp in responses:
        if resp.status_code != 400:
            assert resp.json and False


def test_get_after_post(test_client):
    """
    GIVEN a Flask application
    WHEN POSTing a valid request to the /documents endpoint
    THEN GETing the document by id, it should be returned
    """

    request = { 'title': 'First title', 'text': 'some text' }
    response = test_client.post('/api/v1/documents', json=request)
    assert(response.status_code == 201)
    doc_id = response.json['document']['doc_id']
    assert(doc_id)

    response = test_client.get(f'/api/v1/documents/{doc_id}')
    doc = response.json.get('document')

    # All keys exist
    for key in request:
        assert doc.get(key) == request.get(key)
    assert doc.get('created')
    assert doc.get('doc_id')


def test_get_all_succeeds(test_client):
    """
    GIVEN a Flask application
    WHEN the /documents endpoint is requested (GET)
    THEN it should return four valid documents
    """
    
    response = test_client.get('/api/v1/documents')
    assert response.status_code == 200


def test_update_document(test_client):
    """
    GIVEN a Flask application
    WHEN making a PUT request after a successful POST
    THEN it should return a successful status code and
    THEN a subsequent GET should return the new document
    """
    request = {
        'title': 'A Tale of Two Cities',
        'text': 'It was the best of times, it was the worst of times'
    }

    response = test_client.post('/api/v1/documents', json=request)

    # Valid 201: created response
    assert response.status_code == 201

    # No errors were returned
    doc = response.json['document']
    assert not doc.get('errors')

    doc_id = doc['doc_id']
    orig_updated = doc['updated']

    request = {
        'title': 'A Tale of One City',
        'text': 'It was the aight'
    }

    response = test_client.put(f'/api/v1/documents/{doc_id}', json=request)

    # Valid 204: Not Modified response
    assert response.status_code == 204

    # Finally GET our doc
    response = test_client.get(f'/api/v1/documents/{doc_id}')
    doc = response.json['document']

    assert response.status_code == 200

    # All keys in our request match the response
    for key in request:
        assert doc.get(key) == request.get(key)

    # Creation date should be updated
    assert doc.get('updated') != orig_updated


def test_delete_document(test_client):
    """
    GIVEN a Flask application
    WHEN making a DELETE request
    THEN it should return a successful status code and
    THEN a subsequent GET should NOT return the document
    """
    request = {
        'title': 'A Tale of Two Cities',
        'text': 'It was the best of times.  It was the worst of times.'
    }

    response = test_client.post('/api/v1/documents', json=request)
    doc_id = response.json['document']['doc_id']
    response = test_client.get(f'/api/v1/documents/{doc_id}')
    assert response.status_code == 200

    response = test_client.delete(f'/api/v1/documents/{doc_id}')
    assert response.status_code == 204

    response = test_client.get(f'/api/v1/documents/{doc_id}')
    assert response.status_code == 404
