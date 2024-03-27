#!/usr/bin/env python3
"""
show all databases
"""


def list_all(mongo_collection):
    """
    list all
    :param mongo_collection:
    :return:
    """
    return mongo_collection.find()
