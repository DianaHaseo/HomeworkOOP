from abc import ABC, abstractmethod


class BaseEntity(ABC):
    """Общий абстрактный класс для сущностей магазина."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self):
        """Возвращает строковое представление объекта."""
        pass