import hashlib
import re

from storage import load_users, save_users


# Хэширование пароля
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Проверка пароля
def check_password(input_password, stored_hash):
    return hash_password(input_password) == stored_hash


# Регистрация
def register():
    users = load_users()

    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    # Проверка логина
    if len(login) < 3:
        print("Логин слишком короткий")
        return

    if not re.match("^[a-zA-Z0-9]+$", login):
        print("Логин должен содержать только латинские буквы и цифры")
        return

    if login in users:
        print("Такой пользователь уже существует")
        return

    # Проверка пароля
    if len(password) < 6:
        print("Пароль должен быть не менее 6 символов")
        return

    # Создание пользователя
    users[login] = {
        "password_hash": hash_password(password),
        "balance": 0.0,
        "blocked": False,
        "failed_attempts": 0
    }

    save_users(users)

    print("Регистрация успешна!")


# Авторизация
def login():
    users = load_users()

    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    # Проверка существования
    if login not in users:
        print("Пользователь не найден")
        return None

    user = users[login]

    # Проверка блокировки
    if user["blocked"]:
        print("Аккаунт заблокирован")
        return None

    # Проверка пароля
    if check_password(password, user["password_hash"]):

        user["failed_attempts"] = 0
        save_users(users)

        print("Вход выполнен!")
        return login

    else:
        user["failed_attempts"] += 1

        attempts_left = 3 - user["failed_attempts"]

        if user["failed_attempts"] >= 3:
            user["blocked"] = True
            print("Аккаунт заблокирован!")

        else:
            print(f"Неверный пароль. Осталось попыток: {attempts_left}")

        save_users(users)
        return None
