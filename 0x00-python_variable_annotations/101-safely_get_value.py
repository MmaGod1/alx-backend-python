#!/usr/bin/env python3
"""
Module to safely retrieve a value from a dictionary with a default.
"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
ReturnType = Union[Any, T]
DefaultType = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: DefaultType = None) -> ReturnType:
    """
    Retrieves the value for a given key from a dictionary, or returns the default if the key does not exist.
    """
    if key in dct:
        return dct[key]
    return default
