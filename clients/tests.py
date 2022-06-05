from django.test import TestCase, Client
from clients.models import ClientUser, Card


"""Unit tests"""


class ClientModel(TestCase):
    def test_create_client(self):
        client_user = ClientUser.objects.create(username='client_test1',
                                                email='client@test.com',
                                                password='fbjekzfje1654',
                                                confirmation='fbjekzfje1654',
                                                country='France',
                                                zip_code='75010',
                                                address='5 rue de paris')


class CardModel(TestCase):
    def test_create_card(self):
        card = Card.objects.create()


"""Functional tests"""


class ClientTest(TestCase):
    def set_up(self):
        self.client = Client()

    def test_register_client(self):
        pass

    def test_update_client(self):
        pass


class CardTest(TestCase):
    def set_up(self):
        self.client = Client()

    def test_register_card(self):
        pass
