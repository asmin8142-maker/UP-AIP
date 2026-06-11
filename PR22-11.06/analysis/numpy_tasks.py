import numpy as np
import pandas as pd

DATA_FILE = "data/movies.csv"


def run_numpy_tasks():

    df = pd.read_csv(DATA_FILE)

    revenue = df["revenue"].to_numpy()
    budget = df["budget"].to_numpy()

    print("\n===== NUMPY ANALYSIS =====")

    print("Shape:", revenue.shape)
    print("Dtype:", revenue.dtype)
    print("Size:", revenue.size)

    print("\nПервые 10 элементов")
    print(revenue[:10])

    print("\nКаждый третий")
    print(revenue[::3][:10])

    print("\nС 50 по 100")
    print(revenue[50:100])

    print("\nМинимум:", np.min(revenue))
    print("Максимум:", np.max(revenue))
    print("Среднее:", np.mean(revenue))
    print("Медиана:", np.median(revenue))

    print("Std:", np.std(revenue))
    print("Var:", np.var(revenue))

    print("25%:", np.percentile(revenue, 25))
    print("50%:", np.percentile(revenue, 50))
    print("75%:", np.percentile(revenue, 75))

    print("argmax:", np.argmax(revenue))
    print("argmin:", np.argmin(revenue))

    above_mean = revenue[revenue > np.mean(revenue)]
    print("Выше среднего:", len(above_mean))

    outliers = revenue[
        revenue > np.mean(revenue) + 2 * np.std(revenue)
    ]

    print("Выбросов:", len(outliers))

    labels = np.where(
        revenue > np.mean(revenue),
        "Высокий",
        "Низкий"
    )

    print(labels[:20])

    print(
        "Пропусков:",
        np.isnan(revenue).sum()
    )

    minmax = (
        revenue - revenue.min()
    ) / (
        revenue.max() - revenue.min()
    )

    print(minmax[:10])

    zscore = (
        revenue - revenue.mean()
    ) / revenue.std()

    print(zscore[:10])

    corr = np.corrcoef(
        budget,
        revenue
    )[0, 1]

    print(
        "\nКорреляция budget/revenue:",
        corr
    )