from rest_framework import viewsets, permissions
from .models import ExchangeRate
from .serializers import ExchangeRateSerializer
from django.http import JsonResponse
from .request import request_data
from .settings import API_KEY


class ExchangeRateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer

    def create(self, request):
        obj = request_data("BTC", "USD", API_KEY)
        data = {
            "from_currency": obj['1. From_Currency Code'],
            "to_currency": obj['3. To_Currency Code'],
            "exchange_rate": obj['5. Exchange Rate']
        }
        return JsonResponse(data)
