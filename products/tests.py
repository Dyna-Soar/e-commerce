from django.test import TestCase, Client
from products.models import Product


"""Unit tests"""


class ProductModel(TestCase):
    def test_create_product(self):
        new_product = Product.objects.create(name='apple', description='',
                                             price=0.5, number_in_store=20)
        self.assertEqual(new_product.price, 0.5)


"""Functional tests"""


class ProductManagement(TestCase):
    def set_up(self):
        self.client = Client()

    def test_create_product(self):
        response = self.client.post('/products/create_product',
                                    {'name': 'apple', 'description': '',
                                     'price': 0.5, 'number_in_store': 20})
        self.assertContains(response, 'Product has been created successfully')
