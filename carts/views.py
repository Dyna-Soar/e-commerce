from django.shortcuts import render


def create_cart(user_session):
    if "cart" not in user_session:
        user_session["cart"] = {"products": {}}


def add_product_to_cart(user_session, product, nb_items):
    if product not in user_session["cart"]["products"]:
        user_session["cart"]["products"][product] = {"nb_items": nb_items}


def add_nb_items_product(user_session, product, nb_items):
    if product in user_session["cart"]["products"]:
        user_session["cart"]["products"][product]["nb_items"] += nb_items


def remove_nb_items_product(user_session, product, nb_items):
    if product in user_session["cart"]["products"]:
        user_session["cart"]["products"][product]["nb_items"] -= nb_items
        if user_session["cart"]["products"][product]["nb_items"] == 0:
            user_session["cart"]["products"].remove(product)
