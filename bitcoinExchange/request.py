import requests
from bitcoinExchange.models import ExchangeRate


def request_data(from_currency, to_currency, api_key):
    response = requests.get(
        'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(
            from_currency, to_currency, api_key))
    return response.json()['Realtime Currency Exchange Rate']


def get_data(from_currency, to_currency, api_key):
    response = request_data(from_currency, to_currency, api_key)
    rate, created = ExchangeRate.objects.get_or_create(from_currency=response['1. From_Currency Code'],
                                                       to_currency=response['3. To_Currency Code'],
                                                       defaults={'exchange_rate': response['5. Exchange Rate'],
                                                                 'last_refreshed': response['6. Last Refreshed']})
    if not created:
        rate.exchange_rate = response['5. Exchange Rate']
        rate.last_refreshed = response['6. Last Refreshed']
        rate.save()

    return created
