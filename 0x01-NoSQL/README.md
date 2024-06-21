# 0x01. NoSQL

## Overview

This project contains scripts and Python functions for interacting with MongoDB using Python and PyMongo. Each script performs specific operations such as listing databases, creating databases, inserting documents, querying documents, updating documents, deleting documents, and performing various statistics on MongoDB collections.

## Files

| File Name             | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| 0-list_databases      | Lists all databases in MongoDB.                                             |
| 1-use_or_create_database | Creates or uses the database `my_db`.                                       |
| 2-insert               | Inserts a document with `name: "Holberton school"` into the `school` collection. |
| 3-all                  | Lists all documents in the `school` collection.                              |
| 4-match                | Lists documents with `name: "Holberton school"` in the `school` collection.  |
| 5-count                | Displays the number of documents in the `school` collection.                 |
| 6-update               | Adds an `address: "972 Mission street"` attribute to documents with `name: "Holberton school"` in the `school` collection. |
| 7-delete               | Deletes all documents with `name: "Holberton school"` from the `school` collection. |
| 8-all.py               | Python script to list all documents in a collection.                         |
| 9-insert_school.py     | Python function to insert a new document in a collection based on kwargs.    |
| 10-update_topics.py    | Python function to change all topics of a school document based on the name. |
| 11-schools_by_topic.py | Python function to return schools having a specific topic.                   |
| 12-log_stats.py        | Python script to provide stats about Nginx logs stored in MongoDB.           |
| 100-find               | Lists all documents with name starting by "Holberton" in the collection `school`. |
| 101-students.py        | Python function to return all students sorted by average score.              |
