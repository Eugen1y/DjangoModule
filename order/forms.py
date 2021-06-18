"""
Purchase Application Forms
==========================

"""

from django import forms
from django.utils.translation import gettext as _

from order.models import CartEntity, Order


class CartEntityForm(forms.ModelForm):
    """Cart entity form implementation"""

    quantity = forms.IntegerField(
        min_value=1,
    )

    class Meta:
        model = CartEntity
        fields = ["id", "quantity"]

        widgets = {
            "quantity": forms.NumberInput(attrs={
                "class": "col-1 numberinput form-control"
            })
        }


CartEntitiesFormSet = forms.modelformset_factory(
    CartEntity, form=CartEntityForm, extra=0
)


class OrderForm(forms.ModelForm):
    """Purchase form implementation"""

    address = forms.CharField(
        label=_("address"),
        max_length=128,
    )
    city = forms.CharField(
        label=_("city name"),
        max_length=128,
    )
    zipcode = forms.CharField(
        label=_("zip code"),
        max_length=6,
    )
    country = forms.CharField(
        label=_("country"),
        max_length=32,
    )

    class Meta:
        model = Order
        fields = [
            "address",
            "city",
            "zipcode",
            "country",
        ]

    def get_shipping_address(self):
        super(OrderForm, self).clean()
        address = self.cleaned_data.get("address")
        city = self.cleaned_data.get("city")
        zipcode = self.cleaned_data.get("zipcode")
        country = self.cleaned_data.get("country")

        return f"{address}, {city}, {zipcode}, {country}"

    def save(self, commit=True):
        self.instance.shipping_address = self.get_shipping_address()
        super(OrderForm, self).save()
