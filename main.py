from product import Product
from inventory import Inventory

inventory = Inventory()

def menu(inventory):
    while True:
        print("===== INVENTORY SYSTEM =====")
        print("1. Add Product\n", "2. Remove Product\n", "3. Search Product\n", "4. Display Product\n", "5. Exit\n")

        choice = input("Choose an option: ")

        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            print("Removing Product")
        elif choice == "3":
            print("Searching for the Product")
        elif choice == "4":
            inventory.display_inventory()
        elif choice == "5":
            print("Exiting System")
            break
        else:
            print("Please enter a valid choice and try again!")

def add_product(inventory):
    while True:
        product_id = int(input("Enter the Product's id: "))
        product_name = input("Enter the product's name: ").capitalize()
        product_price = int(input("Enter product's price: "))
        product_quantity = int(input("Enter amount of quantity: "))

        if inventory.search_product(product_id) is not None:
            print("Id already exists")
        else:
            product = Product(product_id, product_name, product_price, product_quantity)
            inventory.add_product(product)
            break

menu(inventory)