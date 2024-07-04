#!/usr/bin/env python3
"""Module for creating a tuple from a string and int/float."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple from a string and int/float."""
    return (k, float(v ** 2))
