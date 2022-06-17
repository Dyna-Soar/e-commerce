from django.test import TestCase, Client
from carts.views import create_cart, add_product_to_cart, add_nb_items_product, remove_nb_items_product
from products.models import Product


class CartManagement(TestCase):
    def set_up(self):
        self.client = Client()
        # Create users
        self.client.post('/users/register',
                         {'username': 'john', "email": 'johnsmith@test.com',
                          'password': 'smith', "confirmation": 'sm'})
        # Create products
        self.client.post('/products/create_product',
                         {'name': 'apple', 'description': '',
                          'price': 0.5, 'number_in_store': 20})

    def test_create_cart(self):
        """Test cart creation"""
        create_cart(self.client.session)
        self.assertIn("cart", self.client.session)
        self.assertEquals(self.client.session["cart"], {"products": {}})

    def test_add_product_to_cart(self):
        """Test add a product to cart"""
        product = Product.objects.create(name="apple", description="", price=0.5, number_in_store=20)
        create_cart(self.client.session)
        add_product_to_cart(self.client.session, product, 3)
        self.assertIn(str(product.id), self.client.session["cart"]["products"])
        self.assertEquals(self.client.session["cart"]["products"][str(product.id)], {"nb_items": 3})

    def test_add_nb_items_product(self):
        """Test increase the number of unit of a product"""
        product = Product.objects.create(name="apple", description="", price=0.5, number_in_store=20)
        create_cart(self.client.session)
        add_product_to_cart(self.client.session, product, 3)
        add_nb_items_product(self.client.session, product, 4)
        self.assertEquals(self.client.session["cart"]["products"][str(product.id)], {"nb_items": 7})

    def test_remove_nb_items_product(self):
        """Test decrease the number of unit of a product"""
        product = Product.objects.create(name="apple", description="", price=0.5, number_in_store=20)
        create_cart(self.client.session)
        add_product_to_cart(self.client.session, product, 3)
        remove_nb_items_product(self.client.session, product, 2)
        self.assertEquals(self.client.session["cart"]["products"][str(product.id)], {"nb_items": 1})
