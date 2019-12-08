"""
This file (test_models.py) contains the unit tests for the models.py file.
"""


def test_new_document(new_document):
    """
    GIVEN a Document model
    WHEN a new Document is created
    THEN check the title, created, doc_id, text are set correctly
    """
    assert new_document.text == "some text"
    assert new_document.title == "My document title"
