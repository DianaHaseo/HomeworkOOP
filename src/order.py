from src.baseentity import BaseEntity
from src.exceptions import ZeroQuantityError


class Order(BaseEntity):
    """Заказ одного товара."""

    def __init__(
        self,
        name,
        description,
        product,
        quantity
    ):
        super().__init__(name, description)

        try:
            if quantity == 0:
                raise ZeroQuantityError(
                    "Товар с нулевым количеством "
                    "не может быть добавлен в заказ"
                )

        except ZeroQuantityError as error:
            print(f"Ошибка: {error}")
            raise

        else:
            self.product = product
            self.quantity = quantity
            self.total_price = product.price * quantity

            print("Товар успешно добавлен в заказ")

        finally:
            print("Обработка добавления товара завершена")

    def __str__(self):
        return (
            f"Заказ: {self.name}, "
            f"товар: {self.product.name}, "
            f"количество: {self.quantity} шт., "
            f"итого: {self.total_price} руб."
        )