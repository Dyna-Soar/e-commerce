from django.test import TestCase, Client
from products.models import Product


"""Unit tests"""


class ProductModel(TestCase):
    def test_create_product(self):
        new_product = Product.objects.create()
        self.assertEqual(new_product.price, 1)


"""Functional tests"""


class ProductManagement(TestCase):
    def set_up(self):
        client = Client()

    def test_create_product(self):
        response = self.client.post('/products/create',
                                    {'name': 'apple', 'description': '',
                                     'price': 0.5, 'number_in_store': 20})
        self.assertIn('Number of items has been increased successfully', response)
