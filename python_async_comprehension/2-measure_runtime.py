#!/usr/bin/env python3
"""Mesures time"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures time"""
    start_time = time.time()
    await asyncio.gather(async_comprehension())
    return time.time() - start_time
