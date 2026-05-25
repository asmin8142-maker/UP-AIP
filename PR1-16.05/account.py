from datetime import datetime
from storage import (
    load_users,
    save_users,
    add_transaction
)

def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def deposit(username):
    """Пополнение счёта"""
    users = load_users()
    try:
        amount = float(input("Введите сумму пополнения: "))
        if amount <= 0:
            print("Сумма должна быть больше нуля")
            return
        
        users[username]["balance"] += amount
        save_users(users)
        add_transaction(username, "deposit", amount)
        print(f"Баланс пополнен. Новый баланс: {users[username]['balance']:.2f}")
    except ValueError:
        print("Ошибка ввода! Введите число.")

def withdraw(username):
    """Снятие средств"""
    users = load_users()
    try:
        amount = float(input("Введите сумму снятия: "))
        if amount <= 0:
            print("Сумма должна быть больше нуля")
            return
        if users[username]["balance"] < amount:
            print("Недостаточно средств на счете!")
            return
            
        users[username]["balance"] -= amount
        save_users(users)
        add_transaction(username, "withdraw", amount)
        print(f"Снятие выполнено. Новый баланс: {users[username]['balance']:.2f}")
    except ValueError:
        print("Ошибка ввода! Введите число.")

def transfer(username):
    """Перевод другому пользователю"""
    users = load_users()
    target_user = input("Введите логин получателя: ")
    
    if target_user not in users:
        print("Пользователь не найден!")
        return
    if target_user == username:
        print("Нельзя переводить деньги самому себе!")
        return
        
    try:
        amount = float(input("Введите сумму перевода: "))
        if amount <= 0:
            print("Сумма должна быть больше нуля")
            return
        if users[username]["balance"] < amount:
            print("Недостаточно средств для перевода!")
            return
            
        users[username]["balance"] -= amount
        users[target_user]["balance"] += amount
        
        save_users(users)
        add_transaction(username, "transfer_out", amount, target_user=target_user)
        add_transaction(target_user, "transfer_in", amount, target_user=username)
        print("Перевод выполнен.")
    except ValueError:
        print("Ошибка ввода! Введите число.")
