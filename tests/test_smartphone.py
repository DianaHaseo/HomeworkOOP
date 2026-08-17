import pytest
from src.product import Product
from src.smartphone import Smartphone


class TestSmartphoneInit:
    """Тесты инициализации Smartphone"""

    def test_smartphone_init(self):
        """Создание смартфона"""
        smartphone = Smartphone(
            "Samsung Galaxy S23",
            "256GB, Серый",
            180000.0,
            5,
            95.5,
            "S23",
            256,
            "Серый"
        )
        assert smartphone.name == "Samsung Galaxy S23"
        assert smartphone.price == 180000.0
        assert smartphone.quantity == 5

    def test_smartphone_additional_attributes(self):
        """Дополнительные атрибуты"""
        smartphone = Smartphone(
            "Samsung Galaxy S23",
            "256GB, Серый",
            180000.0,
            5,
            95.5,
            "S23",
            256,
            "Серый"
        )
        assert smartphone.efficiency == 95.5
        assert smartphone.model == "S23"
        assert smartphone.memory == 256
        assert smartphone.color == "Серый"


class TestSmartphoneInheritance:
    """Тесты наследования"""

    def test_smartphone_is_product(self):
        """Smartphone наследует Product"""
        smartphone = Smartphone(
            "Samsung Galaxy S23",
            "256GB, Серый",
            180000.0,
            5,
            95.5,
            "S23",
            256,
            "Серый"
        )
        assert isinstance(smartphone, Product)

    def test_smartphone_has_product_attributes(self):
        """Атрибуты Product доступны"""
        smartphone = Smartphone(
            "Samsung Galaxy S23",
            "256GB, Серый",
            180000.0,
            5,
            95.5,
            "S23",
            256,
            "Серый"
        )
        assert hasattr(smartphone, 'name')
        assert hasattr(smartphone, 'description')
        assert hasattr(smartphone, 'price')
        assert hasattr(smartphone, 'quantity')


class TestSmartphoneStr:
    """Тесты __str__"""

    def test_smartphone_str(self):
        """__str__ метод"""
        smartphone = Smartphone(
            "Samsung Galaxy S23",
            "256GB, Серый",
            180000.0,
            5,
            95.5,
            "S23",
            256,
            "Серый"
        )
        assert "Samsung Galaxy S23" in str(smartphone)
        assert "180000.0 руб" in str(smartphone)


class TestSmartphoneAdd:
    """Тесты сложения"""

    def test_add_two_smartphones(self):
        """Сложение двух смартфонов"""
        smartphone1 = Smartphone(
            "Samsung Galaxy S23",
            "256GB",
            180000.0,
            5,
            95.5,
            "S23",
            256,
            "Серый"
        )
        smartphone2 = Smartphone(
            "Iphone 15",
            "512GB",
            210000.0,
            8,
            98.2,
            "15",
            512,
            "Gray"
        )
        result = smartphone1 + smartphone2
        expected = (180000.0 * 5) + (210000.0 * 8)
        assert result == expected

    def test_add_smartphone_and_product_raises(self):
        """Сложение смартфона и Product вызывает TypeError"""
        smartphone = Smartphone(
            "Samsung Galaxy S23",
            "256GB",
            180000.0,
            5,
            95.5,
            "S23",
            256,
            "Серый"
        )
        product = Product("Тест", "Описание", 100.0, 10)
        with pytest.raises(TypeError):
            smartphone + product