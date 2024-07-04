#!/usr/bin/env python3
"""Module for summing a mixed list of integers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum a mixed list of integers and floats and return the result."""
    return float(sum(mxd_lst))
