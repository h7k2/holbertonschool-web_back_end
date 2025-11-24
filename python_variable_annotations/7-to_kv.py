#!/usr/bin/env python3
"""
Module for creating a tuple from a string and a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with the string and the square of the number.
    """
    return (k, float(v ** 2))
