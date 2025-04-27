#!/usr/bin/env python3
"""Type-annotated function element_length that takes a list lst
of floats as argument and returns a list of tuples with the element
and its length."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with the element and its length"""
    return [(i, len(i)) for i in lst]
