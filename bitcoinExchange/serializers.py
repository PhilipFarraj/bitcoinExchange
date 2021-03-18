from rest_framework import serializers
from .models import ExchangeRate


class ExchangeRateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ['from_currency', 'to_currency', 'exchange_rate']