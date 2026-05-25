# visualizer.py
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Твоя красивая цветовая гамма
COLOR_DEFAULT = '#0088FF'
COLOR_COMPARE = '#FF3333'
COLOR_SORTED  = '#00CC44'

# Настройка стильного темного окна
fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor('#0a0a0f')
ax.set_facecolor('#13131c')
plt.tight_layout(pad=2)

# Переменная для пропуска кадров
_frame = 0

def draw(array, comparing=[], sorted_indices=[], title="", step_count=0):
    global _frame
    _frame += 1
    
    n = len(array)
    
    # ПРОВЕРКА НА ФИНАЛ: Если отсортированы все элементы, 
    # то пропускать кадр нельзя — нужно обязательно показать финал!
    is_final = len(sorted_indices) >= n - 1 or len(sorted_indices) == n
    
    # Ускорение: отрисовываем только каждый 3-й шаг алгоритма (кроме финала)
    if _frame % 10 != 0 and not is_final:
        return

    # Очищаем холст для нового шага
    ax.cla()
    ax.set_facecolor('#13131c')

    colors = []
    for i in range(n):
        # Если это финал, красим абсолютно всё в жёлтый цвет
        if is_final:
            colors.append(COLOR_SORTED)
        elif i in comparing:
            colors.append(COLOR_COMPARE)
        elif i in sorted_indices:
            colors.append(COLOR_SORTED)
        else:
            colors.append(COLOR_DEFAULT)

    # Рисуем столбцы без рамок
    bars = ax.bar(range(n), array, color=colors, width=0.8, edgecolor='none')

    # Красивые цифры над столбцами (только если элементов мало)
    if n <= 30:
        for i, (bar, val) in enumerate(zip(bars, array)):
            if is_final:
                color = COLOR_SORTED
            else:
                color = COLOR_COMPARE if i in comparing else (COLOR_SORTED if i in sorted_indices else '#aaaacc')
                
            ax.text(bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + max(array) * 0.01,
                    str(val),
                    ha='center', va='bottom',
                    fontsize=max(6, 11 - n // 5),
                    color=color,
                    fontfamily='monospace')

    # Настройки заголовка и осей
    ax.set_title(f'{title}   |   шагов: {step_count}',
                 color='#e8e8f0', fontsize=13, fontweight='bold', pad=10)
    ax.set_xlim(-0.5, n - 0.5)
    ax.set_ylim(0, max(array) * 1.15)
    ax.tick_params(colors='#6060a0')
    ax.set_xticks([])
    
    # Прячем границы рамки окна
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Твоя крутая легенда
    patches = [
        mpatches.Patch(color=COLOR_DEFAULT, label='Обычный'),
        mpatches.Patch(color=COLOR_COMPARE, label='Сравниваются'),
        mpatches.Patch(color=COLOR_SORTED,  label='На своём месте'),
    ]
    ax.legend(handles=patches, loc='upper right',
              facecolor='#1a1a28', edgecolor='#333355',
              labelcolor='#e8e8f0', fontsize=9)

    # Небольшая пауза, чтобы зафиксировать картинку
    plt.pause(0.001)
