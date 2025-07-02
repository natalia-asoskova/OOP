from tests.conftests import *
def test_category_init(one_category, one_product):
    assert one_category.name == "Одежда"
    assert one_category.description == "Летняя"
    assert len(one_category.products) == 1
    assert one_category.products[0] == one_product

def test_total_counts(reset_counters):
    assert Category.total_category == 1
    assert Category.total_product == 1