#!/usr/bin/env python3
"""
an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int,  max_delay: int) -> float:
    """Waits for a random delay between 0 and max_delay"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return time.perf_counter() - start
