import pytest
from src.product import Product


class TestProduct:
    def test_init_complete(self):
        product = Product("Test", "desc", 100.0, 10)
        assert product.name == "Test"
        assert product.description == "desc"
        assert product.price == 100.0
        assert product.quantity == 10

    def test_str(self):
        product = Product("Test", "desc", 100.0, 10)
        assert str(product) == "Test, 100.0 руб. Остаток: 10 шт."

    def test_add(self):
        p1 = Product("A", "d", 100.0, 2)
        p2 = Product("B", "d", 50.0, 3)
        assert p1 + p2 == 350.0  # (100*2) + (50*3)

    def test_new_product_simple(self):
        """Задание 3: базовый класс-метод"""
        data = {"name": "New", "description": "desc", "price": 150.0, "quantity": 3}
        product = Product.new_product(data)
        assert product.name == "New"
        assert product.price == 150.0

    def test_new_product_duplicate(self):
        """✅ ДОПОЛНИТЕЛЬНОЕ Задание 3: дубликат"""
        products = [Product("Test", "desc", 100.0, 5)]
        data = {"name": "Test", "description": "new desc", "price": 200.0, "quantity": 3}

        updated = Product.new_product(data, products)
        assert updated is products[0]  # Тот же объект
        assert products[0].quantity == 8  # 5+3
        assert products[0].price == 200.0  # max(100,200)

    def test_price_setter_valid(self):
        """Задание 4: валидная цена"""
        product = Product("Test", "desc", 100.0, 1)
        product.price = 250.0
        assert product.price == 250.0

    def test_price_setter_zero(self, capfd):
        """Задание 4: цена <= 0"""
        product = Product("Test", "desc", 100.0, 1)
        product.price = 0
        captured = capfd.readouterr()
        assert "Цена не должна быть" in captured.out
        assert product.price == 100.0

    def test_price_setter_price_decrease(self, monkeypatch):
        """✅ ДОПОЛНИТЕЛЬНОЕ Задание 4: понижение цены"""
        product = Product("Test", "desc", 100.0, 1)
        monkeypatch.setattr("builtins.input", lambda _: "y")
        product.price = 80.0
        assert product.price == 80.0

    def test_price_setter_decrease_cancel(self, monkeypatch, capfd):
        """✅ ДОПОЛНИТЕЛЬНОЕ: отмена понижения"""
        product = Product("Test", "desc", 100.0, 1)
        monkeypatch.setattr("builtins.input", lambda _: "n")
        product.price = 80.0
        captured = capfd.readouterr()
        assert "Изменение цены отменено" in captured.out
        assert product.price == 100.0  # Не изменилась
