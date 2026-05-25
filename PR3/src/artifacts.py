from abc import ABC, abstractmethod
from src.threads import Thread

# Абстрактный класс Артефакта
class Artifact(ABC):
    def __init__(self, durability: int):
        self._durability = durability  # Приватная прочность

    @property
    def durability(self) -> int:
        return self._durability

    @abstractmethod
    def activate(self, thread: Thread) -> float:
        pass


# Конкретный артефакт: Кристальное Ядро
class CrystalCore(Artifact):
    def activate(self, thread: Thread) -> float:
        self._durability -= 2  # Каждое использование тратит 2 единицы прочности
        return thread.frequency * 1.5


# Конкретный артефакт: Руническая Матрица
class RuneMatrix(Artifact):
    def __init__(self, durability: int, capacity: int):
        super().__init__(durability)
        self.capacity = capacity
        self.threads = []  # Хранилище для нитей

    def store(self, thread: Thread):
        if len(self.threads) < self.capacity:
            self.threads.append(thread)

    def activate(self, thread: Thread) -> float:
        self._durability -= 1
        # Суммируем частоты всех сохраненных нитей и текущей
        total_energy = sum(t.frequency for t in self.threads) + thread.frequency
        return total_energy
