#!/usr/bin/env python3
"""
Module for getting element lengths in an iterable of sequences.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element and its length.
    """
    return [(i, len(i)) for i in lst]
