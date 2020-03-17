from django.test import TestCase
from .models import Product
# Create your tests here.
class ProductTests(TestCase):
    """
    Added test to make sure we return a product name
    """
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')