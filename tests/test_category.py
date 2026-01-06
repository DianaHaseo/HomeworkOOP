from src.category import Category
from src.product import Product


def test_category_initialization(category1):
    assert category1.name == "Смартфоны"
    assert len(category1.products) == 3


def test_product_initialization(category1):
    product = category1.products[0]
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000.0


def test_category_counters_increment():
    """Тестируем логику счетчиков изолированно"""
    Category.category_count = 0
    Category.products_count = 0

    # Создаем первую категорию с 3 товарами
    Category("Test1", "desc", [
        Product("p1", "", 100, 1),
        Product("p2", "", 100, 1),
        Product("p3", "", 100, 1)
    ])
    assert Category.category_count == 1
    assert Category.products_count == 3

    # Создаем вторую категорию с 1 товаром
    Category("Test2", "desc", [Product("p4", "", 100, 1)])
    assert Category.category_count == 2
    assert Category.products_count == 4


def test_category1_contents(category1):
    assert category1.name == "Смартфоны"
    assert len(category1.products) == 3
    assert category1.products[0].name == "Samsung Galaxy S23 Ultra"


def test_category2_contents(category2):
    assert category2.name == "Телевизоры"
    assert len(category2.products) == 1
    assert category2.products[0].name == '55" QLED 4K'
