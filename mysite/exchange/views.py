from django.shortcuts import render
from django.views import generic
# Create your views here.

from prices import Money
from django_prices_openexchangerates import exchange_currency

def convert(amount, from_currency, to_currency):
    converted_price = exchange_currency(Money(amount=amount, currency=from_currency), to_currency)
    return converted_price


def ExchangeView(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        from_currency = request.POST['currencies']
        to_currency = request.POST['to_currencies']
        output = convert(amount=amount, from_currency=from_currency, to_currency=to_currency)
        return render(request, 'exchange.html', {'converted_amount': output, 'amount': amount})
    else:
        return render(request, 'exchange.html')

#fix currency list, use this request to get all currencies in relation to usd for easy copy and pasting
# https://openexchangerates.org/api/latest.json?app_id=YOUR_APP_ID