from src.baseentity import BaseEntity
from src.order import Order
from src.product import Product


class TestOrder:
    """Тесты класса Order."""

    def test_order_init(self):
        """Создание заказа."""
        product = Product(
            "Телефон",
            "Смартфон",
            50000,
            10
        )

        order = Order(
            "Заказ №1",
            "Покупка телефона",
            product,
            2
        )

        assert order.name == "Заказ №1"
        assert order.description == "Покупка телефона"
        assert order.product is product
        assert order.quantity == 2
        assert order.total_price == 100000

    def test_order_str(self):
        """Строковое представление заказа."""
        product = Product(
            "Телефон",
            "Смартфон",
            50000,
            10
        )

        order = Order(
            "Заказ №1",
            "Покупка телефона",
            product,
            2
        )

        result = str(order)

        assert "Заказ №1" in result
        assert "Телефон" in result
        assert "2 шт." in result
        assert "100000 руб." in result

    def test_order_inherits_base_entity(self):
        """Order наследует BaseEntity."""
        assert issubclass(Order, BaseEntity)