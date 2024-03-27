#!/usr/bin/env python3
"""
schools by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    schools by topic
    :param mongo_collection:
    :param topic:
    :return:
    """
    mongo_collection.find({'topics': topic})
