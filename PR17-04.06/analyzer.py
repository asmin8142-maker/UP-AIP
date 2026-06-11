import emoji
from collections import Counter


def general_stats(df):

    total_messages = len(df)

    participants = df["sender"].nunique()

    top_author = (
        df["sender"]
        .value_counts()
        .idxmax()
    )

    top_author_count = (
        df["sender"]
        .value_counts()
        .max()
    )

    peak_hour = (
        df["hour"]
        .value_counts()
        .idxmax()
    )

    return {
        "total_messages": total_messages,
        "participants": participants,
        "top_author": top_author,
        "top_author_count": top_author_count,
        "peak_hour": peak_hour
    }


def messages_by_hour(df):
    return (
        df["hour"]
        .value_counts()
        .sort_index()
    )


def messages_by_day(df):
    return (
        df.groupby("day")
        .size()
    )


def messages_by_weekday(df):

    weekdays = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",
        6: "Воскресенье"
    }

    data = (
        df["datetime"]
        .dt.dayofweek
        .map(weekdays)
        .value_counts()
    )

    order = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье"
    ]

    return data.reindex(order)


stop_words = {
    "и", "в", "на", "с", "по", "а",
    "что", "это", "как", "к", "из",
    "не", "да", "но", "у", "за",
    "от", "для", "то", "же",

    "отсутствует",
    "аудиофайл",
    "изображение",
    "видео",
    "видеозвонок",
    "аудиозвонок",
    "ответа",
    "сек",
    "мин",
    "стикер",
    "добавлен",
    "удалено",
    "пропущенный",
    "групповой",
    "звонок",
    "приглашено",
    "нажмите",
    "перезвонить"
}

    text = " ".join(
        df["text"]
        .astype(str)
    ).lower()

    words = []

    for word in text.split():

        word = word.strip(
            ".,!?;:()[]{}\"'"
        )

        if len(word) > 2 and word not in stop_words:
            words.append(word)

    return Counter(words).most_common(n)


def top_emojis(df, n=10):

    emojis = []

    for text in df["text"].astype(str):

        for char in text:

            if char in emoji.EMOJI_DATA:
                emojis.append(char)

    return Counter(emojis).most_common(n)