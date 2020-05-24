"""
This module implements some functions based on linear search algorithm
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    print(arr)

    # ver.1
    # return arr.index(min(arr))

    # ver.2
    ind = 0
    r = arr[ind]
    for i in range(1, len(arr)):
        if arr[i] < r:
            ind = i
            r = arr[ind]
    return ind
