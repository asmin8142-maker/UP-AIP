# benchmark.py

import time
import csv
import statistics

from tqdm import tqdm

from algorithms import *
from data_gen import *


def benchmark_algorithm(func, data, repeats=7):

    times = []

    for _ in range(repeats):

        start = time.perf_counter()

        if isinstance(data, tuple):

            func(*data)

        else:

            func(data)

        end = time.perf_counter()

        times.append(end - start)

    return statistics.median(times)


def run_benchmarks():

    sizes = generate_sizes()

    slow_sizes = generate_slow_sizes()

    results = []

    algorithms = {

        "linear_search":
            lambda arr: linear_search(arr, -1),

        "binary_search":
            lambda arr: binary_search(arr, -1),

        "sum_elements":
            sum_elements,

        "merge_sort":
            merge_sort,

        "bubble_sort":
            bubble_sort,

        "insertion_sort":
            insertion_sort
    }

    for name, func in algorithms.items():

        current_sizes = sizes

        if name in [
            "bubble_sort",
            "insertion_sort"
        ]:
            current_sizes = slow_sizes

        for size in tqdm(
                current_sizes,
                desc=name
        ):

            arr = generate_array(size)

            t = benchmark_algorithm(
                func,
                arr
            )

            results.append(
                [name, size, t]
            )

    # =========================
    # Matrix Multiply
    # =========================

    matrix_sizes = [
        5,
        10,
        20,
        30,
        40
    ]

    for size in tqdm(
            matrix_sizes,
            desc="matrix_multiply"
    ):

        A = generate_matrix(size)

        B = generate_matrix(size)

        t = benchmark_algorithm(
            matrix_multiply,
            (A, B),
            repeats=3
        )

        results.append(
            ["matrix_multiply", size, t]
        )

    # =========================
    # Fibonacci
    # =========================

    fib_sizes = list(range(1, 31))

    for n in tqdm(
            fib_sizes,
            desc="fibonacci"
    ):

        t = benchmark_algorithm(
            fibonacci,
            n,
            repeats=1
        )

        results.append(
            ["fibonacci", n, t]
        )

    # =========================
    # Save CSV
    # =========================

    with open(
            "results.csv",
            "w",
            newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["algorithm", "size", "time"]
        )

        writer.writerows(results)

    print("results.csv сохранён")
