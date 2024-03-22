"""Mutating functions."""

__author__ = "730643380"


def manual_append(unambiguousa: list[int], b: int) -> None:
    """Manual Append."""
    unambiguousa.append(b)


def double(unambiguousa: list[int]) -> None:
    """Double."""
    counter = 0
    while counter < len(unambiguousa):
        unambiguousa[counter] *= 2
        counter += 1 
    
