from product import Product
from inventory import Inventory

def menu():
    while True:
        print("===== INVENTORY SYSTEM =====")
        print("1. Add Product\n", "2. Remove Product\n", "3. Search Product\n", "4. Display Product\n", "5. Exit\n")

        choice = int(input("Choose an option: "))

        if choice == 1:
            print("Adding product")
        elif choice == 2:
            print("Removing Product")
        elif choice == 3:
            print("Searching for the Product")
        elif choice == 4:
            print("Displaying Product")
        elif choice == 5:
            print("Exiting System")
            break
        else:
            print("Please enter a valid choice and try again!")

menu()