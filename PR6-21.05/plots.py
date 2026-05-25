# plots.py

import pandas as pd
import matplotlib.pyplot as plt
import time

from data_gen import generate_array
from algorithms import bubble_sort, merge_sort


def plot_all():

    df = pd.read_csv("results.csv")

    # =========================
    # График 1
    # =========================

    fig, ax = plt.subplots(figsize=(10, 6))

    for algo in df["algorithm"].unique():

        subset = df[df["algorithm"] == algo]

        ax.plot(
            subset["size"],
            subset["time"],
            marker="o",
            label=algo
        )

    ax.set_title("Время выполнения алгоритмов")

    ax.set_xlabel("Размер входных данных")

    ax.set_ylabel("Время (секунды)")

    ax.legend()

    fig.savefig(
        "plot_linear.png",
        dpi=150,
        bbox_inches="tight"
    )

    # =========================
    # График 2 — Log-Log
    # =========================

    fig, ax = plt.subplots(figsize=(10, 6))

    for algo in df["algorithm"].unique():

        if algo == "fibonacci":
            continue

        subset = df[df["algorithm"] == algo]

        ax.loglog(
            subset["size"],
            subset["time"],
            marker="o",
            label=algo
        )

    ax.set_title("Log-Log график сложности")

    ax.set_xlabel("Размер входных данных")

    ax.set_ylabel("Время")

    ax.legend()

    fig.savefig(
        "plot_loglog.png",
        dpi=150,
        bbox_inches="tight"
    )

    # =========================
    # График 3
    # Лучший / Средний / Худший
    # =========================

    sizes = [50, 100, 200, 300, 400]

    bubble_best = []
    bubble_avg = []
    bubble_worst = []

    merge_best = []
    merge_avg = []
    merge_worst = []

    for size in sizes:

        arr_best = generate_array(size, "sorted")

        arr_avg = generate_array(size, "random")

        arr_worst = generate_array(size, "reversed")

        # Bubble Sort

        start = time.perf_counter()
        bubble_sort(arr_best)
        bubble_best.append(
            time.perf_counter() - start
        )

        start = time.perf_counter()
        bubble_sort(arr_avg)
        bubble_avg.append(
            time.perf_counter() - start
        )

        start = time.perf_counter()
        bubble_sort(arr_worst)
        bubble_worst.append(
            time.perf_counter() - start
        )

        # Merge Sort

        start = time.perf_counter()
        merge_sort(arr_best)
        merge_best.append(
            time.perf_counter() - start
        )

        start = time.perf_counter()
        merge_sort(arr_avg)
        merge_avg.append(
            time.perf_counter() - start
        )

        start = time.perf_counter()
        merge_sort(arr_worst)
        merge_worst.append(
            time.perf_counter() - start
        )

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(
        sizes,
        bubble_best,
        marker="o",
        label="Bubble Best"
    )

    ax.plot(
        sizes,
        bubble_avg,
        marker="o",
        label="Bubble Average"
    )

    ax.plot(
        sizes,
        bubble_worst,
        marker="o",
        label="Bubble Worst"
    )

    ax.plot(
        sizes,
        merge_best,
        marker="o",
        label="Merge Best"
    )

    ax.plot(
        sizes,
        merge_avg,
        marker="o",
        label="Merge Average"
    )

    ax.plot(
        sizes,
        merge_worst,
        marker="o",
        label="Merge Worst"
    )

    ax.set_title(
        "Лучший / Средний / Худший случай"
    )

    ax.set_xlabel("Размер массива")

    ax.set_ylabel("Время")

    ax.legend()

    fig.savefig(
        "plot_compare.png",
        dpi=150,
        bbox_inches="tight"
    )

    # =========================
    # График 4 — Heatmap
    # =========================

    matrix = df[
        df["algorithm"] == "matrix_multiply"
    ]

    fig, ax = plt.subplots(figsize=(8, 6))

    heatmap = matrix.pivot_table(
        values="time",
        index="size",
        columns="algorithm"
    )

    im = ax.imshow(heatmap)

    fig.colorbar(im)

    ax.set_title(
        "Heatmap умножения матриц"
    )

    fig.savefig(
        "plot_heatmap.png",
        dpi=150,
        bbox_inches="tight"
    )

    print("Графики сохранены")
