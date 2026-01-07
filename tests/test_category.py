import pytest
from src.category import Category
from src.product import Product
from tests.conftest import json_categories  # Импорт для pytest


class TestCategory:
    def test_init_basic(self):
        """Базовая инициализация"""
        product = Product("Test", "desc", 100.0, 1)
        cat = Category("TestCat", "Test desc", [product])
        assert cat.name == "TestCat"
        assert "Test" in cat.products

    def test_empty_products(self):
        """Пустые продукты"""
        cat = Category("Empty", "desc", [])
        assert cat.name == "Empty"
        assert cat.products == ""

    def test_none_products(self):
        cat = Category("None", "desc")  # products=None
        assert cat.name == "None"
        assert cat.products == ""

    def test_products_property(self):
        """@property products"""
        p1 = Product("Samsung", "256GB", 180000.0, 5)
        p2 = Product("iPhone", "512GB", 210000.0, 8)
        cat = Category("Test", "desc", [p1, p2])
        assert "Samsung, 180000 руб." in cat.products
        assert "iPhone, 210000 руб." in cat.products

    def test_add_product(self, empty_category):
        """100% add_product()"""
        product = Product("New Product", "desc", 100.0, 1)
        empty_category.add_product(product)
        assert "New Product" in empty_category.products

    def test_json_categories(self, json_categories):
        """Тест JSON загрузки"""
        assert len(json_categories) == 2
        assert json_categories[0].name == "Смартфоны"
        assert "Samsung Galaxy C23 Ultra" in json_categories[0].products

    def test_real_data(self, smartphones_category):
        """Реальные данные"""
        assert smartphones_category.name == "Смартфоны"
        assert "Samsung Galaxy S23 Ultra" in smartphones_category.products