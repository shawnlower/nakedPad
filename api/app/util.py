import string
from uuid import uuid4

from flask import current_app as app

from app.models import Document
from app.database import db

def normalize_doc_id(title: str, limit=100) -> str:
    """
    Return a normalized document id, consisting only of
    letters and numbers, as well as - and _

    limit: Maximum number of suffix iterations, e.g. valid_name99
    """

    # Query the existing records to see if a normalized doc_id
    # already exists

    title = title.replace(' ', '_')

    valid_chars = string.ascii_letters + string.digits + '_-'
    valid_base = ''.join([c for c in title if c in valid_chars])

    results = Document.query.filter(Document.doc_id.startswith(valid_base))

    if results.count() == 0:
        # Best case, we can just use the normalized base without a suffix
        return valid_base
    else:
        # Otherwise, iterate through the results to find the next suffix
        values = [ r.doc_id for r in results.all() ]
        i=0
        while i < limit:
            test_id = valid_base + str(i)

            if test_id not in values:
                return test_id

            values.remove(test_id)
            i = i + 1
    return str(uuid4())
