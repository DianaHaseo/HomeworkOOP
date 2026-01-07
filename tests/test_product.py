import pytest
from src.product import Product


class TestProduct:
    def test_init_complete(self):
        """Покрытие Product.__init__ (все атрибуты)"""
        product = Product("Test", "desc", 100.0, 10)
        assert product.name == "Test"
        assert product.description == "desc"
        assert product.price

    def test_new_product(self):
        """100% покрытие @classmethod"""
        data = {
            "name": "New Product",
            "description": "Test desc",
            "price": 150.0,
            "quantity": 3
        }
        product = Product.new_product(data)
        assert product.name == "New Product"
        assert product.price == 150.0

    def test_price_getter(self):
        product = Product("Test", "desc", 200.0, 1)
        assert product.price == 200.0

    def test_price_setter_valid(self):
        product = Product("Test", "desc", 100.0, 1)
        product.price = 250.0
        assert product.price == 250.0

    def test_price_setter_invalid(self):
        product = Product("Test", "desc", 100.0, 1)
        product.price = 0  # Должно остаться 100.0
        assert product.price == 100.0

    def test_real_samsung(self):
        product = Product("Samsung Galaxy S23 Ultra", "256GB...", 180000.0, 5)
        assert product.name == "Samsung Galaxy S23 Ultra"