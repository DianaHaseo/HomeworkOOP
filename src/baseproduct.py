from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс продукта."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int
    ):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        """Строковое представление продукта."""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, data: dict, products_list=None):
        """Создание продукта из словаря."""
        pass

    @property
    def price(self):
        """Возвращает цену продукта."""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Устанавливает цену продукта."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            confirm = input(
                "Цена понижается. Подтвердить? (y/n): "
            ).lower()

            if confirm != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price