#!/usr/bin/env python3
"""This module contains a coroutine
that yields random floats asynchronously"""


import asyncio
import random


async def async_generator():
    """async generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
