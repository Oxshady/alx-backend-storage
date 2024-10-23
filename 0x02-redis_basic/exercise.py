#!/usr/bin/env python3
"""Initialize the Cache instance with
a Redis client and flush the database."""


from redis import Redis
from typing import Union
from uuid import uuid4


class Cache:
    """Cache class"""

    def __init__(self) -> None:
        """Initialize the Cache instance with a
        Redis client and flush the database"""

        self._redis = Redis(host="127.0.0.1", port=6379)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate key then store data
        using that key and return the key"""

        key = str(uuid4())
        self._redis.set(key, data)
        return key
