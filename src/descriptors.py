from .exceptions import ImmutableAttributeError

class ValidatedDescriptor:
    """Data descriptor для валидации"""
    def __init__(self, validator, immutable=False):
        self.validator = validator
        self.immutable = immutable
        self.data = {}

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self.data.get(id(obj))

    def __set__(self, obj, value):
        if self.immutable and id(obj) in self.data:
            raise ImmutableAttributeError("Нельзя изменить неизменяемый атрибут")
        self.data[id(obj)] = self.validator(value)

    def __delete__(self, obj):
        raise AttributeError("Нельзя удалить атрибут")


class ReadOnlyProperty:
    """Non-data descriptor"""
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self.getter(obj)
