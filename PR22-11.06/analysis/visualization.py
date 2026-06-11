import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_FILE = "data/movies.csv"


def create_graphs():

    df = pd.read_csv(DATA_FILE)

    # создаём папку output (если нет)
    import os
    os.makedirs("output", exist_ok=True)

    # =====================
    # 1. BAR CHART
    # =====================
    top_lang = df.groupby("original_language")["revenue"].mean().head(10)

    plt.figure()
    top_lang.plot(kind="bar")
    plt.title("Average revenue by language")
    plt.xlabel("Language")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/bar_chart.png")
    plt.close()

    # =====================
    # 2. LINE CHART
    # =====================
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    yearly = df.groupby(df["release_date"].dt.year)["revenue"].mean()

    plt.figure()
    yearly.plot(kind="line", marker="o")
    plt.title("Average revenue over years")
    plt.xlabel("Year")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("output/line_chart.png")
    plt.close()

    # =====================
    # 3. HISTOGRAM
    # =====================
    plt.figure()
    plt.hist(df["revenue"], bins=30)
    plt.title("Revenue distribution")
    plt.xlabel("Revenue")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("output/histogram.png")
    plt.close()

    # =====================
    # 4. SCATTER PLOT
    # =====================
    plt.figure()
    plt.scatter(df["budget"], df["revenue"], alpha=0.5)
    plt.title("Budget vs Revenue")
    plt.xlabel("Budget")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("output/scatter.png")
    plt.close()

    # =====================
    # 5. HEATMAP (корреляция)
    # =====================
    corr = df[["budget", "revenue", "popularity", "vote_average"]].corr()

    plt.figure()
    plt.imshow(corr, cmap="coolwarm")
    plt.colorbar()
    plt.title("Correlation Heatmap")
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.tight_layout()
    plt.savefig("output/heatmap.png")
    plt.close()

    print("Графики сохранены в папку output/")