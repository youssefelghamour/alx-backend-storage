#!/usr/bin/env python3
""" module for Cache class """
import redis
import uuid
from typing import Union, Callable


class Cache:
    """ Cache class """

    def __init__(self):
        """ init method """
        self._redis = redis.Redis()
        self._redis.flushdb()

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
