# import pytest
#
# from src.product import Product, Category
#
#
# @pytest.fixture
# def one_product():
#     return Product(
#         name="платье",
#         description="красный цвет, хлопок",
#         price=3000,
#         quantity=5
#     )
#
# @pytest.fixture
# def one_category(one_product):
#     return Category(
#         name="Одежда",
#         description="Летняя",
#         products=[one_product]
#     )
# @pytest.fixture
# def category(self):
#     Category.total_categories = 0
#     Category.total_products = 0


import pytest
from src.product import Product, Category


@pytest.fixture
def one_product():
    return Product(
        name="платье",
        description="красный цвет, хлопок",
        price=3000,
        quantity=5
    )


@pytest.fixture
def one_category(one_product):
    return Category(
        name="Одежда",
        description="Летняя",
        products=[one_product]
    )


@pytest.fixture(autouse=True)
def reset_counters():
    Category.total_categories = 0
    Category.total_products = 0