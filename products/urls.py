from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.view_products, name='view_products'),
    path('create_product', views.create_product, name='create_product'),
    path('<int:product_id>/increase_number_item', views.increase_number_item, name='increase_number_item'),
    path('<int:product_id>/decrease_number_item', views.decrease_number_item, name='decrease_number_item'),
]