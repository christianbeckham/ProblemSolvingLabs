class ShoppingCart:
    def __init__(self):
        self.products = []

    def get_total_products_in_cart(self):
        return len(self.products)

    def add_product_to_cart(self, product_to_add):
        self.products.append(product_to_add)

    def empty_cart(self):
        for _ in range(len(self.products)):
            self.products.pop()
