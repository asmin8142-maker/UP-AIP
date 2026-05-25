import json
import os

def show_transaction_history(username):
    """Выводит на экран всю историю операций пользователя"""
    file_path = f"transactions/{username}.json"
    
    print(f"\n=== ИСТОРИЯ ОПЕРАЦИЙ ПОЛЬЗОВАТЕЛЯ [{username}] ===")
    
    if not os.path.exists(file_path):
        print("История операций пуста.")
        return
        
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            history = json.load(file)
        except json.JSONDecodeError:
            print("Ошибка чтения файла истории.")
            return
            
    if not history:
        print("Операций пока не зафиксировано.")
        return
        
    # Переводим типы транзакций на понятный язык
    types_dict = {
        "deposit": "Пополнение",
        "withdraw": "Снятие",
        "transfer_out": "Перевод (исходящий)",
        "transfer_in": "Перевод (входящий)"
    }
    
    for tx in history:
        tx_type = types_dict.get(tx["type"], tx["type"])
        amount = tx["amount"]
        date = tx["date"]
        
        info = f"[{date}] {tx_type}: {amount:.2f} тенге."
        if "to_user" in tx:
            info += f" (Участник: {tx['to_user']})"
            
        print(info)
    print("==================================================")
