from django.test import TestCase, Client
from users.models import User


"""Unit tests"""


class UserModelTest(TestCase):
    def test_create(self):
        user = User.objects.create_user(username='georges', password='fnezin-13579')
        self.assertEqual(user.username, 'georges')


"""Functional tests"""


class UserManagementTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_invalid(self):
        response = self.client.post('/users/register',
                                    {'username': 'john', "email": 'johnsmith@test.com',
                                     'password': 'smith', "confirmation": 'sm'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Password must match confirmation")

    def test_register_valid(self):
        response = self.client.post('/users/register',
                                    {'username': 'john', "email": 'johnsmith@test.com',
                                     'password': 'smith!990', "confirmation": 'smith!990'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'User created successfully')

    def test_register_already_taken(self):
        self.client.post('/users/register',
                         {'username': 'john', "email": 'john@test.com',
                          'password': 'smith!990', "confirmation": 'smith!990'})
        response = self.client.post('/users/register',
                                    {'username': 'john', "email": 'john@test.com',
                                     'password': 'smith!990', "confirmation": 'smith!990'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username already taken")


class UserAuthenticationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_invalid(self):
        response = self.client.post('/users/login', {'username': 'abcd', 'password': 'fueizbjk-7428'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Incorrect credentials')

    def test_login_valid(self):
        response = self.client.post('/users/login', {'username': 'john', 'password': 'smith!990'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login successful')

    def test_logout(self):
        pass
