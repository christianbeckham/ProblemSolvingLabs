from shopping_cart import ShoppingCart


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()

    def add_product(self, new_product):
        self.cart.add_product_to_cart(new_product)

    def view_products(self):
        for product in self.cart.products:
            print(f'{product.name} ({product.category}) costs ${product.price}')
