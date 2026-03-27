from .exceptions import ImmutableAttributeError

class ValidatedDescriptor:
    """Дескриптор для валидации атрибутов"""
    def __init__(self, validator, immutable=False):
        self.validator = validator
        self.immutable = immutable
        self.data = {}

    def __get__(self, obj, objtype=None):
        """Возвращает значение атрибута"""
        if obj is None:
            return self
        return self.data.get(id(obj))

    def __set__(self, obj, value):
        """Устанавливает значение с валидацией"""
        if self.immutable and id(obj) in self.data:
            raise ImmutableAttributeError("Нельзя изменить неизменяемый атрибут")
        self.data[id(obj)] = self.validator(value)

    def __delete__(self, obj):
        """Запрещает удаление атрибута"""
        raise AttributeError("Нельзя удалить атрибут")


class ReadOnlyProperty:
    """Дескриптор для read-only свойств"""
    def __init__(self, getter):
        self.getter = getter
        self.data = {}

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        obj_id = id(obj)
        if obj_id not in self.data:
            self.data[obj_id] = self.getter(obj)
        return self.data[obj_id]

    def __set__(self, obj, value):
        raise ImmutableAttributeError("Read-only свойство нельзя изменить")

    def __delete__(self, obj):
        raise ImmutableAttributeError("Read-only свойство нельзя удалить")
