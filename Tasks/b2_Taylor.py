"""
Taylor series
"""
from typing import Union
from numpy import e     # just for my tests
from numpy import sin   # just for my tests

def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    print(x)
    res = 0
    for n in range(15):
        fact_n = 1
        for i in range(1, n + 1):
            fact_n *= i
        res += x ** n / fact_n
    return res


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    print(x)
    res = 0
    for n in range(1, 7):
        fact_n = 1
        for i in range(1, 2 * n):
            fact_n *= i
        res += (-1) ** (n - 1) * x ** (2 * n - 1) / fact_n
    return res


if __name__ == '__main__':
    # print(e)
    print(ex(1.55433))
    print(e ** 1.55433)
    print(sinx(1.55433))
    print(sin(1.55433))
