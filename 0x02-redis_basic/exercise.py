#!/usr/bin/env python3
""" module for Cache class """
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ decorator to count the number of times a method is called """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function that increments the call count in Redis """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ decorator to store input and output history of a method using
        Redis lists """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function to capture inputs and outputs and store
            them in Redis """
        # convert args to string for simplicity
        input_str = str(args)

        # Redis key for inputs and outputs lists
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        # store input in Redis list
        self._redis.rpush(inputs_key, input_str)

        # execute the original method to get the output
        output = method(self, *args, **kwargs)

        # store output in Redis list
        self._redis.rpush(outputs_key, output)

        return output
    return wrapper


class Cache:
    """ Cache class """

    def __init__(self):
        """ init method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ stores the data with a randomly generated key
            and returns the key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes,
                                                          int, float]:
        """ retrieves the data for a key
            and optionally applies a function to convert it """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        else:
            return value

    def get_str(self, key: str) -> str:
        """ retrieves the data for a key and converts it to a string """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ retrieves the data for a key and converts it to an int """
        return self.get(key, lambda d: int(d))
