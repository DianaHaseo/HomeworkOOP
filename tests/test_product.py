import pytest

from src.product import Product


class TestProductInit:
    """Тесты инициализации Product."""

    def test_product_init(self):
        """Создание продукта."""
        product = Product(
            "Тест",
            "Описание",
            100.0,
            10
        )

        assert product.name == "Тест"
        assert product.description == "Описание"
        assert product.price == 100.0
        assert product.quantity == 10

    def test_product_str(self):
        """__str__ метод."""
        product = Product(
            "Телефон",
            "Смартфон",
            50000.0,
            5
        )

        assert "Телефон" in str(product)
        assert "50000.0 руб" in str(product)
        assert "5 шт" in str(product)


class TestProductAdd:
    """Тесты сложения продуктов."""

    def test_add_two_products(self):
        """Сложение двух продуктов."""
        product1 = Product(
            "Тест 1",
            "Описание 1",
            100.0,
            10
        )

        product2 = Product(
            "Тест 2",
            "Описание 2",
            200.0,
            5
        )

        result = product1 + product2
        expected = (100.0 * 10) + (200.0 * 5)

        assert result == expected

    def test_add_product_with_zero_quantity(self):
        """Сложение с нулевым количеством."""
        product1 = Product(
            "Тест 1",
            "Описание 1",
            100.0,
            0
        )

        product2 = Product(
            "Тест 2",
            "Описание 2",
            200.0,
            5
        )

        result = product1 + product2
        expected = 0 + (200.0 * 5)

        assert result == expected


class TestProductPrice:
    """Тесты цены продукта."""

    def test_price_setter_increase(self):
        """Увеличение цены."""
        product = Product(
            "Тест",
            "Описание",
            100.0,
            10
        )

        product.price = 150.0

        assert product.price == 150.0

    def test_price_setter_zero(self, capsys):
        """Установка нулевой цены."""
        product = Product(
            "Тест",
            "Описание",
            100.0,
            10
        )

        product.price = 0

        captured = capsys.readouterr()

        assert "Цена не должна быть нулевая" in captured.out

    def test_price_setter_negative(self, capsys):
        """Установка отрицательной цены."""
        product = Product(
            "Тест",
            "Описание",
            100.0,
            10
        )

        product.price = -50

        captured = capsys.readouterr()

        assert "Цена не должна быть нулевая" in captured.out


class TestProductNewProduct:
    """Тесты new_product."""

    def test_new_product_from_dict(self):
        """Создание из словаря."""
        data = {
            "name": "Новый продукт",
            "description": "Описание",
            "price": 150.0,
            "quantity": 10
        }

        product = Product.new_product(data)

        assert product.name == "Новый продукт"
        assert product.price == 150.0
        assert product.quantity == 10

    def test_new_product_with_duplicates(self):
        """Создание с дубликатом."""
        data = {
            "name": "Тест",
            "description": "Описание",
            "price": 150.0,
            "quantity": 5
        }

        products_list = [
            Product(
                "Тест",
                "Описание",
                100.0,
                10
            )
        ]

        result = Product.new_product(
            data,
            products_list
        )

        assert result is products_list[0]
        assert result.quantity == 15
        assert result.price == 150.0

"""Тесты функциональности миксина ProductMixin."""