from django.db import models


class ExchangeRate(models.Model):
    from_currency = models.CharField(max_length=15)
    to_currency = models.CharField(max_length=15)
    exchange_rate = models.FloatField(max_length=20)
    last_refreshed = models.DateTimeField()

    def __str__(self):
        return '{}-{}'.format(self.from_currency,self.to_currency)