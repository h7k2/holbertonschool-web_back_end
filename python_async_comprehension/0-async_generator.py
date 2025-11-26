#!/usr/bin/env python3
"""
Asynchronous generator that yields random numbers between 0 and 10.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yield a random number between 0 and 10, ten times.
    Each yield occurs after a 1-second asynchronous pause.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
