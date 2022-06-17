from django.test import TestCase, Client
from products.models import Product
from products.views import increase_number_item, decrease_number_item


"""Unit tests"""


class ProductModel(TestCase):
    def test_create_product(self):
        """Test product creation"""
        new_product = Product.objects.create(name='apple', description='',
                                             price=0.5, number_in_store=20)
        self.assertEqual(new_product.price, 0.5)


class ProductNumberItems(TestCase):
    def test_increase_items(self):
        """Test increase of items for a product"""
        new_product = Product.objects.create(name='apple', description='',
                                             price=0.5, number_in_store=20)

        result = increase_number_item(new_product.id, 2)
        self.assertEqual(result, 'Number of items has been increased successfully')
        self.assertEqual(Product.objects.get(id=new_product.id).number_in_store, 22)

    def test_decrease_number_items(self):
        """Test decrease of items for a product"""
        new_product = Product.objects.create(name='apple', description='',
                                             price=0.5, number_in_store=20)

        result = decrease_number_item(new_product.id, 2)
        self.assertEqual(result, 'Number of items has been decreased successfully')
        self.assertEqual(Product.objects.get(id=new_product.id).number_in_store, 18)


"""Functional tests"""


class ProductManagement(TestCase):
    def set_up(self):
        self.client = Client()

    def test_create_product(self):
        """Test product creation from a request"""
        response = self.client.post('/products/create_product',
                                    {'name': 'apple', 'description': '',
                                     'price': 0.5, 'number_in_store': 20})
        self.assertContains(response, 'Product has been created successfully')

    def test_view_products(self):
        """Test display of products from a request"""
        response = self.client.post('/products/create_product',
                                    {'name': 'apple', 'description': '',
                                     'price': 0.5, 'number_in_store': 20})
        response = self.client.get('/products/')
        self.assertContains(response, 'apple')
