"""Summing the elements of a list using different loops."""

__author__ = "730643380"


def w_sum(vals: list[float]) -> float:
    """Using a while loop, if the index is less than the length of the list then it will add index positions to sum."""
    sum: float = 0.0
    index: int = 0
    if vals == []:
        return sum
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum 


def f_sum(vals: list[float]) -> float:
    """Goes through the index positions of vals and adds each element to sum."""
    sum: float = 0.0
    if vals == []:
        return sum
    for i in vals:
        sum += i
    return sum


def f_range_sum(vals: list[float]) -> float:
    """This function goes through the elemnts in the list and adds them together within the range of the list (vals)."""
    sum: float = 0.0
    if vals == []:
        return sum
    for i in range(len(vals)):
        sum += vals[i]
    return sum