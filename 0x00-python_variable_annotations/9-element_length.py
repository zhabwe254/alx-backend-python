#!/usr/bin/env python3
"""Module for getting lengths of elements in a list."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples, each containing a sequence and its length."""
    return [(i, len(i)) for i in lst]
