#!/usr/bin/env python3
"""Module providing a function to update the topics field
of school documents in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """Update the topics list of all school documents matching the name.

    Args:
        mongo_collection: A pymongo collection instance.
        name (str): The name of the school to update.
        topics (list): The new list of topics for the school.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
