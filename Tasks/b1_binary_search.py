from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    print(elem, arr)
    if elem not in arr:
        return None
    start = 0
    finish = len(arr)
    while True:
        half = int((finish + start) // 2)
        if half == start:
            return start
        if elem in arr[start: half]:
            finish = half
        else:
            start = half


if __name__ == '__main__':
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(binary_search(5, x))