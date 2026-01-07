import json
import os
import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def json_categories():
    """Загрузка категорий из products.json"""
    path = os.path.join(os.path.dirname(__file__), "../data/products.json")
    if not os.path.exists(path):
        pytest.skip("products.json не найден в data/")

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    categories = []
    for cat_data in data:
        products = [Product(**p) for p in cat_data['products']]
        categories.append(Category(cat_data['name'], cat_data['description'], products))
    return categories


@pytest.fixture
def smartphones_category():
    """Фикстура для смартфонов"""
    return Category(
        "Смартфоны",
        "Смартфоны описание",
        [
            Product("Samsung Galaxy S23 Ultra", "256GB...", 180000.0, 5),
            Product("Iphone 15", "512GB...", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB...", 31000.0, 14)
        ]
    )


@pytest.fixture
def tv_category():
    """Фикстура для телевизоров"""
    return Category(
        "Телевизоры",
        "ТВ описание",
        [Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)]
    )


@pytest.fixture
def empty_category():
    """Пустая категория для add_product"""
    return Category("Пустая", "desc", [])