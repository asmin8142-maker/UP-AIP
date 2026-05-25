# main.py
import random
import matplotlib.pyplot as plt

# Импортируем модули проекта
from stats import print_statistics 
import visualizer  
from algorithms.bubble import bubble_sort
from algorithms.selection import selection_sort
from algorithms.insertion import insertion_sort

def get_elements_count():
    while True:
        try:
            user_input = input("Введите количество элементов N (от 2 до 100): ")
            n = int(user_input)
            if 2 <= n <= 100:
                return n
            else:
                print("Ошибка: Число должно быть в диапазоне от 2 до 100. Попробуйте снова.")
        except ValueError:
            print("Ошибка: Вы ввели не целое число. Попробуйте снова.")

def get_algorithm_choice():
    while True:
        print("\nДоступные алгоритмы:")
        print("1. Сортировка пузырьком (Bubble Sort)")
        print("2. Сортировка выбором (Selection Sort)")
        print("3. Сортировка вставками (Insertion Sort)")
        print("4. Запустить все три по очереди")
        
        choice = input("Выберите пункт меню (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        print("Ошибка: Неверный выбор. Введите цифру от 1 до 4.")

def main():
    print("=== Добро пожаловать в программу визуализации сортировок! ===")
    
    n = get_elements_count()
    choice = get_algorithm_choice()
    
    original_array = [random.randint(1, 100) for _ in range(n)]
    results = {}
    
    plt.ion()
    
    # Запуск алгоритмов
    if choice == '1' or choice == '4':
        visualizer._frame = 0  # Сбрасываем счетчик кадров перед стартом
        print("\nЗапуск Сортировки пузырьком...")
        steps = bubble_sort(original_array, visualizer.draw)
        results["Сортировка пузырьком"] = steps
        if choice == '4': plt.pause(1)
            
    if choice == '2' or choice == '4':
        visualizer._frame = 0  # Сбрасываем счетчик кадров перед стартом
        print("\nЗапуск Сортировки выбором...")
        steps = selection_sort(original_array, visualizer.draw)
        results["Сортировка выбором"] = steps
        if choice == '4': plt.pause(1)
            
    if choice == '3' or choice == '4':
        visualizer._frame = 0  # Сбрасываем счетчик кадров перед стартом
        print("\nЗапуск Сортировки вставками...")
        steps = insertion_sort(original_array, visualizer.draw)
        results["Сортировка вставками"] = steps

    plt.ioff()
    plt.close()
    
    print_statistics(n, results)

if __name__ == "__main__":
    main()
