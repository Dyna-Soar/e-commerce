from django.test import TestCase, Client
from clients.models import ClientUser, Card


"""Unit tests"""


class ClientModel(TestCase):
    def test_create_client(self):
        client_user = ClientUser.objects.create(username='client_test1',
                                                email='client@test.com',
                                                password='fbjekzfje1654',
                                                country='France',
                                                zip_code='75010',
                                                address='5 rue de paris')

        self.assertEqual(client_user.username, 'client_test1')
        self.assertEqual(client_user.zip_code, '75010')


class CardModel(TestCase):
    def test_create_card(self):
        client_user = ClientUser.objects.create(username='client_test1',
                                                email='client@test.com',
                                                password='fbjekzfje1654',
                                                country='France',
                                                zip_code='75010',
                                                address='5 rue de paris')

        card = Card.objects.create(client=ClientUser.objects.get(username='client_test1'),
                                   full_name='test_name test_surname',
                                   card_network='Visa',
                                   card_number=0,
                                   card_security_code=123,
                                   expiration_date='07/2028')
        self.assertEqual(card.card_network, 'Visa')
        self.assertEqual(card.client_id, 1)


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
