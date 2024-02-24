# # script.py

# import os
# import django

# from decimal import Decimal
# import requests

# # Set the DJANGO_SETTINGS_MODULE environment variable
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "currency_converter.settings")

# # Initialize Django
# django.setup()
# from converter.models import ExchangeRate
# def update_exchange_rates():
#     base_currency = 'USD'  # Your base currency
#     api_url = f'https://api.exchangerate-api.com/v4/latest/{base_currency}'

#     try:
#         response = requests.get(api_url)
#         data = response.json()
#         rates = data.get('rates', {})

#         for target_currency, exchange_rate in rates.items():
#             ExchangeRate.objects.update_or_create(
#                 base_currency=base_currency,
#                 target_currency=target_currency,
#                 defaults={'exchange_rate': Decimal(exchange_rate)}
#             )

#         print('Exchange rates updated successfully.')
#     except Exception as e:
#         print(f'Error updating exchange rates: {e}')

# if __name__ == "__main__":
#     update_exchange_rates()


# script.py

import requests
from decimal import Decimal
from django_countries import countries

import os
import django

# from decimal import Decimal
import requests

# # Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "currency_converter.settings")

# Initialize Django
django.setup()
from converter.models import ExchangeRate
all_country_codes=['USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL']
def update_exchange_rates(api_key):
    # Fetch all country codes from django_countries
    
    

    for base_currency in all_country_codes:
        print(base_currency)
        api_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'

        try:
            response = requests.get(api_url)
            data = response.json()
            print(data)
            conversion_rates = data.get('conversion_rates', {})

            for target_currency, exchange_rate in conversion_rates.items():
                ExchangeRate.objects.update_or_create(
                    base_currency=base_currency,
                    target_currency=target_currency,
                    defaults={'exchange_rate': Decimal(exchange_rate)}
                )
                print(f"Updating {base_currency} to {target_currency} with rate {exchange_rate}...")

            #print(f'Exchange rates for {base_currency} updated successfully.')
        except Exception as e:
            print(f'Error updating exchange rates for {base_currency}: {e}')

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'e424011256dddd7d2c444218'
update_exchange_rates(api_key)
