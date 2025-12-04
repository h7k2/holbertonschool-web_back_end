#!/usr/bin/env python3
"""Module providing a function to retrieve schools
that include a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """Return a list of schools that contain the given topic.

    Args:
        mongo_collection: A pymongo collection instance.
        topic (str): The topic to search for.

    Returns:
        A list of school documents matching the topic.
    """
    return list(mongo_collection.find({"topics": topic}))
