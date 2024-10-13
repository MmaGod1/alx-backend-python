#!/usr/bin/env python3
"""
Module to zoom in on an array based on a specified factor.
"""


from typing import List, Tuple

def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Returns a new list with each element of the input list repeated
    based on the zoom factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array = [12, 72, 91]

zoom_2x = zoom_array(array)

# Ensure that we pass an integer factor
zoom_3x = zoom_array(array, int(3.0))  # Convert to int if a float is provided
