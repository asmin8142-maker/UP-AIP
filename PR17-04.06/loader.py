import re
import pandas as pd


def load_whatsapp_chat(path):
    pattern = r'^\[(\d{2}\.\d{2}\.\d{4}),\s(\d{2}:\d{2}:\d{2})\]\s([^:]+):\s(.*)$'

    messages = []

    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:

            clean_line = line.replace('\u200e', '').strip()

            match = re.match(pattern, clean_line)

            if match:
                date, time, sender, text = match.groups()

                messages.append({
                    'date': date,
                    'time': time[:-3],
                    'sender': sender.strip(),
                    'text': text.strip()
                })

    df = pd.DataFrame(messages)

    if not df.empty:
        df['datetime'] = pd.to_datetime(
            df['date'] + ' ' + df['time'],
            dayfirst=True
        )

        df['hour'] = df['datetime'].dt.hour
        df['day'] = df['datetime'].dt.date

    return df