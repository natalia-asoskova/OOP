import pytest
from src.product import Product, Category

@pytest.fixture
def first_product():
    return {
        'name': 'Платье',
        'description': 'Летнее',
        'price': 3000,
        'quantity': 10
    }

@pytest.fixture
def second_product():
    return {
        'name': 'Джинсы',
        'description': 'Темно синие',
        'price': 800,
        'quantity': 15
    }

@pytest.fixture
def sample_product(first_product):
    return Product.new_product(first_product)

@pytest.fixture
def another_product(second_product):
    return Product.new_product(second_product)

@pytest.fixture
def empty_category():
    return Category("Одежда", "Для женщин")

@pytest.fixture
def category_with_products(sample_product, another_product):
    cat = Category("Одежда", "Для женщин")
    cat.add_product(sample_product)
    cat.add_product(another_product)
    return cat
