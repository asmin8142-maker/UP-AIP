# stats.py

def print_statistics(n, results):
    """
    Выводит итоговую сравнительную таблицу в консоль.
    :param n: Количество элементов в массиве
    :param results: Словарь вида {"Название алгоритма": количество_шагов}
    """
    print("\n" + "=" * 44)
    print(f"Сравнение алгоритмов (N = {n})")
    print("=" * 44)
    print(f"{'Алгоритм':<25} {'Шагов (сравнений)':<15}")
    print("-" * 44)
    
    for algo_name, steps in results.items():
        print(f"{algo_name:<25} {steps:<15}")
        
    print("=" * 44)
    
    # Находим алгоритм с минимальным количеством шагов
    winner = min(results, key=results.get)
    print(f"Победитель по шагам: {winner}")
    print("=" * 44 + "\n")
