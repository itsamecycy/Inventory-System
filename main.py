from product import Product
from inventory import Inventory

inventory = Inventory()

def menu(inventory):
    while True:
        print("\n===== INVENTORY SYSTEM =====")
        print("1. Add Product\n", 
              "2. Remove Product\n", 
              "3. Search Product\n", 
              "4. Display Product\n", 
              "5. Update Product\n",
              "6. Exit\n")

        choice = input("Choose an option: ")

        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            remove_product(inventory)
        elif choice == "3":
            search_product(inventory)
        elif choice == "4":
            print("--- INVENTORY ---")
            inventory.display_inventory()
        elif choice == "5":
            update_menu(inventory)
        elif choice == "6":
            print("Exiting System...")
            break
        else:
            print("Please enter a valid choice and try again!")

def add_product(inventory):
    while True:
        # Error Handling
        try:
            product_id = int(input("Enter the Product's id: "))
            if product_id <= 0:
                print("Product ID must be greater than zero!")
                continue
            if inventory.search_product(product_id) is None:
                product_name = input("Enter the product's name: ").title()
                while True:
                    try:
                        product_price = float(input("Enter product's price: "))
                        if product_price < 0:
                            print("Price cannot be negative")
                            continue
                        break
                    except ValueError:
                        print("Please enter a valid price!")
                while True:
                    try:
                        product_quantity = int(input("Enter amount of quantity: "))
                        if product_quantity < 0:
                            print("Amount of stock cannot be negative!")
                            continue
                        break
                    except ValueError:
                        print("Please enter a valid quantity!")
                product = Product(product_id, product_name, product_price, product_quantity)
                inventory.add_product(product)
                print("Product has been added successfully!")
                break
            else:
                print("ID already exists")
        except ValueError:
            print("Please enter a valid number!")

def remove_product(inventory):
    while True:
        try:
            product_id = int(input("Enter the Product's id: "))
            if product_id <= 0:
                print("Product ID must be greater than zero!")
                continue
            if inventory.remove_product(product_id):
                print("The product was successfully removed.")
                break
            else:
                print("The product you're trying to remove does not exist.")
        except ValueError:
            print("Product ID is invalid.")

def search_product(inventory):
    while True:
        try:
            product_id = int(input("Enter the Product's id: "))
            if product_id <= 0:
                print("Product ID must be greater than zero!")
                continue

            product = inventory.search_product(product_id)

            if product is None:
                print("The product you're trying to find does not exist.")
            else:
                print(product)
                break
        except ValueError:
            print("Product ID is invalid.")

def update_price(inventory):
    while True:
        try:
            product_id = int(input("Enter the product's ID to update: "))
            
            if product_id <= 0:
                print("Product ID must be greater than zero.")
                continue

            product = inventory.search_product(product_id)

            if product is None:
                print("The product you're trying to find does not exist.")
                continue

            while True:
                try:
                    product_price = float(input("Enter the new price: "))

                    if product_price < 0:
                        print("Price cannot be negative.")
                        continue

                    product.update_price(product_price)
                    break
                except ValueError:
                    print("PLease enter a valid price.")

            break

        except ValueError:
            print("Please enter a valid ID!")

def update_menu(inventory):
    while True:
        print("\nWhat would you like to update?")
        print("1. Product Name\n", "2. Product Price\n", "3. Back\n")
        
        update_choice = input("Choose what to update: ")

        if update_choice == "1":
            print("Updating product's name")
        elif update_choice == "2":
            update_price(inventory)
        elif update_choice == "3":
            print("Going back to main menu...")
            break

menu(inventory)