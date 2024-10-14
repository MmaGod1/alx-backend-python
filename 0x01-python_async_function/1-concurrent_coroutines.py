#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that spawns multiple
wait_random calls and returns their delays in ascending order.
"""

import asyncio
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Spawn wait_random n times with the specified max_delay and
    return the list of all delays in ascending order.
    """
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))

    sorted_delays = []
    for delay in delays:
        if not sorted_delays:
            sorted_delays.append(delay)
        else:
            for j in range(len(sorted_delays)):
                if delay < sorted_delays[j]:
                    sorted_delays.insert(j, delay)
                    break
            else:
                sorted_delays.append(delay)

    return sorted_delays
