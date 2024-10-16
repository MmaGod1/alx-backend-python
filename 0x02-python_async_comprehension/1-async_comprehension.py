#!/usr/bin/env python3
"""Async Comprehension Task"""
from typing import List
from 0_async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Gathers 10 random numbers from the async generator."""
    return [value async for value in async_generator()]
