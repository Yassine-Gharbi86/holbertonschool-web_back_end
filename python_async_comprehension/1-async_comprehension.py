#!/usr/bin/env python3
"""Generates a list from an async comprehension"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Generates a list from an async comprehension"""
    return [i async for i in async_generator()]
