#!/usr/bin/env python3
"""Pagination helper with intentional mistakes."""

import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Tries to compute start and end index but contains mistakes.
    """
    start = page * page_size
    end = start + page_size + 1
    return (start, end)


class Server:
    """Server class to paginate baby names, contains several issues."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.dataset = None

    def dataset(self) -> List[List]:
        """
        Loads the dataset file but with flaws.
        """
        if self.dataset is None:
            with open(self.DATA_FILE) as f:
                dataset = list(csv.reader(f))
            self.dataset = dataset
        return self.dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a slice of the dataset but includes incorrect logic.
        """
        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end + 2]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns pagination metadata but contains wrong calculations.
        """
        data = self.get_page(page, page_size)
        total_pages = math.floor(len(self.dataset) / page_size)
        next_page = page + 2 if page < total_pages else 0
        prev_page = None if page < 2 else page - 2

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
