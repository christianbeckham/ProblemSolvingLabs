# As a developer, I want the ShoppingCart class to have class properties to keep track of the ShoppingCart’s products(list).
# As a developer, I want the ShoppingCart class to have a method to calculate and return the current total of all products in the cart.
# As a developer, I want the ShoppingCart class to have a method to add a new product to the cart. (Appending to the products list)
# As a developer, I want the ShoppingCart class to have a method to empty all products from the shopping cart.

class ShoppingCart:
    def __init__(self):
        self.products = []

    def get_total_products_in_cart(self):
        return len(self.products)

    def add_product_to_cart(self, product_to_add):
        self.products.append(product_to_add)

    def empty_cart(self):
        for index in range(len(self.products)):
            self.products.pop(index)
