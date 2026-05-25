import json
import os

FILE_PATH = "users.json"

def load_users():
    """Загружает пользователей из файла users.json"""
    if not os.path.exists(FILE_PATH):
        return {}
    
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_users(users):
    """Сохраняет словарь пользователей в файл users.json"""
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

def add_transaction(username, transaction_type, amount, target_user=None):
    """Записывает трансляцию в персональный JSON-файл пользователя внутри папки transactions"""
    os.makedirs("transactions", exist_ok=True)
    file_path = f"transactions/{username}.json"
    
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                history = json.load(file)
            except json.JSONDecodeError:
                history = []
    else:
        history = []
        
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data = {
        "type": transaction_type,
        "amount": amount,
        "date": timestamp
    }
    if target_user:
        data["to_user"] = target_user
        
    history.append(data)
    
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)
