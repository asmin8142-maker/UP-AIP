import warnings
from typing import Protocol
from src.spells import Spell
from src.artifacts import Artifact

# Создаем ArcaneInterface через Protocol (утиная типизация на уровне интерфейсов)
class ArcaneInterface(Protocol):
    def cast(self, caster, target) -> str: ...
    def describe(self) -> str: ...


# Класс Мага (Нитяра)
class Caster:
    def __init__(self, name: str, energy: float, artifact: Artifact = None):
        self.name = name
        self.energy = energy
        self.artifact = artifact
        self._spell_book = {}  # Приватная книга заклинаний

    def learn(self, spell: Spell):
        self._spell_book[spell.name] = spell

    def forget(self, spell_name: str):
        if spell_name in self._spell_book:
            del self._spell_book[spell_name]

    def equip(self, artifact: Artifact):
        # Если артефакт уже есть — выводим предупреждение
        if self.artifact is not None:
            warnings.warn(f"Внимание! У {self.name} уже экипирован артефакт. Старый будет заменен!")
        self.artifact = artifact

    def cast(self, spell_name: str, target: str) -> str:
        if spell_name not in self._spell_book:
            return f"{self.name} не знает заклинания {spell_name}!"
        
        spell = self._spell_book[spell_name]
        if self.energy < spell.cost:
            return f"Недостаточно энергии у {self.name} для сотворения {spell_name}!"
            
        return spell.cast(self, target)

    # Перегрузка встроенной функции len() для подсчета заклинаний
    def __len__(self) -> int:
        return len(self._spell_book)
