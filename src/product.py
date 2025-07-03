class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict):
        return cls(
            name=product_dict.get('name'),
            description=product_dict.get('description'),
            price=product_dict.get('price'),
            quantity=product_dict.get('quantity')
        )


class Category:
    name: str
    description: str
    __products: list

    total_category = 0
    total_product = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.total_category += 1
        Category.total_product += len(self.__products)

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.total_product += 1

    def get_products_info(self):
        result = []
        for product in self.__products:
            info = f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            result.append(info)
        return result

