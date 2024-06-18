#!/usr/bin/env python3
""" task 14 """
from pymongo import MongoClient


def top_students(mongo_collection):
    """ returns all students sorted by average score """
    pipeline = [
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': {
                    '$avg': '$topics.score'
                },
                'topics': 1
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
