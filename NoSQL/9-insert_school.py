#!/usr/bin/env python3
"""Module containing a helper to insert a document
into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document into the specified collection.

    Args:
        mongo_collection: A pymongo collection instance.
        **kwargs: Fields and values of the document to insert.

    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
