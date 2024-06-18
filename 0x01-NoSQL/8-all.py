#!/usr/bin/env python3
""" task8 """


def list_all(mongo_collection):
    """ lists all documents in a collection or an empty list """
    return list(mongo_collection.find())
