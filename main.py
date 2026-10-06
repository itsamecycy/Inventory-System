from product import Product
from inventory import Inventory

product1 = Product(1, 'Air Pods', 900, 10)
product2 = Product(2, 'Keyboard', 200, 5)
product3 = Product(3, 'Mouse', 100, 10)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

inventory.display_inventory()

inventory.remove_product(1)

print("Current inventory:")

inventory.display_inventory()

search = inventory.search_product(2)

if search:
    print("Product found: ", search)
else:
    print("Product not found.")