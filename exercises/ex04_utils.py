"""Exercise 04 List Utility Functions!"""

__author__ = 730643380


def all(vals: list[int], num: int) -> bool:
    """This while loop checks each index to see if it is not equal to num, if not then it'll return true."""
    index: int = 0
    if vals == []:
        return False
    while index < len(vals):
        if vals[index] != num:
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    """The while loop compares each elemtn in the list and the highest int becomes the max which is later returned."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    index: int = 1
    greaterestest: int = input[0]
    while index < len(input):
        if greaterestest < input[index]:
            greaterestest = input[index]
        index += 1
    return greaterestest


def is_equal(vals1: list[int], vals2: list[int]) -> bool:
    """This function checks if both lengths of the lists are not equal then it returns False, otherwise it enters the while loop and compares indexes."""
    index: int = 0
    if len(vals1) != len(vals2):
        return False
    while index < len(vals1):
        if vals1[index] != vals2[index]:
            return False
        index += 1
    return True


def extend(vals1: list[int], vals2: list[int]) -> None:
    """This function adds vals2 on the end of vals1."""
    index: int = 0
    while index < len(vals2):
        vals1.append(vals2[index])
        index += 1
    