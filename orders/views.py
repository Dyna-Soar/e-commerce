from django.shortcuts import render
from orders.models import Order, OrderItem
from products.models import Product
from clients.models import ClientUser
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def validate_order():
    pass


def create_order_item(product_cart, client):
    product = Product.objects.get(id=product_cart["product"])
    order_item = OrderItem.objects.create(client=client, product=product, number_items=product_cart["number_items"])
    order_item.save()
    return order_item


@login_required
def create_order(request):
    if request.method == "POST":
        cart_products = request.user["cart"]["products"]
        #cart_products = client_session["cart"]["products"]
        order = Order.objects.create(client=request.user, address_to_ship="address")
        order.save()
        for product_cart in cart_products:
            order_item = create_order_item(product_cart, request.user)
            order.products.add(order_item)
            order.save()
        return HttpResponse(f'Order has been created: {order.total_price}')


