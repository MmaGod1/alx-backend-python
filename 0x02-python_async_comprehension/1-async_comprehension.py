#!/usr/bin/env python3
"""Async Comprehension Task"""
from typing import List
async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Gathers 10 random numbers from the async generator."""
    return [value async for value in async_generator()]
