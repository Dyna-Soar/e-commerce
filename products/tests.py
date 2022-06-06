from django.test import TestCase, Client
from django.urls import reverse
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

    def test_view_products(self):
        response = self.client.post('/products/create_product',
                                    {'name': 'apple', 'description': '',
                                     'price': 0.5, 'number_in_store': 20})
        response = self.client.get('/products/')
        self.assertContains(response, 'apple')

    def test_increase_number_item(self):
        #product = Product.objects.get(id=1)
        response = self.client.post(reverse('products:increase_number_item', args=[1]), {'increase_item': 2})
        self.assertContains(response, 'Number of items has been increased successfully')
        self.assertEqual(Product.objects.get(id=1).number_in_store, 22)

    def decrease_number_item(self):
        #product = Product.objects.get(id=1)
        response = self.client.post(reverse('products/1/decrease_number_item', {'decrease_item': 4}))
        self.assertContains(response, 'Number of items has been increased successfully')
        self.assertEqual(Product.objects.get(id=1).number_in_store, 18)
