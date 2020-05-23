"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any

COUNT_PRIORiTY = 10
priority_deque = {p: [] for p in range(COUNT_PRIORiTY)}

def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global priority_deque

    priority_deque[priority] = priority_deque[priority].append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    global priority_deque

    for p in priority_deque:
        if priority_deque[p]:
            return priority_deque[p][0]
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    for i in range(ind):
        res = dequeue()
    return res


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global priority_deque

    priority_deque.clear()
    priority_deque = {p: [] for p in range(COUNT_PRIORiTY)}
    return None
