"""
function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection based on kwargs"""
    status = mongo_collection.insert_one(kwargs)
    if status.acknowledged:
        return status.inserted_id
