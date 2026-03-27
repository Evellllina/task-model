from datetime import datetime
from .exceptions import InvalidPriorityError, InvalidStatusError

class Task:
    """Класс задачи с валидируемыми атрибутами"""
    def __init__(self, task_id, description, priority=3, status="pending"):
        self._id = task_id
        self._description = description
        self._priority = priority
        self._status = status
        self._created_at = datetime.now()

    @property
    def id(self):
        """Уникальный идентификатор задачи"""
        return self._id

    @property
    def description(self):
        """Описание задачи"""
        return self._description

    @description.setter
    def description(self, value):
        """Установка описания с валидацией"""
        if not isinstance(value, str):
            raise InvalidPriorityError("Описание должно быть строкой")
        if not value.strip():
            raise InvalidPriorityError("Описание не может быть пустым")
        self._description = value.strip()

    @property
    def priority(self):
        """Приоритет задачи"""
        return self._priority

    @priority.setter
    def priority(self, value):
        """Установка приоритета с валидацией"""
        if not isinstance(value, int):
            raise InvalidPriorityError("Приоритет должен быть целым числом")
        if not 1 <= value <= 5:
            raise InvalidPriorityError("Приоритет должен быть от 1 до 5")
        self._priority = value

    @property
    def status(self):
        """Статус задачи"""
        return self._status

    @status.setter
    def status(self, value):
        """Установка статуса с валидацией"""
        valid = {"pending", "in_progress", "completed", "failed"}
        if not isinstance(value, str):
            raise InvalidStatusError("Статус должен быть строкой")
        if value not in valid:
            raise InvalidStatusError(f"Статус должен быть одним из {valid}")
        self._status = value

    @property
    def created_at(self):
        """Время создания задачи"""
        return self._created_at

    @property
    def is_ready(self):
        return self.status == "pending" and 1 <= self.priority <= 5

    @property
    def age_seconds(self):
        return (datetime.now() - self._created_at).total_seconds()

    def __repr__(self):
        return f"Task(id='{self.id}', description='{self.description[:30]}', priority={self.priority}, status='{self.status}')"

    def __str__(self):
        return f"Задача #{self.id}: {self.description[:50]} (приоритет={self.priority}, статус={self.status})"