from django.shortcuts import render


def create_cart(user_session):
    if "cart" not in user_session:
        user_session["cart"] = {"products": {}}
        user_session.save()


def add_product_to_cart(user_session, product, nb_items):
    if product not in user_session["cart"]["products"]:
        user_session["cart"]["products"][product.id] = {"nb_items": nb_items}
        user_session.save()


def add_nb_items_product(user_session, product, nb_items):
    if str(product.id) in user_session["cart"]["products"]:
        user_session["cart"]["products"][str(product.id)]["nb_items"] += nb_items
        user_session.save()


def remove_nb_items_product(user_session, product, nb_items):
    if str(product.id) in user_session["cart"]["products"]:
        user_session["cart"]["products"][str(product.id)]["nb_items"] -= nb_items
        user_session.save()
        if user_session["cart"]["products"][str(product.id)]["nb_items"] <= 0:
            user_session["cart"]["products"].remove(product)
            user_session.save()
