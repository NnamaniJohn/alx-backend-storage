#!/usr/bin/env python3
"""
update topic
"""


def update_topics(mongo_collection, name, topics):
    """
    update topic
    :param mongo_collection:
    :param name:
    :param topics:
    :return:
    """
    return mongo_collection.update_one({"name": name},
                        {"$set": {"topics": topics}}, upsert=True)
