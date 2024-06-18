#!/usr/bin/env python3
"""
    script that provides some stats about Nginx logs stored in MongoDB:

    - Database: logs
    - Collection: nginx
    - Display:
        - first line: x logs where x is the number of documents in this
          collection
        - second line: Methods:
        - 5 lines with the number of documents with the method = ["GET",
          "POST", "PUT", "PATCH", "DELETE"] in this orde
        - one line with the number of documents with:
            - method=GET
            - path=/status
"""
from pymongo import MongoClient


def log_stats():
    """ log_stats function """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    print(f"{nginx.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {nginx.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {nginx.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {nginx.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {nginx.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {nginx.count_documents({'method': 'DELETE'})}")
    print(f"{nginx.count_documents({'method': 'GET', 'path': '/status'})} "
          "status check")


if __name__ == "__main__":
    log_stats()
