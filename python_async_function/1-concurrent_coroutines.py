#!/usr/bin/env python3
"""
an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Waits for a random delay between 0 and max_delay"""
    delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)
