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
