from django.urls import path
from clients import views


app_name = 'clients'
urlpatterns = [
    path('register', views.client_register, name='client_register')
]
