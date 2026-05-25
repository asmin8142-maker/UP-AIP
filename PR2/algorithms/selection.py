# algorithms/selection.py

def selection_sort(array, draw_func):
    """
    Сортировка выбором с визуализацией каждого сравнения.
    :param array: Исходный массив (копия будет сортироваться)
    :param draw_func: Функция отрисовки draw из модуля visualizer
    :return: Итоговое количество шагов (сравнений)
    """
    arr = list(array)
    n = len(arr)
    step_count = 0
    
    # Список индексов, которые уже встали на свои финальные места
    sorted_indices = []
    
    # Двигаем границу неотсортированной части массива
    for i in range(n):
        min_idx = i  # Предполагаем, что первый элемент — минимальный
        
        for j in range(i + 1, n):
            step_count += 1
            
            # Подсвечиваем красным текущего «кандидата на минимум» (min_idx) и элемент, с которым сравниваем (j)
            draw_func(arr, comparing=[min_idx, j], sorted_indices=sorted_indices,
                      title="Сортировка выбором (Selection Sort)", step_count=step_count)
            
            if arr[j] < arr[min_idx]:
                min_idx = j
                # Показываем новый найденный минимум
                draw_func(arr, comparing=[min_idx], sorted_indices=sorted_indices,
                          title="Сортировка выбором (Selection Sort)", step_count=step_count)
        
        # Если нашли элемент меньше, чем arr[i], меняем их местами
        if min_idx != i:
            # Отдельно подсвечиваем перестановку перед её совершением
            draw_func(arr, comparing=[i, min_idx], sorted_indices=sorted_indices,
                      title="Сортировка выбором — Перестановка!", step_count=step_count)
            
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
        # Элемент встал на своё окончательное место
        sorted_indices.append(i)
        
    # Финальный кадр: всё отсортировано
    draw_func(arr, comparing=[], sorted_indices=sorted_indices,
              title="Сортировка выбором — Готово!", step_count=step_count)
              
    return step_count
