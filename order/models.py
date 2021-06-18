"""
Purchase Application Models
===========================

"""

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext as _

from order.services import get_cart_entity_price, get_cart_entity_quantity



class Cart(models.Model):
    """Cart model implementation"""

    class Meta:
        db_table = "cart"
        verbose_name = _("shopping cart")
        verbose_name_plural = _("shopping carts")

    purchased = models.BooleanField(
        default=False,
        verbose_name=_("cart purchased flag"),
    )

    customer = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        verbose_name=_("customer"),
    )

    def __repr__(self):
        """Return a string representation of an instance"""

        return f"<Cart {self}>"

    def __str__(self):
        """Return a string version of an instance"""

        return f"[{self.get_entities_count():#}]"

    def get_entities(self):
        """Return cart entities queryset"""

        return self.entities.all()

    def get_entities_count(self):
        """Return cart entities count"""

        return sum(map(get_cart_entity_quantity, self.get_entities()))

    def get_total(self):
        """Return a total price of an instance"""

        return sum(map(get_cart_entity_price, self.get_entities()))



class CartEntity(models.Model):
    """Cart product entity model implementation"""

    class Meta:
        db_table = "cart_entity"
        verbose_name = _("cart product entity")
        verbose_name_plural = _("cart product entities")

    product = models.ForeignKey(
        "product.Product",
        editable=False,
        on_delete=models.PROTECT,
        verbose_name=_("cart product title"),
    )

    quantity = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name=_("cart product quantity"),
    )

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="entities",
        verbose_name=_("related cart entity"),
    )

    def __repr__(self):
        """Return a string representation of an instance"""

        return f"<CartProduct> ('{self}')"

    def __str__(self):
        """Return a string version of an instance"""

        return f"{self.product} - {self.quantity}"

    def get_total(self):
        """Return a total price of an instance"""

        return self.product.price * self.quantity


class Order(models.Model):
    """Purchase model implementation"""

    class Meta:
        db_table = "order"
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    cart = models.OneToOneField(
        Cart,
        on_delete=models.CASCADE,
        related_name="order",
        verbose_name=_("shopping cart"),
    )

    purchased_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("purchased datetime"),
    )

    shipping_address = models.TextField()

    def __repr__(self):
        """Return a string representation of an instance"""

        return f"<Purchase ({self})>"

    def __str__(self):
        """Return a string version of an instance"""

        return f"{self.purchased_at}"

    def get_total(self):
        """Return a total price of an instance"""

        return self.cart.get_total()

    def save(self, *args, **kwargs):
        self.cart.purchased = True
        self.cart.save()

        self.cart.customer.userprofile.balance -= self.get_total()
        self.cart.customer.userprofile.save()

        super(Order, self).save(*args, **kwargs)
