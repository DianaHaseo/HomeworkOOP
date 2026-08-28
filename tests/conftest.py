import json
import os

import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import Lawngrass


@pytest.fixture
def sample_product():
    """Базовый продукт для тестов."""

    return Product(
        "Тестовый продукт",
        "Описание",
        100.0,
        10
    )


@pytest.fixture
def sample_smartphone():
    """Смартфон для тестов."""

    return Smartphone(
        "Samsung Galaxy S23",
        "256GB, Серый",
        180000.0,
        5,
        95.5,
        "S23",
        256,
        "Серый"
    )


@pytest.fixture
def sample_lawngrass():
    """Газонная трава для тестов."""

    return Lawngrass(
        "Газонная трава",
        "Элитная трава",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )


@pytest.fixture
def json_categories():
    """Загрузка категорий из products.json."""

    path = os.path.join(
        os.path.dirname(__file__),
        "../data/products.json"
    )

    if not os.path.exists(path):
        pytest.skip(
            "products.json не найден в data/"
        )

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []

    for cat_data in data:
        products = [
            Product(**product)
            for product in cat_data["products"]
        ]

        categories.append(
            Category(
                cat_data["name"],
                cat_data["description"],
                products
            )
        )

    return categories


@pytest.fixture
def smartphones_category():
    """Категория со смартфонами."""

    return Category(
        "Смартфоны",
        "Смартфоны описание",
        [
            Product(
                "Samsung Galaxy S23 Ultra",
                "256GB...",
                180000.0,
                5
            ),
            Product(
                "Iphone 15",
                "512GB...",
                210000.0,
                8
            ),
            Product(
                "Xiaomi Redmi Note 11",
                "1024GB...",
                31000.0,
                14
            )
        ]
    )


@pytest.fixture
def tv_category():
    """Категория с телевизорами."""

    return Category(
        "Телевизоры",
        "ТВ описание",
        [
            Product(
                '55" QLED 4K',
                "Фоновая подсветка",
                123000.0,
                7
            )
        ]
    )


@pytest.fixture
def empty_category():
    """Пустая категория."""

    return Category(
        "Пустая",
        "desc",
        []
    )