import unittest
from unittest.mock import patch

from inventory import Inventory
from product import Product

import mysql.connector

class TestInventory(unittest.TestCase):

    def setUp(self):
        # Replace the real MySQL connection with a mock.
        self.connect_patcher = patch(
            "inventory.mysql.connector.connect"
        )
        self.mock_connect = self.connect_patcher.start()

        self.inventory = Inventory()

        self.mock_connection = self.mock_connect.return_value
        self.mock_cursor = self.mock_connection.cursor.return_value

    def tearDown(self):
        # Stop the patch after each test.
        self.connect_patcher.stop()

    def test_search_product_found(self):
        # Simulate a row returned by MySQL.
        self.mock_cursor.fetchone.return_value = (
            1, "Keyboard", 200.00, 5
        )

        result = self.inventory.search_product(1)

        self.assertIsInstance(result, Product)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.name, "Keyboard")
        self.assertEqual(result.price, 200.00)
        self.assertEqual(result.quantity, 5)

        self.mock_cursor.execute.assert_called_once_with(
            unittest.mock.ANY, (1,)
        )
        self.mock_cursor.close.assert_called_once()

    def test_search_product_not_found(self):
        # Simulate MySQL finding no matching product.
        self.mock_cursor.fetchone.return_value = None

        result = self.inventory.search_product(999)

        self.assertIsNone(result)
        self.mock_cursor.execute.assert_called_once_with(
            unittest.mock.ANY, (999,)
        )
        self.mock_cursor.close.assert_called_once()

    def test_add_product_success(self):
        product = Product(2, "Mouse", 100.00, 10)

        self.inventory.add_product(product)

        self.mock_cursor.execute.assert_called_once()
        self.mock_connection.commit.assert_called_once()
        self.mock_connection.rollback.assert_not_called()
        self.mock_cursor.close.assert_called_once()

    def test_add_product_duplicate_id(self):
        product = Product(1, "Keyboard", 200.00, 5)

        self.mock_cursor.execute.side_effect = (
            mysql.connector.IntegrityError("Duplicate ID")
        )

        self.inventory.add_product(product)

        self.mock_connection.commit.assert_not_called()
        self.mock_connection.rollback.assert_called_once()
        self.mock_cursor.close.assert_called_once()


    def test_remove_product_success(self):
        self.mock_cursor.rowcount = 1

        result = self.inventory.remove_product(1)

        self.assertTrue(result)
        self.mock_cursor.execute.assert_called_once()
        self.mock_connection.commit.assert_called_once()
        self.mock_connection.rollback.assert_not_called()
        self.mock_cursor.close.assert_called_once()

    def test_remove_product_not_found(self):
        self.mock_cursor.rowcount = 0

        result = self.inventory.remove_product(999)

        self.assertFalse(result)
        self.mock_connection.commit.assert_called_once()
        self.mock_connection.rollback.assert_not_called()
        self.mock_cursor.close.assert_called_once()

    def test_remove_product_database_error(self):
        self.mock_cursor.execute.side_effect = (
            mysql.connector.Error("Database error")
        )

        with self.assertRaises(mysql.connector.Error):
            self.inventory.remove_product(1)

        self.mock_connection.rollback.assert_called_once()
        self.mock_connection.commit.assert_not_called()
        self.mock_cursor.close.assert_called_once()


    def test_update_product_price_success(self):
        self.mock_cursor.rowcount = 1

        result = self.inventory.update_product_price(1, 250.00)

        self.assertTrue(result)
        self.mock_cursor.execute.assert_called_once()
        self.mock_connection.commit.assert_called_once()
        self.mock_connection.rollback.assert_not_called()
        self.mock_cursor.close.assert_called_once()

    def test_update_product_price_not_found(self):
        self.mock_cursor.rowcount = 0

        result = self.inventory.update_product_price(999, 250.00)

        self.assertFalse(result)
        self.mock_connection.commit.assert_called_once()
        self.mock_connection.rollback.assert_not_called()
        self.mock_cursor.close.assert_called_once()


    def test_update_product_name_success(self):
        self.mock_cursor.rowcount = 1

        result = self.inventory.update_product_name(1, "Gaming Keyboard")

        self.assertTrue(result)
        self.mock_cursor.execute.assert_called_once()
        self.mock_connection.commit.assert_called_once()
        self.mock_connection.rollback.assert_not_called()
        self.mock_cursor.close.assert_called_once()

    def test_update_product_name_not_found(self):
        self.mock_cursor.rowcount = 0

        result = self.inventory.update_product_name(999, "Gaming Keyboard")

        self.assertFalse(result)
        self.mock_connection.commit.assert_called_once()
        self.mock_connection.rollback.assert_not_called()
        self.mock_cursor.close.assert_called_once()


    def test_update_product_quantity_success(self):
        self.mock_cursor.rowcount = 1

        result = self.inventory.update_product_quantity(1, 20)

        self.assertTrue(result)
        self.mock_cursor.execute.assert_called_once()
        self.mock_connection.commit.assert_called_once()
        self.mock_connection.rollback.assert_not_called()
        self.mock_cursor.close.assert_called_once()

    def test_update_product_quantity_not_found(self):
        self.mock_cursor.rowcount = 0

        result = self.inventory.update_product_quantity(999, 20)

        self.assertFalse(result)
        self.mock_connection.commit.assert_called_once()
        self.mock_connection.rollback.assert_not_called()
        self.mock_cursor.close.assert_called_once()


    def test_calc_total_value(self):
        self.mock_cursor.fetchone.return_value = (1500.00,)

        result = self.inventory.calc_total_value()

        self.assertEqual(result, 1500.00)
        self.mock_cursor.execute.assert_called_once()
        self.mock_cursor.close.assert_called_once()

    def test_calc_total_value_empty_inventory(self):
        self.mock_cursor.fetchone.return_value = (None,)

        result = self.inventory.calc_total_value()

        self.assertEqual(result, 0.0)
        self.mock_cursor.execute.assert_called_once()
        self.mock_cursor.close.assert_called_once()


    @patch("builtins.print")
    def test_low_stock_report_with_products(self, mock_print):
        self.mock_cursor.fetchall.return_value = [
            (1, "Keyboard", 200.00, 2),
            (2, "Mouse", 100.00, 5),
        ]

        self.inventory.low_stock_report()

        printed_output = " ".join(
            str(call.args[0])
            for call in mock_print.call_args_list
            if call.args
        )

        self.assertIn("LOW STOCK REPORT", printed_output)
        self.assertIn("Keyboard", printed_output)
        self.assertIn("Mouse", printed_output)
        self.mock_cursor.close.assert_called_once()

    @patch("builtins.print")
    def test_low_stock_report_empty(self, mock_print):
        self.mock_cursor.fetchall.return_value = []

        self.inventory.low_stock_report()

        mock_print.assert_called_once_with(
            "No low-stock products found."
        )
        self.mock_cursor.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
