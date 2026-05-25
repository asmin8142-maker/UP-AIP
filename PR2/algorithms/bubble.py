# algorithms/bubble.py

def bubble_sort(array, draw_func):
    """
    Сортировка пузырьком с визуализацией каждого сравнения.
    :param array: Исходный массив (копия будет сортироваться)
    :param draw_func: Функция отрисовки draw из модуля visualizer
    :return: Итоговое количество шагов (сравнений)
    """
    # Делаем копию массива, чтобы не испортить оригинальный для других алгоритмов
    arr = list(array)
    n = len(arr)
    step_count = 0
    
    # Храним индексы гарантированно отсортированных элементов
    sorted_indices = []
    
    # Главный цикл алгоритма
    for i in range(n):
        swapped = False
        
        # Внутренний цикл: сравниваем соседние элементы
        # С каждым проходом i элементов "всплывают" в конец, поэтому n - i - 1
        for j in range(0, n - i - 1):
            step_count += 1
            
            # Вызываем визуализатор: подсвечиваем красным элементы j и j+1, которые сравниваем
            draw_func(arr, comparing=[j, j + 1], sorted_indices=sorted_indices, 
                      title="Сортировка пузырьком (Bubble Sort)", step_count=step_count)
            
            # Если левый элемент больше правого — меняем их местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
                # Показываем состояние СРАЗУ после перестановки
                draw_func(arr, comparing=[j, j + 1], sorted_indices=sorted_indices, 
                          title="Сортировка пузырьком (Bubble Sort)", step_count=step_count)
        
        # Элемент на позиции (n - i - 1) встал на свое финальное место
        sorted_indices.append(n - i - 1)
        
        # Если за весь проход не было ни одной перестановки, массив уже отсортирован
        if not swapped:
            # Все оставшиеся элементы тоже считаются отсортированными
            for k in range(n):
                if k not in sorted_indices:
                    sorted_indices.append(k)
            break
            
    # Финальный кадр: показываем полностью зеленый (отсортированный) массив
    draw_func(arr, comparing=[], sorted_indices=sorted_indices, 
              title="Сортировка пузырьком — Готово!", step_count=step_count)
    
    return step_count
