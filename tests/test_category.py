import pytest
from src.category import Category
from src.product import Product
from tests.conftest import json_categories, smartphones_category, tv_category, empty_category


class TestCategory:
    @pytest.fixture(autouse=True)
    def reset_counters(self):
        """Сброс глобальных счетчиков"""
        Category.products_count = 0
        Category.category_count = 0

    def test_init_basic(self):
        product = Product("Test", "desc", 100.0, 1)
        cat = Category("TestCat", "Test desc", [product])
        assert cat.name == "TestCat"
        assert cat.description == "Test desc"
        assert "Test" in cat.products

    def test_init_multiple_products(self):
        p1 = Product("P1", "d1", 100, 1)
        p2 = Product("P2", "d2", 200, 2)
        cat = Category("Multi", "desc", [p1, p2])
        assert Category.products_count == 2
        assert "P1" in cat.products

    def test_init_empty_list(self):
        cat = Category("Empty", "desc", [])
        assert cat.products == ""
        assert Category.products_count == 0

    def test_init_no_products(self):
        cat = Category("None", "desc")
        assert cat.products == ""

    def test_str_total_quantity(self):
        p1 = Product("A", "d", 100, 5)
        p2 = Product("B", "d", 200, 8)
        cat = Category("Test", "desc", [p1, p2])
        assert str(cat) == "Test, количество продуктов: 13 шт."

    def test_str_empty_category(self):
        cat = Category("Empty", "desc", [])
        assert str(cat) == "Empty, количество продуктов: 0 шт."

    def test_str_real_data(self, smartphones_category):
        assert "Смартфоны, количество продуктов: 27 шт." in str(smartphones_category)

    def test_add_product_empty(self, empty_category):
        product = Product("New", "desc", 100.0, 1)
        empty_category.add_product(product)
        assert "New" in empty_category.products
        assert Category.products_count == 1

    def test_add_product_multiple(self):
        cat = Category("Test", "desc", [])
        p1 = Product("P1", "d1", 100, 1)
        p2 = Product("P2", "d2", 200, 2)
        cat.add_product(p1)
        cat.add_product(p2)
        assert len(cat.products.split("\n")) == 2

    def test_products_property_single(self):
        p1 = Product("Samsung", "256GB", 180000.0, 5)
        cat = Category("Phones", "desc", [p1])
        assert cat.products == "Samsung, 180000.0 руб. Остаток: 5 шт."

    def test_products_property_multiple(self):
        """Фикс: проверяем полное совпадение, не частичное"""
        p1 = Product("Samsung", "256GB", 180000.0, 5)
        p2 = Product("iPhone", "512GB", 210000.0, 8)
        cat = Category("Phones", "desc", [p1, p2])
        expected = "Samsung, 180000.0 руб. Остаток: 5 шт.\niPhone, 210000.0 руб. Остаток: 8 шт."
        assert cat.products == expected

    def test_products_property_empty(self):
        cat = Category("Empty", "desc", [])
        assert cat.products == ""

    def test_iterator_basic(self):
        p1 = Product("A", "d", 100, 1)
        p2 = Product("B", "d", 200, 2)
        cat = Category("Test", "desc", [p1, p2])
        products = list(cat)
        assert len(products) == 2
        assert products[0].name == "A"
        assert products[1].name == "B"

    def test_iterator_real_data(self, smartphones_category):
        products = list(smartphones_category)
        assert len(products) == 3
        assert products[0].name == "Samsung Galaxy S23 Ultra"

    def test_iterator_empty(self, empty_category):
        products = list(empty_category)
        assert len(products) == 0

    def test_json_categories(self, json_categories):
        assert len(json_categories) == 2
        assert json_categories[0].name == "Смартфоны"

    def test_tv_category(self, tv_category):
        assert tv_category.name == "Телевизоры"
        assert str(tv_category) == "Телевизоры, количество продуктов: 7 шт."

    def test_full_cycle(self):
        p1 = Product("TV1", "desc1", 100000, 3)
        cat = Category("TVs", "desc", [p1])
        p2 = Product("TV2", "desc2", 150000, 4)
        cat.add_product(p2)
        assert str(cat) == "TVs, количество продуктов: 7 шт."
        assert len(list(cat)) == 2