import pytest
from tests.conftests import *
def test_new_product_creates_product(first_product):
    product = Product.new_product(first_product)
    assert isinstance(product, Product)
    assert product.name == 'Платье'
    assert product.description == 'Летнее'
    assert product.price == 3000
    assert product.quantity == 10

def test_product_price(capsys):
    product = Product("Платье", "Красное", 30000.0, 3)
    product.price = 0
    captured = capsys.readouterr()
    assert product.price == 30000.0
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


