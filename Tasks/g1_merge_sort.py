from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) < 2:
        return container
    else:
        middle = len(container) // 2
        left = sort(container[:middle])
        right = sort(container[middle:])
    res = []
    while left or right:
        if not left:
            res.extend(right)
            right = []
        elif not right:
            res.extend(left)
            left = []
        elif left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append((right.pop(0)))
    return res
