from product import Product
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

#USE inventory_system;
# SELECT * FROM products;

class Inventory:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

    def add_product(self, product):
        cursor = self.connection.cursor()

        query = """
            INSERT INTO products (id, name, price, quantity)
            VALUES (%s, %s, %s, %s)
        """

        values = (
            product.id,
            product.name,
            product.price,
            product.quantity
        )

        try:
            cursor.execute(query, values)
            self.connection.commit()
            print("Product has been added successfully!")

        except mysql.connector.IntegrityError:
            self.connection.rollback()
            print("A product with that ID already exists.")

        finally:
            cursor.close()

    
    def display_inventory(self):
        cursor = self.connection.cursor()

        query = """
            SELECT id, name, price, quantity
            FROM products
        """

        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            for row in results:
                product = Product(
                    row[0],
                    row[1],
                    row[2],
                    row[3]
                )
                print(product)
        else:
            print("Inventory is empty.")

        cursor.close()

    
    def search_product(self, product_id):
        cursor = self.connection.cursor()

        query = """
            SELECT id, name, price, quantity
            FROM products
            WHERE id = %s
        """

        cursor.execute(query, (product_id,))
        row = cursor.fetchone()

        cursor.close()

        if row is not None:
            return Product(
                row[0],
                row[1],
                row[2],
                row[3]
            )

        return None

    
    def remove_product(self, product_id):
        cursor = self.connection.cursor()

        query = "DELETE FROM products WHERE id = %s"

        try:
            cursor.execute(query, (product_id,))
            self.connection.commit()

            if cursor.rowcount > 0:
                return True
            return False

        except mysql.connector.Error:
            self.connection.rollback()
            raise

        finally:
            cursor.close()

    def update_product_price(self, product_id, new_price):
        cursor = self.connection.cursor()

        query = """
            UPDATE products
            SET price = %s
            WHERE id = %s
        """

        values = (new_price, product_id)

        try:
            cursor.execute(query, values)
            self.connection.commit()

            if cursor.rowcount > 0:
                return True
            return False

        except mysql.connector.Error:
            self.connection.rollback()
            raise

        finally:
            cursor.close()

    def update_product_name(self, product_id, new_name):
        cursor = self.connection.cursor()

        query = """
            UPDATE products
            SET name = %s
            WHERE id = %s
        """

        values = (new_name, product_id)

        try:
            cursor.execute(query, values)
            self.connection.commit()

            if cursor.rowcount > 0:
                return True

            return False

        except mysql.connector.Error:
            self.connection.rollback()
            raise

        finally:
            cursor.close()

    def update_product_quantity(self, product_id, new_quantity):
        cursor = self.connection.cursor()

        query = """
            UPDATE products
            SET quantity = %s
            WHERE id = %s
        """

        values = (new_quantity, product_id)

        try:
            cursor.execute(query, values)
            self.connection.commit()

            if cursor.rowcount > 0:
                return True

            return False

        except mysql.connector.Error:
            self.connection.rollback()
            raise

        finally:
            cursor.close()

    def calc_total_value(self):
        cursor = self.connection.cursor()

        query = """
            SELECT SUM(price * quantity)
            FROM products
        """

        try:
            cursor.execute(query)
            result = cursor.fetchone()

            if result[0] is not None:
                return float(result[0])

            return 0.0

        finally:
            cursor.close()

    def low_stock_report(self, threshold=5):
        cursor = self.connection.cursor()

        query = """
            SELECT id, name, price, quantity
            FROM products
            WHERE quantity <= %s
            ORDER BY quantity ASC
        """

        try:
            cursor.execute(query, (threshold,))
            results = cursor.fetchall()

            if not results:
                print("No low-stock products found.")
                return

            print(f"\n--- LOW STOCK REPORT (Quantity <= {threshold}) ---")

            for row in results:
                print(
                    f"ID: {row[0]}, "
                    f"Name: {row[1]}, "
                    f"Price: ₱{row[2]:,.2f}, "
                    f"Quantity: {row[3]}"
                )

        finally:
            cursor.close()
