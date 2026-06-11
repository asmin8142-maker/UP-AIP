import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud


if not os.path.exists("output"):
    os.makedirs("output")


def plot_hour_activity(by_hour):

    plt.figure(figsize=(10, 5))

    by_hour.plot(
        kind="line",
        marker="o"
    )

    plt.title("Активность по часам")

    plt.xlabel("Час")

    plt.ylabel("Сообщения")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("output/hours.png")

    plt.close()


def plot_day_activity(by_day):

    plt.figure(figsize=(12, 5))

    ax = by_day.plot(
        kind="bar"
    )

    moving_avg = (
        by_day
        .rolling(window=3)
        .mean()
    )

    ax.plot(
        range(len(moving_avg)),
        moving_avg,
        linewidth=3
    )

    plt.title("Активность по дням")

    plt.xlabel("Дата")

    plt.ylabel("Сообщения")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("output/days.png")

    plt.close()


def generate_word_cloud(df):

    text = " ".join(
        df["text"]
        .dropna()
        .astype(str)
    )

    stop_words = {
        "и", "в", "на", "с", "по",
        "а", "что", "это", "как",
        "не", "да", "но",
        "отсутствует",
        "аудиофайл",
        "изображение",
        "видео",
        "стикер",
        "удалено"
    }

    wordcloud = WordCloud(
        width=1200,
        height=800,
        background_color="white",
        stopwords=stop_words
    ).generate(text)

    plt.figure(figsize=(12, 8))

    plt.imshow(wordcloud)

    plt.axis("off")

    plt.tight_layout()

    plt.savefig("output/wordcloud.png")

    plt.close()