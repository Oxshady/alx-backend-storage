#!/usr/bin/env python3
"""A module for using the Redis NoSQL data storage.
This module provides a Cache class that interacts with a
Redis database. It allows storing data in Redis and retrieving it
with optional type conversions. The Redis database is flushed upon
initialization of the Cache instance.
"""
import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


def count_calls(method: Callable) -> Callable:
    """Tracks the number of calls
    made to a method in a Cache class.
    Increments a Redis key that
    corresponds to the method's qualified name.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The wrapped method
        that increments the call count.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Invokes the given method after
        incrementing its call counter."""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Tracks the call history
    of a method in a Cache class.
    Stores the inputs and outputs of the method calls.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The wrapped
        method that tracks input and output history.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        key_input = f"{method.__qualname__}:inputs"
        key_output = f"{method.__qualname__}:outputs"
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(key_input, str(args))
        data = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(key_output, data)
        return data

    return wrapper


def replay(fn: Callable) -> None:
    """Displays the call history of a Cache class method"""
    if fn is None or not hasattr(fn, "__self__"):
        return

    redius = getattr(fn.__self__, "_redis", None)
    if not isinstance(redius, redis.Redis):
        return

    method_name = fn.__qualname__
    in_key = f"{method_name}:inputs"
    out_key = f"{method_name}:outputs"
    num_of_calls = int(redius.get(method_name) or 0)

    print(f"{method_name} was called {num_of_calls} times:")

    inputs = redius.lrange(in_key, 0, -1)
    outputs = redius.lrange(out_key, 0, -1)

    for ins, outs in zip(inputs, outputs):
        print(
            f'{method_name}(*{ins.decode("utf-8")}) -> {outs.decode("utf-8")}'
            )


class Cache:
    """Represents an object
    for storing data in a Redis data storage.

    Methods:
        store(data: Union[str, bytes, int, float]) -> str:
            Stores data in the Redis
            cache and returns a unique key.

        get(key: str, fn: Optional[Callable] = None) ->
        Union[str, bytes, int, float, None]:
            Retrieves data from the Redis
            cache using the provided key.
            Optionally applies a conversion
            function to the data.

        get_str(key: str) -> Optional[str]:
            Retrieves the data as a UTF-8 decoded string.

        get_int(key: str) -> Optional[int]:
            Retrieves the data as an integer.
    """

    def __init__(self) -> None:
        """Initializes a Cache instance.
        This ensures that the Redis cache is
        empty when the Cache instance is created.
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a value in a Redis data
        storage and returns the key.

        Args:
            data (Union[str, bytes, int, float]):
                The data to store in Redis.
                Can be a string, bytes, int, or float.

        Returns:
            str: A unique key generated
            for the stored data.
        """
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(
        self,
        key: str,
        fn: Callable = None,
    ) -> Union[str, bytes, int, float]:
        """Retrieves a value from a Redis data storage.

        Args:
            key (str): The Redis key for the data.
            fn (Optional[Callable]): A function to apply
            to the retrieved data for conversion.

        Returns:
            Union[str, bytes, int, float]:
            The retrieved data, optionally converted
            by the provided function,
            or None if the key doesn't exist.
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """Retrieves a string value from a Redis data storage.

        Args:
            key (str): The Redis key for the data.

        Returns:
            str: The retrieved data decoded as a string,
            or None if the key doesn't exist.
        """
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieves an integer value from a Redis data storage.

        Args:
            key (str): The Redis key for the data.

        Returns:
            int: The retrieved data converted to an integer,
            or None if the key doesn't exist.
        """
        return self.get(key, lambda x: int(x))
