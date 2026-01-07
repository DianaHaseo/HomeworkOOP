import pytest
from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_counters():
    """Автоматический сброс счетчиков перед каждым тестом."""
    Category.products_count = 0
    Category.category_count = 0


@pytest.fixture
def category1():
    """Категория Смартфоны с 3 продуктами."""
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    p3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [p1, p2, p3]  # ✅ Передается в __init__ → копируется в __products
    )


@pytest.fixture
def category2():
    """Категория Телевизоры с 1 продуктом."""
    p4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)

    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [p4]
    )


@pytest.fixture
def empty_category():
    """Пустая категория для теста add_product()."""
    return Category("Пустая", "desc", [])