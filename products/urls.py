from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('create_product', views.create_product, name='create_product'),
    path('increase_number_item/<int:product_id>/<int:add_item>', views.increase_number_item, name='increase_number_item'),
    path('decrease_number_item/<int:product_id>/<int:sub_item>', views.decrease_number_item, name='decrease_number_item'),
]