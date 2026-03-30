class TaskValidationError(Exception):
    """Базовое исключение для ошибок валидации задачи"""
    pass

class InvalidPriorityError(TaskValidationError):
    """Исключение при неверном значении приоритета"""
    pass

class InvalidStatusError(TaskValidationError):
    """Исключение при неверном значении статуса"""
    pass

class ImmutableAttributeError(TaskValidationError):
    """Исключение при попытке изменить неизменяемый атрибут"""
    pass
