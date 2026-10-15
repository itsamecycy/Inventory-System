import unittest

from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        # Create a fresh product before each test.
        self.product = Product(1, "Keyboard", 200.00, 5)

    def test_product_attributes(self):
        self.assertEqual(self.product.id, 1)
        self.assertEqual(self.product.name, "Keyboard")
        self.assertEqual(self.product.price, 200.00)
        self.assertEqual(self.product.quantity, 5)


    def test_product_string_representation(self):
        expected = (
            "Product ID: 1, Name: Keyboard, "
            "Price: $200.0, Quantity: 5"
        )
        self.assertEqual(str(self.product), expected)

if __name__ == "__main__":
    unittest.main()
