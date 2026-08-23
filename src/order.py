from src.baseentity import BaseEntity

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

        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self):
        return (
            f"Заказ: {self.name}, "
            f"товар: {self.product.name}, "
            f"количество: {self.quantity} шт., "
            f"итого: {self.total_price} руб."
        )