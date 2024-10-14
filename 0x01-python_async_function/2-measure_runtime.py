#!/usr/bin/env python3
"""Module for measuring execution time of wait_n.
"""

import asyncio
import time
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the average execution time for wait_n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
