from src.baseproduct import BaseProduct
from src.mixin import ProductMixin


class Product(ProductMixin, BaseProduct):
    """Базовый класс продукта."""

    def __str__(self):
        return (
            f"{self.name}, {self.price} руб. "
            f"Остаток: {self.quantity} шт."
        )

    def __add__(self, other):
        """Сложение продуктов одного типа."""

        if type(self) is type(other):
            return (
                self.price * self.quantity
                + other.price * other.quantity
            )

        raise TypeError(
            "Можно складывать только товары одного типа"
        )

    @classmethod
    def new_product(cls, data: dict, products_list=None):
        """Создание продукта из словаря."""

        name = data["name"]

        if products_list:
            for existing in products_list:
                if existing.name == name:
                    new_price = max(
                        existing.price,
                        data["price"]
                    )

                    existing.quantity += data["quantity"]
                    existing.price = new_price

                    return existing

        return cls(
            data["name"],
            data["description"],
            data["price"],
            data["quantity"]
        )