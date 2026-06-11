import pandas as pd

DATA_FILE = "data/movies.csv"


def run_pandas_tasks():

    df = pd.read_csv(DATA_FILE)

    print("\n===== PANDAS ANALYSIS =====")

    # №5 Первичный обзор
    print("\n--- HEAD ---")
    print(df.head(10))

    print("\n--- TAIL ---")
    print(df.tail(5))

    print("\n--- SHAPE ---")
    print(df.shape)

    print("\n--- DTYPES ---")
    print(df.dtypes)

    print("\n--- COLUMNS ---")
    print(df.columns)

    print("\n--- INFO ---")
    print(df.info())

    print("\n--- DESCRIBE ---")
    print(df.describe())

    # №6 Пропуски
    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())

    # Заполнение пропусков
    numeric_cols = df.select_dtypes(include=["number"]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    object_cols = df.select_dtypes(include=["object"]).columns
    df[object_cols] = df[object_cols].fillna("Неизвестно")

    print("\n--- AFTER FILL MISSING ---")
    print(df.isnull().sum())

    # №7 Дубликаты
    print("\n--- DUPLICATES ---")
    print(df.duplicated().sum())

    df = df.drop_duplicates()

    print("После удаления:", df.duplicated().sum())

    # №8 Новые признаки
    df["profit"] = df["revenue"] - df["budget"]
    df["budget_diff"] = df["budget"] - df["budget"].mean()

    print("\n--- NEW FEATURES ---")
    print(df[["budget", "revenue", "profit", "budget_diff"]].head())

    # Перевод даты
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")

    df["year"] = df["release_date"].dt.year
    df["month"] = df["release_date"].dt.month

    print("\n--- DATE FEATURES ---")
    print(df[["release_date", "year", "month"]].head())

    # №9 GroupBy
    group = df.groupby("original_language").agg({
        "revenue": ["mean", "sum", "max"],
        "budget": ["mean"]
    })

    print("\n--- GROUPBY LANGUAGE ---")
    print(group.sort_values(("revenue", "sum"), ascending=False).head())

    # №10 Фильтрация
    filtered = df[(df["budget"] > 10000000) & (df["revenue"] > 50000000)]

    print("\n--- FILTERED DATA ---")
    print(filtered[["title", "budget", "revenue"]].head())

    sorted_df = df.sort_values(by=["revenue", "budget"], ascending=[False, False])

    print("\n--- TOP FILMS ---")
    print(sorted_df[["title", "revenue", "budget"]].head())

    print("\n--- QUERY ---")
    print(df.query("revenue > 100000000 and budget > 50000000").head())