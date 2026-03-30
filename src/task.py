from datetime import datetime
from .exceptions import InvalidPriorityError, InvalidStatusError, TaskValidationError
from .descriptors import ValidatedDescriptor, ReadOnlyProperty


class Task:
    """Класс задачи с валидируемыми атрибутами"""

    @staticmethod
    def _validate_priority(value):
        if not isinstance(value, int):
            raise InvalidPriorityError("Приоритет должен быть целым числом")
        if not 1 <= value <= 5:
            raise InvalidPriorityError("Приоритет должен быть от 1 до 5")
        return value

    @staticmethod
    def _validate_status(value):
        valid = {"pending", "in_progress", "completed", "failed"}
        if not isinstance(value, str):
            raise InvalidStatusError("Статус должен быть строкой")
        if value not in valid:
            raise InvalidStatusError(f"Статус должен быть одним из {valid}")
        return value

    @staticmethod
    def _validate_description(value):
        if not isinstance(value, str):
            raise InvalidPriorityError("Описание должно быть строкой")
        if not value.strip():
            raise InvalidPriorityError("Описание не может быть пустым")
        return value.strip()

    @staticmethod
    def _validate_id(value):
        if not isinstance(value, str):
            raise TaskValidationError("ID должен быть строкой")
        if not value.strip():
            raise TaskValidationError("ID не может быть пустым")
        return value.strip()

    # Data descriptors
    priority = ValidatedDescriptor(_validate_priority, immutable=False)
    status = ValidatedDescriptor(_validate_status, immutable=False)
    description = ValidatedDescriptor(_validate_description, immutable=False)
    _id = ValidatedDescriptor(_validate_id, immutable=False)  # ← убрал immutable

    # Non-data descriptors (без кэша)
    is_ready = ReadOnlyProperty(lambda self: self.status == "pending" and 1 <= self.priority <= 5)
    age_seconds = ReadOnlyProperty(lambda self: (datetime.now() - self._created_at).total_seconds())

    @property
    def id(self):
        """Уникальный идентификатор задачи"""
        return self._id

    @property
    def created_at(self):
        """Время создания задачи"""
        return self._created_at

    def __init__(self, task_id, description, priority=3, status="pending"):
        self._id = task_id
        self.description = description
        self.priority = priority
        self.status = status
        self._created_at = datetime.now()

    def __repr__(self):
        return f"Task(id='{self.id}', description='{self.description[:30]}', priority={self.priority}, status='{self.status}')"

    def __str__(self):
        return f"Задача #{self.id}: {self.description[:50]} (приоритет={self.priority}, статус={self.status})"
