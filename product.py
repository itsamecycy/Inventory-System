class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name

        # Error handling for negative price and quantity
        if price < 0:
            self.price = 0
        else:
            self.price = price

        if quantity < 0:
            self.quantity = 0
        else:
            self.quantity = quantity

    def add_stock(self, quantity):
        # Error handling for adding negative stock
        if quantity < 0:
            print("Cannot add negative stock.")
        else:
            self.quantity += quantity
            print(f"Added {quantity} units of {self.name} to stock.")

    def remove_stock(self, quantity):
        # Error handling for removing more stock than available
        if quantity < 0:
            print("Cannot remove negative stock.")
        elif quantity > self.quantity:
            print("Not enough stock to remove.")
        else:
            self.quantity -= quantity
            print(f"Removed {quantity} units of {self.name} from stock.")

    def update_price(self, new_price):
        if new_price < 0:
            print("Price cannot be negative!")
        else:
            self.price = new_price
            print(f"Price of {self.name} has been updated to {self.price}.")

    def __str__(self):
        return f"Product ID: {self.id}, Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"