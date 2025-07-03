import pytest
from tests.conftests import *

def test_category_initialization(empty_category):
    assert empty_category.name == "Одежда"
    assert empty_category.description == "Для женщин"
    assert empty_category.get_products_info() == []

def test_product_total_count(empty_category, sample_product):
    empty_category.add_product(sample_product)
    products_info = empty_category.get_products_info()
    assert len(products_info) == 1
    assert products_info[0] == f"{sample_product.name}, {sample_product.price} руб. Остаток: {sample_product.quantity} шт."
    assert Category.total_product >= 1

def test_category_products(category_with_products, sample_product, another_product):
    products_info = category_with_products.get_products_info()
    assert len(products_info) == 2
    strings = [
        f"{sample_product.name}, {sample_product.price} руб. Остаток: {sample_product.quantity} шт.",
        f"{another_product.name}, {another_product.price} руб. Остаток: {another_product.quantity} шт."
    ]
    assert all(info in products_info for info in strings)
