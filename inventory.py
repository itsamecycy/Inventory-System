class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [product for product in self.products if product.id != product_id]

    def display_inventory(self):
        for product in self.products:
            print(product)

    def search_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product

        return None