#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
import time
from importlib import import_module as load_module
async_comprehension = load_module('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of running async_comprehension.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
