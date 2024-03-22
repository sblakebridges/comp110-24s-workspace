"""Splitting a dictionary into two lists."""

__author__ = "730643380"


def get_keys(dic: dict[str, int]) -> list[str]:
    """Get Keys."""
    indict: list[str] = []
    for key in dic:
        indict.append(key)
    return indict


def get_values(dic: dict[str, int]) -> list[int]:
    """Get Values."""
    indict: list[int] = []
    for key in dic:
        indict.append(dic[key])
    return indict