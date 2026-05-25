import warnings
from src.caster import Caster
from src.spells import WeaveSpell, CutSpell, LegendaryWeaveSpell, CombinedSpell, SpellRarity, execute_all
from src.threads import EnergyThread, FormThread, TimeThread
from src.artifacts import CrystalCore, RuneMatrix

def main():
    print("--- Инициализация Нитяров ---")
    # Создание Архимага Варна и ученицы Сел
    varna = Caster("Архимаг Варн", 200.0)
    sel = Caster("Ученица Сел", 40.0)

    # Запись и вывод порядка разрешения методов (MRO)
    print(f"Порядок разрешения методов (MRO) для LegendaryWeaveSpell:\n{LegendaryWeaveSpell.__mro__}\n")

    # Демонстрация перегрузки оператора + (слияние нитей)
    print("--- Слияние Магических Нитей ---")
    t1 = EnergyThread("Нить Огня", 120.0, 0.8, charge=5.0)
    t2 = FormThread("Нить Стали", 80.0, 0.9, density=1.4)
    t_combined = t1 + t2
    print(f"Результат слияния: {t_combined}")
    print(f"Резонанс новой нити сам с собой: {t_combined.resonate(t_combined):.2f}\n")

    # Экипировка артефактов и демонстрация предупреждения (warnings)
    print("--- Экипировка Артефактов ---")
    core = CrystalCore(durability=50)
    matrix = RuneMatrix(durability=100, capacity=3)
    
    sel.equip(core)
    varna.equip(matrix)
    
    # Включаем отображение предупреждений в консоли
    warnings.simplefilter('always', UserWarning)
    print("Попытка повторной экипировки для проверки предупреждения:")
    sel.equip(core)  # Здесь Python выведет предупреждение в консоль
    print()

    # Обучение заклинаниям
    common_cut = CutSpell("Малый Разрез", 15.0, SpellRarity.COMMON, severity=0.2)
    legendary_weave = LegendaryWeaveSpell("Абсолютные Узы", 50.0, SpellRarity.LEGENDARY)
    
    sel.learn(common_cut)
    varna.learn(legendary_weave)

    # Проверка перегрузки оператора > (сравнение редкости заклинаний)
    print("--- Сравнение Силы Заклинаний ---")
    print(f"Проверка: {legendary_weave.name} > {common_cut.name} = {legendary_weave > common_cut}\n")

    # НАЧАЛО ДУЭЛИ
    print("--- НАЧАЛО МАГИЧЕСКОЙ ДУЭЛИ ---")
    print(varna.cast("Абсолютные Узы", sel.name))
    print(sel.cast("Малый Разрез", varna.name))
    print("--------------------------------\n")

    # Демонстрация Duck Typing через общую функцию
    print("--- Демонстрация Duck Typing (Утиная типизация) ---")
    mixed_spells = [common_cut, legendary_weave]
    duck_results = execute_all(mixed_spells, varna, "Тренировочный Манекен")
    for res in duck_results:
        print(res)
    print()

    # Итоговый статус персонажей
    print("--- ИТОГОВЫЙ ОТЧЕТ ДВИЖКА ---")
    for caster in [varna, sel]:
        print(f"Маг: {caster.name}")
        print(f"  Оставшаяся энергия: {caster.energy}")
        print(f"  Заклинаний в книге: {len(caster)}")
        print(f"  Прочность артефакта: {caster.artifact.durability if caster.artifact else 'Нет'}")
    print("-----------------------------")

if __name__ == "__main__":
    main()
