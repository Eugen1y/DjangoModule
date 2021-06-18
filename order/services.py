"""
Purchase Application Services
=============================

"""

from django.apps import apps


def get_cart_entity_price(cart_entity):
    """Return a total price for a cart entity"""

    model = apps.get_model("order", "CartEntity")
    if not isinstance(cart_entity, model):
        raise TypeError(f"{model.__name__} expected")

    return cart_entity.get_total()


def get_cart_entity_quantity(cart_entity):
    """Return a cart entity quantity value"""

    model = apps.get_model("order", "CartEntity")
    if not isinstance(cart_entity, model):
        raise TypeError(f"{model.__name__} expected")

    return cart_entity.quantity

