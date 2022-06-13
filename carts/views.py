from django.shortcuts import render


def create_cart(request):
    request.session["cart"] = {"user": request.user, "products": {}}


def add_product_to_cart(request, product, nb_items):
    request.session["cart"]["products"][product] = {"nb_items": nb_items}


def add_nb_items_product(request, product, nb_items):
    request.session["cart"]["products"][product]["nb_items"] += nb_items


def remove_nb_items_product(request, product, nb_items):
    request.session["cart"]["products"][product]["nb_items"] -= nb_items
    if request.session["cart"]["products"][product]["nb_items"] == 0:
        request.session["cart"]["products"].remove(product)
