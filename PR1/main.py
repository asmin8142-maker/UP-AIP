from auth import register, login
from account import deposit, withdraw, transfer
from report import show_transaction_history

def account_menu(username):
    while True:
        print(f"\n=== Меню аккаунта [{username}] ===")
        print("1. Пополнить счёт")
        print("2. Снять средства")
        print("3. Перевести другому пользователю")
        print("4. Посмотреть историю операций")
        print("0. Выйти из аккаунта")
        
        choice = input("Выберите пункт: ")
        
        if choice == "1":
            deposit(username)
        elif choice == "2":
            withdraw(username)
        elif choice == "3":
            transfer(username)
        elif choice == "4":
            show_transaction_history(username)
        elif choice == "0":
            print("Выход из аккаунта выполнен.")
            break
        else:
            print("Неверный пункт меню")

def main():
    while True:
        print("\n=== Консольный Банк ===")
        print("1. Войти")
        print("2. Регистрация")
        print("0. Выход")
        
        choice = input("Выберите пункт: ")
        
        if choice == "1":
            username = login()
            if username:
                account_menu(username)
        elif choice == "2":
            register()
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Неверный пункт меню")

if __name__ == "__main__":
    main()
