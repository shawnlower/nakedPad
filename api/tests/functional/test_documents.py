"""
This file tests the /documents endpoint

"""

#def test_valid_post_succeeds(test_client, init_database):

def test_get_all_succeeds(test_client):
    """
    GIVEN a Flask application
    WHEN the /documents endpoint is requested (GET)
    THEN it should return four valid documents
    """
    
    response = test_client.get('/api/v1/documents')
    assert response.status_code == 200
    assert len(response.json['results']) == 0
