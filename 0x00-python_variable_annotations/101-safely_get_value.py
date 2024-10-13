#!/usr/bin/env python3
"""
Module to safely get a value from a dictionary with a default.
"""


from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """
    Returns the value for the given key if it exists in the dictionary, otherwise returns the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
