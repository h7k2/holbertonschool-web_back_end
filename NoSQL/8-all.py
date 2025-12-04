#!/usr/bin/env python3
"""Module providing a function to retrieve every document
from a MongoDB collection.
"""


def list_all(mongo_collection):
    """Return all documents stored in the given collection.

    Args:
        mongo_collection: A pymongo collection instance.

    Returns:
        A list containing all documents in the collection.
        If the collection is empty, an empty list is returned.
    """
    return list(mongo_collection.find())
