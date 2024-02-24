from django.shortcuts import render,redirect
from .forms import CurrencyConverterForm
from .models import ExchangeRate
from django.contrib.auth import authenticate,login as dj_login,logout
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            print(user)
            dj_login(request,user)
            return redirect("currency_converter")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')
    
    else:
        return render(request, 'login.html')
    


def logout_view(request):
    logout(request)
    return redirect('/')

def currency_converter(request):
    if request.method == 'POST':
        form = CurrencyConverterForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            print(amount)
            from_currency = form.cleaned_data['from_currency']
            print(from_currency)
            to_currency = form.cleaned_data['to_currency']
            print(to_currency)
            exchange_rate = ExchangeRate.objects.filter(
                base_currency=from_currency,
                target_currency=to_currency
            ).first()

            if exchange_rate:
                converted_amount = amount * exchange_rate.exchange_rate
                return render(request, 'currency_converter.html', {'converted_amount': converted_amount,'from_currency':from_currency,'to_currency':to_currency,'amount':amount})
            else:
                error_message = 'Exchange rate not found for the specified currencies.'
                return render(request, 'currency_converter.html', {'error_message': error_message})
    else:
        form = CurrencyConverterForm()

    return render(request, 'currency_converter.html', {'form': form})
