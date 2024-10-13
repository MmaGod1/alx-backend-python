#!/usr/bin/env python3
"""
Module to compute the length of each element in a list.
"""


from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing an element and its length.
    """
    return [(i, len(i)) for i in lst]
