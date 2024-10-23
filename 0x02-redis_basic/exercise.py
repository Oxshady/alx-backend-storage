#!/usr/bin/env python3
"""Initialize the Cache instance with
a Redis client and flush the database."""


from redis import Redis
from uuid import uuid4
from typing import Union


class Cache:
    """Cache class"""

    def __init__(self) -> None:
        """Initialize the Cache instance with a
        Redis client and flush the database"""

        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:

        """generate key then store data
        using that key and return the key"""
        uuid = str(uuid4())
        self._redis.set(name=uuid, value=data)
        return uuid
