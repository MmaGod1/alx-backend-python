#!/usr/bin/env python3
"""Async Comprehensions"""
from typing import List
from importlib import import_module as load_module
async_gen = load_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Generates a list of 10 floating-point numbers from async_gen.
    """
    return [item async for item in async_gen()]
