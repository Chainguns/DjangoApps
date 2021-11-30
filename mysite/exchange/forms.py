from django import forms

from django_prices.forms import MoneyField

AVAILABLE_CURRENCIES = ["BTC", "USD"]


class ProductForm(forms.Form):
    name = forms.CharField(label="Name")
    price_net = MoneyField(label="net", available_currencies=AVAILABLE_CURRENCIES)