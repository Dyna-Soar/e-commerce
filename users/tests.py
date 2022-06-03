from django.test import TestCase, Client
from users.models import User


"""Unit tests"""


class UserModelTest(TestCase):
    def test_create(self):
        user = User.objects.create_user(username='georges', password='fnezin-13579')
        self.assertEqual(user.username, 'georges')


"""Functional tests"""

c = Client()


class UserManagementTest(TestCase):
    def test_register_invalid(self):
        response = c.post('users/register', {'username': 'john', 'password': 'smith'})
        self.assertEqual(response.status_code, 406)

    def test_register_valid(self):
        response = c.post('users/register',
                          {'username': 'john', "email": 'johnsmith@test.com', 'password': 'smith!990',
                           "confirmation": 'smith!990'})
        self.assertEqual(response.status_code, 200)

    def test_register_already_taken(self):
        response = c.post('users/register',
                          {'username': 'john', "email": 'john@test.com', 'password': 'smith!990',
                           "confirmation": 'smith!990'})
        self.assertEqual(response.status_code, 403)


class UserAuthenticationTest(TestCase):
    def test_login_invalid(self):
        response = c.post('users/login', {'username': 'abcd', 'password': 'fueizbjk-7428'})
        self.assertEqual(response.status_code, 406)

    def test_login_valid(self):
        response = c.post('users/login', {'username': 'john', 'password': 'smith!990'})
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        pass
