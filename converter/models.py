from django.db import models

# converter/models.py


class ExchangeRate(models.Model):
    base_currency = models.CharField(max_length=3)
    target_currency = models.CharField(max_length=3)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f"{self.base_currency}-{self.target_currency}"

