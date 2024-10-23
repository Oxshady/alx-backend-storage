#!/usr/bin/env python3
"""
Initialize the Cache instance with
a Redis client and flush the database.
"""


import redis
import uuid
from typing import Union


class Cache:
    """
    methods to handle redis cache operations
    """
    def __init__(self) -> None:
        """
        Initialize redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in redis cache
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
