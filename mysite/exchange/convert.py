from prices import Money
from django_prices_openexchangerates import exchange_currency

def convert(amount, from_currency, to_currency):
    converted_price = exchange_currency(Money(amount=amount, currency=from_currency), to_currency)
    return converted_price