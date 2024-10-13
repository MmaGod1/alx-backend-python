#!/usr/bin/env python3
"""
Module to create a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.
    """
    def multiply(value: float) -> float:
        return multiplier * value

    return multiply
