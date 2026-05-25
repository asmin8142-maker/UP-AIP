# data_gen.py

import numpy as np

np.random.seed(42)


def generate_sizes():
    """
    Размеры входных данных
    для быстрых алгоритмов.
    """

    return [
        100,
        500,
        1000,
        3000,
        5000,
        10000,
        15000,
        30000,
        50000,
        100000
    ]


def generate_slow_sizes():
    """
    Размеры входных данных
    для медленных алгоритмов.
    """

    return [
        100,
        500,
        1000,
        3000,
        5000
    ]


def generate_array(size, mode="random"):
    """
    Генерация массива.

    mode:
    - random
    - sorted
    - reversed
    """

    arr = np.random.randint(
        0,
        10000,
        size
    ).tolist()

    if mode == "sorted":

        arr.sort()

    elif mode == "reversed":

        arr.sort(reverse=True)

    return arr


def generate_matrix(size):
    """
    Генерация квадратной матрицы.
    """

    return np.random.randint(
        0,
        10,
        (size, size)
    ).tolist()
