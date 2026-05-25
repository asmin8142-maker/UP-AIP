from abc import ABC, abstractmethod
from enum import Enum
from typing import List

# Перечисление для редкости заклинаний
class SpellRarity(Enum):
    COMMON = "Обычное"
    RARE = "Редкое"
    LEGENDARY = "Легендарное"


# Абстрактный базовый класс заклинания
class Spell(ABC):
    def __init__(self, name: str, cost: float, rarity: SpellRarity):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    # Абстрактный метод каста (должен быть реализован у всех потомков)
    @abstractmethod
    def cast(self, caster, target) -> str:
        pass

    # Абстрактный метод описания
    @abstractmethod
    def describe(self) -> str:
        pass

    # Перегрузка оператора > для сравнения заклинаний по редкости
    def __gt__(self, other: 'Spell') -> bool:
        rarity_weights = {SpellRarity.COMMON: 1, SpellRarity.RARE: 2, SpellRarity.LEGENDARY: 3}
        return rarity_weights[self.rarity] > rarity_weights[other.rarity]


# Конкретное заклинание: Создание связи
class WeaveSpell(Spell):
    def cast(self, caster, target) -> str:
        caster.energy -= self.cost
        return f"[{self.name}] {caster.name} ткёт новую связь с {target}. Затрачено энергии: {self.cost}."

    def describe(self) -> str:
        return f"Заклинание связи '{self.name}' ({self.rarity.value})"


# Конкретное заклинание: Разрез нитей
class CutSpell(Spell):
    def __init__(self, name: str, cost: float, rarity: SpellRarity, severity: float):
        super().__init__(name, cost, rarity)  # Вызов конструктора родителя
        self.severity = severity

    def cast(self, caster, target) -> str:
        caster.energy -= self.cost
        return f"[{self.name}] {caster.name} разрезает нити {target}, снижая стабильность на {self.severity}."

    def describe(self) -> str:
        return f"Разрушающее заклинание '{self.name}' с силой {self.severity}"


# Конкретное заклинание: Оковы
class BindSpell(Spell):
    def cast(self, caster, target) -> str:
        caster.energy -= self.cost
        return f"[{self.name}] {caster.name} накладывает постоянные оковы на {target}."

    def describe(self) -> str:
        return f"Удерживающее заклинание '{self.name}'"


# Легендарное заклинание (наследует WeaveSpell и расширяет его через super().cast())
class LegendaryWeaveSpell(WeaveSpell):
    def cast(self, caster, target) -> str:
        base_effect = super().cast(caster, target)
        return f"{base_effect} Древняя магия удваивает прочность созданной нити!"


# Комбинированное заклинание (Паттерн Компоновщик / Composite)
class CombinedSpell(Spell):
    def __init__(self, name: str, spells: List[Spell]):
        total_cost = sum(s.cost for s in spells)
        super().__init__(name, total_cost, SpellRarity.LEGENDARY)
        self.spells = spells

    def cast(self, caster, target) -> str:
        results = []
        for spell in self.spells:
            results.append(spell.cast(caster, target))
        return " -> ".join(results)

    def describe(self) -> str:
        return f"Комбинированное плетение '{self.name}' из {len(self.spells)} заклинаний."


# Функция демонстрации Duck Typing
def execute_all(spells_list, caster, target) -> List[str]:
    """Принимает любой список объектов с методом cast() и вызывает его"""
    results = []
    for spell in spells_list:
        results.append(spell.cast(caster, target))
    return results
