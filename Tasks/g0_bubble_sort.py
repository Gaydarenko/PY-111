from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    size = len(container) - 1
    move = True
    for _ in range(len(container)):
        if not move:
            break
        move = False
        for i in range(size):
            if container[i] > container[i+1]:
                container[i], container[i+1] = container[i+1], container[i]
                move = True
        size -= 1
    return container
