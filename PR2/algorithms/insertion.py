# algorithms/insertion.py

def insertion_sort(array, draw_func):
    """
    Сортировка вставками с визуализацией каждого сравнения и сдвига.
    :param array: Исходный массив (копия будет сортироваться)
    :param draw_func: Функция отрисовки draw из модуля visualizer
    :return: Итоговое количество шагов (сравнений)
    """
    arr = list(array)
    n = len(arr)
    step_count = 0
    
    # В этой сортировке левая часть постоянно перестраивается, поэтому 
    # мы будем считать элементы «зелеными» только в самом конце алгоритма,
    # либо условно подсвечивать уже обработанную левую часть. 
    # Сделаем подсветку финальной в самом конце, чтобы не путать, так как элементы слева еще могут двигаться.
    
    for i in range(1, n):
        key = arr[i]  # Элемент, который мы будем вставлять
        j = i - 1
        
        # Пока не дошли до начала массива и текущий элемент больше, чем key
        while j >= 0:
            step_count += 1
            
            # Подсвечиваем красным элемент, который двигаем (j+1), и тот, с которым сравниваем (j)
            draw_func(arr, comparing=[j, j + 1], sorted_indices=list(range(i)),
                      title="Сортировка вставками (Insertion Sort)", step_count=step_count)
            
            if arr[j] > key:
                arr[j + 1] = arr[j]  # Сдвигаем элемент вправо
                j -= 1
                
                # Показываем массив сразу после сдвига
                draw_func(arr, comparing=[j + 1], sorted_indices=list(range(i)),
                          title="Сортировка вставками — Сдвиг элементов", step_count=step_count)
            else:
                break
                
        arr[j + 1] = key  # Вставляем элемент на его место
        
    # В конце помечаем весь массив зеленым
    draw_func(arr, comparing=[], sorted_indices=list(range(n)),
              title="Сортировка вставками — Готово!", step_count=step_count)
              
    return step_count
