from django.test import TestCase, Client
from users.views import UserManagement, UserAuthentication


c = Client()


class UserManagementTest(TestCase):
    def test_register_invalid(self):
        response = c.post(UserManagement.register, {'username': 'john', 'password': 'smith'})
        assert response.status_code == 406

    def test_register_valid(self):
        response = c.post(UserManagement.register,
                          {'username': 'john', "email": 'johnsmith@test.com', 'password': 'smith!990',
                           "confirmation": 'smith!990'})
        assert response.status_code == 200

    def test_register_already_taken(self):
        response = c.post(UserManagement.register,
                          {'username': 'john', "email": 'john@test.com', 'password': 'smith!990',
                           "confirmation": 'smith!990'})
        assert response.status_code == 403


class UserAuthenticationTest(TestCase):
    def test_login_invalid(self):
        response = c.post(UserAuthentication.login_view, {'username': 'abcd', 'password': 'fueizbjk-7428'})
        assert response.status_code == 406

    def test_login_valid(self):
        response = c.post(UserAuthentication.login_view, {'username': 'john', 'password': 'smith!990'})
        assert response.status_code == 200

    def test_logout(self):
        pass
