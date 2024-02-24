from django.contrib import admin
from .models import ExchangeRate
# Register your models here.
admin.site.register(ExchangeRate)
admin.site.site_header='Currency Adminstration'