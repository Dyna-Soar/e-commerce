from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.view_products, name='view_products'),
    path('create_product', views.create_product, name='create_product'),
]