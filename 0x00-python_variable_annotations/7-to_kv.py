#!/usr/bin/env python3
"""
Module to convert a string and a number into a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k and the square of v.
    """
    return (k, float(v ** 2))
