#!/usr/bin/env python3
"""
insert
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert school
    :param mongo_collection:
    :param kwargs:
    :return:
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
