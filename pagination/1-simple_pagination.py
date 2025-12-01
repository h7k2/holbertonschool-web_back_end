#!/usr/bin/env python3
"""Simple helper function and pagination server."""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Compute the start and end indexes for a given pagination request.

    The logic is straightforward:
    - pages start at 1
    - each page contains `page_size` items
    - we translate the page number into list slice boundaries

    Args:
        page (int): Page number, starting from 1.
        page_size (int): How many items are displayed per page.

    Returns:
        tuple: (start_index, end_index) for slicing a list.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
