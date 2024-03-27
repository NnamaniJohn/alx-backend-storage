#!/usr/bin/env python3
"""
Redis
"""
import redis
import uuid
import typing


def count_calls(method: typing.Callable) -> typing.Callable:
    """
    count calls
    :param method:
    :return:
    """
    def wrapper(cls, data: str | bytes | int | float):
        """
        wrapper
        :param cls:
        :param data:
        :return:
        """
        cls._redis.incr(wrapper.__qualname__)
        return method(cls, data)
    return wrapper


class Cache:
    """
    Cache class
    """

    def __init__(self):
        """
        init cache
        :return:
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: str | bytes | int | float) -> str:
        """
        store
        :param data:
        :return:
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: typing.Callable = None) -> str | bytes | int | float:
        """
        get
        :param key:
        :param fn:
        :return:
        """
        value = self._redis.get(key)
        if value and fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        get str
        :param key:
        :return:
        """
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """
        get int
        :param key:
        :return:
        """
        return self.get(key, fn=int)
