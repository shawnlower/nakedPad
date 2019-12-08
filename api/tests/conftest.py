import pytest
from app import create_app
from app.database import db
from app.models import Document


@pytest.fixture(scope='module')
def new_document():
    document = Document(
            text='some text', 
            title='My document title',
    )
    return document

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Fake data
    documents = [
        Document(
            text='It was the best of times, it was the worst of times', 
            title='A Tale of Two Cities',
        ),
        Document(
            text='<html><head /><body><article>Hello</article></body></html>', 
            title='A random HTML page',
        ),
        Document(
            text='<p>A fragment of text', 
            title='A fragment of text',
        ),
        Document(
            text='', 
            title='Doc1',
        ),
    ]
    map(lambda doc: db.session.add(doc), documents)
    db.session.add(documents[0])

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()

