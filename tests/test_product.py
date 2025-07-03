import pytest
from tests.conftests import *
def test_new_product_creates_product(first_product):
    product = Product.new_product(first_product)
    assert isinstance(product, Product)
    assert product.name == 'Платье'
    assert product.description == 'Летнее'
    assert product.price == 3000
    assert product.quantity == 10


