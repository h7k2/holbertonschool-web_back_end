#!/usr/bin/env python3
"""Simple helper function and pagination server."""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Compute start and end indexes for a given page.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Items per page.

    Returns:
        Tuple[int, int]: Start and end indexes for slicing.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset, skipping the header row."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                rows = [row for row in reader]
            self.__dataset = rows[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the rows corresponding to a specific page.

        Args:
            page (int): Page number (must be > 0).
            page_size (int): Items per page (must be > 0).

        Returns:
            List[List]: The requested page of data.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        return data[start:end]
