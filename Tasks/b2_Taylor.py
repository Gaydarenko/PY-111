"""
Taylor series
"""
from typing import Union
from numpy import e
from numpy import log
from numpy import sin

def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    print(x)
    return 0


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


# if __name__ == '__main__':
    # print(e)
    print(sinx(1.55433))
    print(sin(1.55433))
