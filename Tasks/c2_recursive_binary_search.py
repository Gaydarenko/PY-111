from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    print(elem, arr)
    if elem not in arr:
        return None
    try:
        half = (binary_search.finish + binary_search.start) // 2
        if half == binary_search.start:
            res = binary_search.start
            del(binary_search.start, binary_search.finish)
            return res
        if elem in arr[binary_search.start: half]:
            binary_search.finish = half
        else:
            binary_search.start = half
    except AttributeError:
        binary_search.start = 0
        binary_search.finish = len(arr)
    return binary_search(elem, arr)


if __name__ == '__main__':
    # x = [0, 1, 2, 3, 4, 5, 6, 7]
    # print(binary_search(7, x))
    y = [i for i in range(100)] + [101]
    # y = [1, 2, 2, 2]
    binary_search(5, y)
    # print(y.index(101))
