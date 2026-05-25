import logging
from abc import ABC

# Настройка логирования ошибок в файл error.log
logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s %(message)s'
)

class Thread:
    def __init__(self, name: str, frequency: float, stability: float):
        self._name = name
        # Приватные поля через механизм name mangling (__имя)
        self.__frequency = None
        self.__stability = None
        
        # Передаем значения через сеттеры для автоматической валидации
        self.frequency = frequency
        self.stability = stability

    @property
    def name(self) -> str:
        return self._name

    # Геттер для частоты
    @property
    def frequency(self) -> float:
        return self.__frequency

    # Сеттер для частоты с валидацией (диапазон 0.1 - 999.9)
    @frequency.setter
    def frequency(self, value: float):
        if not (0.1 <= value <= 999.9):
            msg = f"Некорректная частота {value}. Должна быть в диапазоне от 0.1 до 999.9"
            logging.error(msg)
            raise ValueError(msg)
        self.__frequency = value

    # Геттер для стабильности
    @property
    def stability(self) -> float:
        return self.__stability

    # Сеттер для стабильности с валидацией (диапазон 0.0 - 1.0)
    @stability.setter
    def stability(self, value: float):
        if not (0.0 <= value <= 1.0):
            msg = f"Некорректная стабильность {value}. Должна быть в диапазоне от 0.0 до 1.0"
            logging.error(msg)
            raise ValueError(msg)
        self.__stability = value

    def __repr__(self) -> str:
        return f"Thread('{self.name}', {self.frequency}, {self.stability})"

    def __str__(self) -> str:
        return f"Нить {self.name} (Частота: {self.frequency}, Стабильность: {self.stability})"

    # Метод резонанса (взаимодействие двух нитей)
    def resonate(self, other: 'Thread') -> float:
        return (self.frequency + other.frequency) * (self.stability * other.stability)

    # Перегрузка оператора + для слияния нитей
    def __add__(self, other: 'Thread') -> 'Thread':
        new_name = f"Слияние {self.name} и {other.name}"
        new_freq = min(999.9, max(0.1, (self.frequency + other.frequency) / 2))
        new_stab = min(1.0, max(0.0, self.stability * other.stability))
        return Thread(new_name, new_freq, new_stab)


# --- Дочерние классы нитей ---

class EnergyThread(Thread):
    def __init__(self, name: str, frequency: float, stability: float, charge: float):
        super().__init__(name, frequency, stability)
        self.charge = charge

    def resonate(self, other: Thread) -> float:
        base = super().resonate(other)
        return base * 1.2 + self.charge


class FormThread(Thread):
    def __init__(self, name: str, frequency: float, stability: float, density: float):
        super().__init__(name, frequency, stability)
        self.density = density

    def resonate(self, other: Thread) -> float:
        return super().resonate(other) * self.density


class TimeThread(Thread):
    def __init__(self, name: str, frequency: float, stability: float, dilation: float):
        super().__init__(name, frequency, stability)
        self.dilation = dilation

    def resonate(self, other: Thread) -> float:
        return super().resonate(other) + (self.dilation * 10)
