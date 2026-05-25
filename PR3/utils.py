import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def confirm(message):
    answer = input(f"{message} (y/n): ").lower()
    return answer == "y"

def progress_bar(percent, length=20):
    percent = max(0, min(100, percent))
    filled = int(length * percent / 100)
    return "[" + "#" * filled + "-" * (length - filled) + "]"

def format_bytes(size):
    for unit in ['Б', 'КБ', 'МБ', 'ГБ']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} ТБ"
