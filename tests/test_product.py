import pytest
import sys
from io import StringIO
from src.product import Product

@pytest.fixture
def product():
    return Product("Test", "desc", 100.0, 10)

def test_new_product():
    data = {"name": "New", "description": "new desc", "price": 200.0, "quantity": 5}
    prod = Product.new_product(data)
    assert prod.name == "New"
    assert prod.price == 200.0
    assert prod.quantity == 5

def test_price_getter(product):
    assert product.price == 100.0

def test_price_setter_positive(product):
    product.price = 150.0
    assert product.price == 150.0

def test_price_setter_negative(product):
    captured_output = StringIO()
    sys.stdout = captured_output
    product.price = 0
    sys.stdout = sys.__stdout__
    assert "Цена не должна быть нулевая или отрицательная" in captured_output.getvalue()
    assert product.price == 100.0

def test_price_setter_negative_zero(product):
    captured_output = StringIO()
    sys.stdout = captured_output
    product.price = -50.0
    sys.stdout = sys.__stdout__
    assert "Цена не должна быть нулевая или отрицательная" in captured_output.getvalue()
    assert product.price == 100.0