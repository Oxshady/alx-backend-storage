#!/usr/bin/env python3
"""
This module provides a Cache class that interacts with a Redis database.
It allows storing data in Redis and retrieving it with
optional type conversions.
The Redis database is flushed upon initialization of the Cache instance.
"""

import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(fn: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    Increments a Redis key that corresponds to the method's qualified name.

    Args:
        fn (Callable): The method to be decorated.

    Returns:
        Callable: The wrapped method that increments the call count.
    """

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        key = fn.__qualname__
        self._redis.incr(key)
        return fn(self, *args, **kwargs)

    return wrapper


class Cache:
    """
    A class to handle basic operations with a Redis cache.

    Methods:
        store(data: Union[str, bytes, int, float]) -> str:
            Stores data in the Redis cache and returns a unique key.

        get(key: str, fn: Optional[Callable] = None) ->
        Union[str, bytes, int, float, None]:
            Retrieves data from the Redis cache using the provided key.
            Optionally applies a conversion function to the data.

        get_str(key: str) -> Optional[str]:
            Retrieves the data as a UTF-8 decoded string.

        get_int(key: str) -> Optional[int]:
            Retrieves the data as an integer.
    """

    def __init__(self) -> None:
        """
        Initializes the Redis client and flushes the database.
        This ensures that the Redis cache is
        empty when the Cache instance is created.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls  # Apply the count_calls decorator to store
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the provided data in the Redis cache.

        Args:
            data (Union[str, bytes, int, float]):
                The data to store in Redis.
                Can be a string, bytes, int, or float.

        Returns:
            str: A unique key generated for the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Retrieves data from the Redis
        cache using the provided key.
        Optionally applies a conversion function.

        Args:
            key (str): The Redis key for the data.
            fn (Optional[Callable]):
                A function to apply to the retrieved
                data for conversion (e.g., decode, int).
                Defaults to None.

        Returns:
            Any: The retrieved data, optionally
            converted by the provided function,
                or None if the key doesn't exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves data from Redis and decodes it as a UTF-8 string.

        Args:
            key (str): The Redis key for the data.

        Returns:
            Optional[str]: The retrieved data decoded as a string,
            or None if the key doesn't exist.
        """
        return self.get(key=key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves data from Redis and converts it to an integer.

        Args:
            key (str): The Redis key for the data.

        Returns:
            Optional[int]: The retrieved data converted to an integer,
            or None if the key doesn't exist.
        """
        return self.get(key=key, fn=int)
