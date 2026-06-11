from loader import load_whatsapp_chat

from analyzer import (
    general_stats,
    messages_by_hour,
    messages_by_day,
    top_words,
    top_emojis
)

from visualizer import (
    plot_hour_activity,
    plot_day_activity,
    generate_word_cloud
)


print("Загрузка данных...")

df = load_whatsapp_chat("data/_chat.txt")

if df.empty:
    print("Чат пуст.")
    exit()


stats = general_stats(df)

print("\n===== ОБЩАЯ СТАТИСТИКА =====")

print(
    f"Всего сообщений: {stats['total_messages']}"
)

print(
    f"Количество участников: {stats['participants']}"
)

print(
    f"Самый активный участник: {stats['top_author']}"
)

print(
    f"Сообщений у лидера: {stats['top_author_count']}"
)

print(
    f"Пиковый час: {stats['peak_hour']}:00"
)


print("\n===== ТОП-20 СЛОВ =====")

for word, count in top_words(df):
    print(f"{word}: {count}")


print("\n===== ТОП-10 ЭМОДЗИ =====")

for emo, count in top_emojis(df):
    print(f"{emo}: {count}")


by_hour = messages_by_hour(df)
plot_hour_activity(by_hour)

by_day = messages_by_day(df)
plot_day_activity(by_day)

generate_word_cloud(df)

print("\nГотово!")

print("Созданы файлы:")

print("output/hours.png")
print("output/days.png")
print("output/wordcloud.png")