import pytest

from src.baseentity import BaseEntity
from src.exceptions import ZeroQuantityError
from src.order import Order
from src.product import Product


class TestOrder:

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

        assert issubclass(
            Order,
            BaseEntity
        )


class TestOrderZeroQuantity:

    def test_zero_quantity_raises_custom_error(self):
        """Нулевое количество вызывает пользовательское исключение."""

        product = Product(
            "Телефон",
            "Смартфон",
            50000,
            10
        )

        with pytest.raises(
            ZeroQuantityError
        ):
            Order(
                "Заказ №1",
                "Покупка телефона",
                product,
                0
            )

    def test_zero_quantity_error_message(
        self,
        capsys
    ):
        """Проверка сообщения об ошибке."""

        product = Product(
            "Телефон",
            "Смартфон",
            50000,
            10
        )

        with pytest.raises(
            ZeroQuantityError
        ):
            Order(
                "Заказ №1",
                "Покупка телефона",
                product,
                0
            )

        captured = capsys.readouterr()

        assert "нулевым количеством" in captured.out
        assert "Обработка добавления товара завершена" in captured.out

    def test_successful_order_prints_messages(
        self,
        capsys
    ):
        """При успешном создании заказа выводятся сообщения."""

        product = Product(
            "Телефон",
            "Смартфон",
            50000,
            10
        )

        Order(
            "Заказ №1",
            "Покупка телефона",
            product,
            2
        )

        captured = capsys.readouterr()

        assert "Товар успешно добавлен в заказ" in captured.out
        assert "Обработка добавления товара завершена" in captured.out