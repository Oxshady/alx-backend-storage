from pymongo.collection import Collection
from pymongo.cursor import Cursor
from typing import Union, List, Dict
"""
lists all documents in a collection
"""


def list_all(mongo_collection: Collection) -> Union[Cursor[Dict], List]:
    """function that lists all documents in a collection"""
    documents = mongo_collection.find()
    if documents:
        return documents
    else:
        return []
