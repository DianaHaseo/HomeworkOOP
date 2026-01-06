import pytest
from src.category import Category
from src.product import Product

@pytest.fixture(autouse=True)
def reset_counters():
    Category.products_count = 0
    Category.category_count = 0

@pytest.fixture
def category1():
    p1 = Product("Samsung Galaxy S23 Ultra", "", 180000.0, 5)
    p2 = Product("Iphone 15", "", 210000.0, 8)
    p3 = Product("Xiaomi Redmi Note 11", "", 31000.0, 14)
    return Category("Смартфоны", "desc", [p1, p2, p3])

@pytest.fixture
def category2():
    p4 = Product("55\" QLED 4K", "", 123000.0, 7)
    return Category("Телевизоры", "desc", [p4])

@pytest.fixture
def empty_category():
    return Category("Empty", "desc", [])

def test_category_initialization(category1):
    assert category1.name == "Смартфоны"
    assert len(category1.products.split("\n")) == 3

def test_category_getter_format(category1):
    assert "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт." in category1.products

def test_add_product(empty_category):
    p = Product("New", "", 100.0, 1)
    empty_category.add_product(p)
    assert len(empty_category.products.split("\n")) == 1
    assert "New, 100 руб. Остаток: 1 шт." in empty_category.products
    assert Category.products_count == 1

def test_category_counters(category1, category2):
    assert Category.category_count == 2
    assert Category.products_count == 4

def test_category2_contents(category2):
    assert category2.name == "Телевизоры"
    assert len(category2.products.split("\n")) == 1
    assert "55\" QLED 4K" in category2.products