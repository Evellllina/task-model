import pytest
import time
from src.task import Task
from src.exceptions import InvalidPriorityError, InvalidStatusError


def test_create_task1():
    task = Task("T001", "Тест", priority=3)
    assert task.id == "T001"

def test_create_task3():
    task = Task("T001", "Тест", priority=3)
    assert task.description == "Тест"

def test_create_task4():
    task = Task("T001", "Тест", priority=3)
    assert task.priority == 3
    assert task.status == "pending"


def test_custom_status():
    task = Task("T001", "Тест", status="in_progress")
    assert task.status == "in_progress"


def test_invalid_id():
    task = Task("T001", "Тест")
    assert task.id == "T001"


def test_invalid_priority_too_low():
    task = Task("T001", "Тест")
    with pytest.raises(InvalidPriorityError):
        task.priority = 0


def test_invalid_priority_too_high():
    task = Task("T001", "Тест")
    with pytest.raises(InvalidPriorityError):
        task.priority = 6


def test_invalid_priority_wrong_type():
    task = Task("T001", "Тест")
    with pytest.raises(InvalidPriorityError):
        task.priority = "высокий"


def test_invalid_status():
    task = Task("T001", "Тест")
    with pytest.raises(InvalidStatusError):
        task.status = "неверный"


def test_change_priority():
    task = Task("T001", "Тест", priority=3)
    task.priority = 5
    assert task.priority == 5


def test_change_description():
    task = Task("T001", "Старое")
    task.description = "Новое"
    assert task.description == "Новое"


def test_change_status():
    task = Task("T001", "Тест")
    task.status = "completed"
    assert task.status == "completed"


def test_is_ready():
    task = Task("T001", "Тест", priority=3)
    assert task.is_ready is True
    task.status = "in_progress"
    assert task.is_ready is False


def test_age_seconds():
    task = Task("T001", "Тест")
    time.sleep(0.1)
    assert task.age_seconds > 0


def test_repr():
    task = Task("T001", "Тест")
    assert "T001" in repr(task)


def test_str():
    task = Task("T001", "Тест")
    assert "T001" in str(task)
