from tests.conftests import one_product

def test_product_init(one_product):
    assert one_product.name == "платье"
    assert one_product.description == "красный цвет, хлопок"
    assert one_product.price == 3000
    assert one_product.quantity == 5
