#!/usr/bin/env python3
"""Module to zoom in on an array based on a specified factor."""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Creates multiple copies of items in a tuple.

    Args:
        lst (Tuple): A tuple of items.
        factor (int): The number of times to repeat each item.

    Returns:
        List: A list containing the zoomed-in values.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
