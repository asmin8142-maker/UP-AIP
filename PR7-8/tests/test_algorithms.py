import pytest
from unittest.mock import patch, MagicMock
from src.threads import Thread, EnergyThread
from src.caster import Caster
from src.artifacts import CrystalCore, RuneMatrix
from src.spells import WeaveSpell, CutSpell, BindSpell, LegendaryWeaveSpell, CombinedSpell, SpellRarity, execute_all

# --- 1. Базовые тесты: Проверка нитей (Happy Path) ---

def test_thread_correct_assignment():
    t = Thread("Тестовая Нить", 500.0, 0.5)
    assert t.frequency == 500.0
    assert t.stability == 0.5
    assert repr(t) == "Thread('Тестовая Нить', 500.0, 0.5)"
    assert "Нить Тестовая Нить" in str(t)

def test_thread_addition_operator():
    t1 = Thread("Нить А", 100.0, 0.8)
    t2 = Thread("Нить Б", 200.0, 0.5)
    t3 = t1 + t2
    assert t3.frequency == 150.0
    assert t3.stability == 0.4

def test_child_threads_resonance():
    et = EnergyThread("Огонь", 100.0, 0.5, charge=5.0)
    assert et.resonate(et) == (100.0 + 100.0) * (0.5 * 0.5) * 1.2 + 5.0


# --- 2. Граничные случаи и валидация (ValueError) ---

def test_thread_raises_value_error_on_invalid_frequency():
    with pytest.raises(ValueError):
        Thread("Сбой Частоты", 1000.0, 0.5)
    with pytest.raises(ValueError):
        Thread("Сбой Частоты", 0.0, 0.5)

def test_thread_raises_value_error_on_invalid_stability():
    with pytest.raises(ValueError):
        Thread("Сбой Стабильности", 100.0, 1.5)
    with pytest.raises(ValueError):
        Thread("Сбой Стабильности", 100.0, -0.1)


# --- 3. Логирование ошибок (caplog) ---

def test_logging_creates_error_log(caplog):
    with pytest.raises(ValueError):
        Thread("Тест Лога", 2000.0, 0.5)
    assert any("Некорректная частота" in record.message for record in caplog.records)


# --- 4. Тесты для Заклинаний (spells.py) ---

def test_spell_rarity_comparison():
    common = CutSpell("Разрез", 10.0, SpellRarity.COMMON, severity=0.1)
    legendary = LegendaryWeaveSpell("Узы", 40.0, SpellRarity.LEGENDARY)
    assert legendary > common

def test_weave_and_cut_spells():
    caster = Caster("Маг", 100.0)
    weave = WeaveSpell("Связь", 20.0, SpellRarity.COMMON)
    cut = CutSpell("Разрез", 15.0, SpellRarity.RARE, severity=0.5)
    
    assert "ткёт новую связь" in weave.cast(caster, "Цель")
    assert caster.energy == 80.0
    assert "Разрушающее заклинание" in cut.describe()


# --- ИСПРАВЛЕННЫЙ ТЕСТ ДЛЯ КОМБО-ЗАКЛИНАНИЙ ---
def test_bind_and_combined_spells():
    caster = Caster("Маг", 100.0)
    b = BindSpell("Оковы", 10.0, SpellRarity.COMMON)
    
    # 1. Проверяем одиночное заклинание
    assert "накладывает постоянные оковы" in b.cast(caster, "Цель")
    assert caster.energy == 90.0  # Было 100, потратили 10
    assert "Удерживающее заклинание" in b.describe()
    
    # 2. Проверяем комбинированное заклинание
    combined = CombinedSpell("Комбо", [b, b])
    assert combined.cost == 20.0  # Стоимость сложилась верно
    
    # Запускаем само заклинание, чтобы оно потратило энергию
    assert "накладывает постоянные оковы" in combined.cast(caster, "Цель")
    assert caster.energy == 70.0  # Было 90, вычли еще 20 за комбо
    assert "Комбинированное плетение" in combined.describe()


# --- 5. Тесты для Кастера и Артефактов (caster.py / artifacts.py) ---

def test_caster_book_and_casting():
    caster = Caster("Ученик", 30.0)
    spell = WeaveSpell("Связь", 20.0, SpellRarity.COMMON)
    
    caster.learn(spell)
    assert len(caster) == 1
    
    assert "ткёт новую связь" in caster.cast("Связь", "Враг")
    assert caster.cast("Неизвестное", "Враг") == "Ученик не знает заклинания Неизвестное!"
    assert "Недостаточно энергии" in caster.cast("Связь", "Враг")
    
    caster.forget("Связь")
    assert len(caster) == 0

def test_artifacts_logic():
    t = Thread("Нить", 100.0, 0.8)
    core = CrystalCore(durability=10)
    assert core.activate(t) == 150.0
    assert core.durability == 8
    
    matrix = RuneMatrix(durability=20, capacity=2)
    matrix.store(t)
    assert matrix.activate(t) == 200.0


# --- 6. Использование Моков (unittest.mock) ---

def test_artifact_activation_with_patch():
    with patch('src.artifacts.CrystalCore.activate') as mock_activate:
        mock_activate.return_value = 99.9
        core = CrystalCore(durability=10)
        t = Thread("Эфир", 100.0, 0.5)
        assert core.activate(t) == 99.9
        mock_activate.assert_called_once_with(t)

def test_caster_with_magic_mock():
    caster = Caster("Варн", 100.0)
    mock_artifact = MagicMock()
    caster.equip(mock_artifact)
    assert caster.artifact == mock_artifact

def test_mock_side_effect():
    mock_obj = MagicMock()
    mock_obj.activate.side_effect = RuntimeError("Критический сбой")
    with pytest.raises(RuntimeError):
        mock_obj.activate()
