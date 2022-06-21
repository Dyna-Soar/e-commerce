from django.test import TestCase
from products.models import Product
from clients.models import ClientUser
from carts.views import create_cart, add_product_to_cart
from orders.models import Order
from orders.views import create_order, create_order_item


class OrderManagementTest(TestCase):
    def set_up(self):
        self.product = Product.objects.create(name='apple',
                                              description='',
                                              price=0.5,
                                              number_in_store=20)
        self.client_user = ClientUser.objects.create(username='client_test1',
                                                     email='client@test.com',
                                                     password='fbjekzfje1654',
                                                     country='France',
                                                     zip_code='75010',
                                                     address='5 rue de paris')

    def test_create_order_item(self):
        pass

    def test_create_order(self):
        # Create 2-3 products
        product1 = Product.objects.create(name='apple', description='', price=0.5, number_in_store=20)
        product2 = Product.objects.create(name='banana', description='', price=0.3, number_in_store=30)
        product3 = Product.objects.create(name='orange', description='', price=0.4, number_in_store=10)
        # Add products to cart
        create_cart(self.client.session)
        add_product_to_cart(self.client.session, product1, 4)
        add_product_to_cart(self.client.session, product2, 2)
        add_product_to_cart(self.client.session, product3, 6)
        # Test order view
        response = self.client.post("/orders/create_order")
        self.assertContains(response, "Order has been created")
        #self.assertEquals(response.status_code, 200)
