import pytest
from src.category import Category
from src.product import Product
from tests.conftest import json_categories, smartphones_category


class TestCategory:
    @pytest.fixture(autouse=True)
    def reset_counters(self):
        """Автоматический сброс счетчиков перед каждым тестом"""
        Category.products_count = 0
        Category.category_count = 0

    def test_init_basic(self):
        """Базовая инициализация + счетчики"""
        product = Product("Test", "desc", 100.0, 1)
        cat = Category("TestCat", "Test desc", [product])
        assert cat.name == "TestCat"
        assert cat.description == "Test desc"
        assert "Test" in cat.products
        assert Category.products_count == 1
        assert Category.category_count == 1

    def test_init_multiple_products(self):
        """Несколько продуктов в init"""
        p1 = Product("P1", "d1", 100, 1)
        p2 = Product("P2", "d2", 200, 2)
        cat = Category("Multi", "desc", [p1, p2])
        assert Category.products_count == 2
        assert "P1" in cat.products
        assert "P2" in cat.products

    def test_str(self):
        cat = Category("Test", "desc", [])
        assert "Test, количество продуктов: 0 шт." in str(cat)

    def test_class_counters_add_product(self):
        """add_product + счетчик"""
        cat = Category("Test", "desc", [])
        product = Product("New", "desc", 100.0, 1)
        cat.add_product(product)
        assert Category.products_count == 1
        assert "New" in cat.products

    def test_empty_products(self):
        """Пустой список"""
        cat = Category("Empty", "desc", [])
        assert cat.products == ""
        assert Category.products_count == 0

    def test_none_products(self):
        """products=None"""
        cat = Category("None", "desc")
        assert cat.products == ""
        assert Category.products_count == 0

    def test_products_property(self):
        """Несколько продуктов в property"""
        p1 = Product("Samsung", "256GB", 180000.0, 5)
        p2 = Product("iPhone", "512GB", 210000.0, 8)
        cat = Category("Phones", "desc", [p1, p2])
        products_str = cat.products
        assert "Samsung, 180000 руб." in products_str
        assert "iPhone, 210000 руб." in products_str
        assert len(products_str.split("\n")) == 2

    def test_json_categories(self, json_categories):
        """JSON fixture"""
        assert len(json_categories) == 2
        assert json_categories[0].name == "Смартфоны"

    def test_real_data(self, smartphones_category):
        """Реальная фикстура"""
        assert smartphones_category.name == "Смартфоны"
        assert len(smartphones_category.products.split("\n")) == 3