#!/usr/bin/env python3
"""Module that defines a function to wait
for a random delay between 0 and max_delay"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Waits for a random delay between 0 and max_delay"""
    return [await task_wait_random(max_delay) for _ in range(n)]
