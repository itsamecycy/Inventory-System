from product import Product
from inventory import Inventory

#SELECT * FROM inventory_system.products; run in MySQL workbench to check table of products

inventory = Inventory()

def menu(inventory):
    while True:
        print("\n===== INVENTORY SYSTEM =====")
        print("1. Add Product\n", 
              "2. Remove Product\n", 
              "3. Search Product\n", 
              "4. Display Product\n", 
              "5. Update Product\n",
              "6. Calculate total Inventory Value\n",
              "7. Stock Report\n",
              "8. Exit\n")

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
            calc_total = inventory.calc_total_value()
            print(f"Total Inventory Value is ${calc_total:,.2f}.")
        elif choice == "7":
            low_stock = inventory.low_stock_report()
        elif choice == "8":
            print("Exiting program.....")
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
                while True:
                    product_name = input("Enter the product's name: ").strip().title()
                    if not product_name:
                        print("Name cannot be empty.")
                        continue
                    break
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

                if inventory.add_product(product):
                    print("Product has been added successfully!")
                    break
                else:
                    print("Could not add product. The ID may already exist.")
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


def update_price(inventory, product):
    while True:
        try:
            product_price = float(input("Enter the new price: "))

            if product_price < 0:
                print("Price cannot be negative.")
                continue

            if inventory.update_product_price(product.id, product_price):
                print("Price updated successfully!")
                print(inventory.search_product(product.id))
            else:
                print("Price was not changed, or the product was not found.")

            break

        except ValueError:
            print("Please enter a valid price!")


def update_name(inventory, product):
    while True:
        product_name = input(
            "Enter the new name for the product: "
        ).strip().title()

        if not product_name:
            print("Name cannot be empty!")
            continue

        if inventory.update_product_name(product.id, product_name):
            print("Name updated successfully!")
            print(inventory.search_product(product.id))
        else:
            print("Name was not changed, or the product was not found.")

        break


def update_quantity(inventory, product):
    while True:
        try:
            product_quantity = int(input("Enter the new quantity: "))

            if product_quantity < 0:
                print("Quantity cannot be negative.")
                continue

            if inventory.update_product_quantity(
                product.id, product_quantity
            ):
                print("Quantity updated successfully!")
                print(inventory.search_product(product.id))
            else:
                print(
                    "Quantity was not changed, or the product was not found."
                )

            break

        except ValueError:
            print("Please enter a valid quantity!")


def update_menu(inventory):

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

    while True:

        print("\nWhat would you like to update?")
        print("1. Product Name\n", "2. Product Price\n", "3. Product Stock\n", "4. Exit\n")
        
        update_choice = input("Choose what to update: ")

        if update_choice == "1":
            update_name(inventory, product)
        elif update_choice == "2":
            update_price(inventory, product)
        elif update_choice == "3":
            update_quantity(inventory, product)
        elif update_choice == "4":
            print("Going back to main menu...")
            break
        else:
            print("Please enter a valid choice!")

try:
    menu(inventory)
finally:
    inventory.connection.close()
    print("Database connection closed.")