#!/usr/bin/env python3
"""
Coroutine that collects 10 random numbers from async_generator
using an async comprehension.
"""

from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehension
    over async_generator(), and return them as a list.

    Returns:
        List[float]: 10 random numbers asynchronously generated.
    """
    return [i async for i in async_generator()]
