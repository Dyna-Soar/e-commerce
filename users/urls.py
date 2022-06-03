from django.urls import path

from users.views import UserManagement, UserAuthentication

app_name = 'users'

urlpatterns = [
    path('register', UserManagement.register, name='register'),
    path('login', UserAuthentication.login_view, name='login'),
    path('logout', UserAuthentication.logout_view, name='logout'),
]