#!/usr/bin/env python3
""" task9 """


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs
        and returns its id """
    return mongo_collection.insert_one(kwargs).inserted_id
