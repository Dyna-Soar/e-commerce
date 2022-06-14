from django.shortcuts import render


def create_cart(request):
    if "cart" not in request.session:
        request.session["cart"] = {"products": {}}


def add_product_to_cart(request, product, nb_items):
    if product not in request.session["cart"]["products"]:
        request.session["cart"]["products"][product] = {"nb_items": nb_items}


def add_nb_items_product(request, product, nb_items):
    if product in request.session["cart"]["products"]:
        request.session["cart"]["products"][product]["nb_items"] += nb_items


def remove_nb_items_product(request, product, nb_items):
    if product in request.session["cart"]["products"]:
        request.session["cart"]["products"][product]["nb_items"] -= nb_items
        if request.session["cart"]["products"][product]["nb_items"] == 0:
            request.session["cart"]["products"].remove(product)
