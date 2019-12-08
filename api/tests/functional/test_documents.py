"""
This file tests the /documents endpoint
"""

def test_valid_post_succeeds(test_client):
    """
    GIVEN a Flask application
    WHEN POSTing a valid request to the /documents endpoint
    THEN it should return a valid response
    """

    request = { 'document': {
        'title': 'A Tale of Two Cities',
        'text': 'It was the best of times, it was the worst of times'
    } }

    print(test_client.__doc__)
    # response = test_client.post('/api/v1/documents', content_type='application/json')
    response = test_client.post('/api/v1/documents', json=request)
    print(response.json)
    assert response.status_code == 201
    assert response.json['title'] == request['title']
    assert response.json['text'] == request['text']

def test_get_all_succeeds(test_client):
    """
    GIVEN a Flask application
    WHEN the /documents endpoint is requested (GET)
    THEN it should return four valid documents
    """
    
    response = test_client.get('/api/v1/documents')
    assert response.status_code == 200
    assert len(response.json['results']) == 0
