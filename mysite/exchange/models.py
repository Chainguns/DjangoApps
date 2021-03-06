from django.db import models

from prices import Money
from django_prices_openexchangerates import exchange_currency

from django.db import models
from django_prices.models import MoneyField, TaxedMoneyField


class Model(models.Model):
    currency = models.CharField(max_length=3, default="BTC")
    price_net_amount = models.DecimalField(max_digits=9, decimal_places=2, default="5")
    price_net = MoneyField(amount_field="price_net_amount", currency_field="currency")
    price_gross_amount = models.DecimalField(
        max_digits=9, decimal_places=2, default="5"
    )
    price_gross = MoneyField(
        amount_field="price_gross_amount", currency_field="currency"
    )
    price = TaxedMoneyField(
        net_amount_field="price_net_amount",
        gross_amount_field="price_gross_amount",
        currency="currency",
    )