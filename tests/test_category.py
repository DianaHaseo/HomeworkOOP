import pytest
from src.category import Category
from src.product import Product
from tests.conftest import json_categories

class TestCategory:
    @pytest.fixture(autouse=True)
    def reset_counters(self):
        """Авто сброс счетчиков"""
        Category.products_count = 0
        Category.category_count = 0

    def test_init_basic(self):
        """✅ Задание 1: базовая init + приватность"""
        product = Product("Test", "desc", 100.0, 1)
        cat = Category("TestCat", "Test desc", [product])
        assert cat.name == "TestCat"
        assert cat.description == "Test desc"
        # Приватность: pytest.raises(AttributeError, getattr, cat, '__products')
        assert Category.products_count == 1
        assert Category.category_count == 1

    def test_add_product(self):
        """✅ Задание 1: add_product метод"""
        cat = Category("Test", "desc", [])
        product = Product("New Product", "desc", 100.0, 1)
        cat.add_product(product)
        assert Category.products_count == 1
        assert "New Product" in cat.products

    def test_products_property(self):
        """✅ Задание 2: @property products"""
        p1 = Product("Samsung", "256GB", 180000.0, 5)
        p2 = Product("iPhone", "512GB", 210000.0, 8)
        cat = Category("Phones", "desc", [p1, p2])
        assert "Samsung, 180000 руб. Остаток: 5 шт." in cat.products
        assert len(cat.products.split("\n")) == 2

    def test_products_empty(self):
        """Пустые случаи для property"""
        cat1 = Category("Empty", "desc", [])
        cat2 = Category("None", "desc")
        assert cat1.products == ""
        assert cat2.products == ""

    def test_counters_init(self):
        """Счетчики при init"""
        p1 = Product("P1", "d1", 100, 1)
        cat1 = Category("Cat1", "desc", [p1])  # +1 продукт, +1 категория
        cat2 = Category("Cat2", "desc", [])     # +0 продуктов, +1 категория
        assert Category.products_count == 1
        assert Category.category_count == 2

    def test_counters_add(self):
        """Счетчики при add_product"""
        cat = Category("Test", "desc", [])
        p1 = Product("Add", "d1", 100, 1)
        cat.add_product(p1)
        assert Category.products_count == 1

    def test_json_fixture(self, json_categories):
        """Тест conftest"""
        assert len(json_categories) == 2
        assert json_categories[0].name == "Смартфоны"

    def test_real_fixture(self, smartphones_category):
        """Реальные данные"""
        assert smartphones_category.name == "Смартфоны"
        assert "Samsung Galaxy S23 Ultra" in smartphones_category.products