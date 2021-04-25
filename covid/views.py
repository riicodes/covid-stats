import requests
from django.shortcuts import render


def home(request):
    data = requests.get('https://api.covid19api.com/summary').json()
    global_data = data.get('Global')
    countries = data.get('Countries')
    context = {
        'data': data,
        'global_data': global_data,
        'countries': countries,
    }
    return render(request, 'home.html', context)


def nepal(request):
    total_data = requests.get('https://api.covid19api.com/summary').json()
    data_per_day = requests.get('https://api.covid19api.com/live/country/nepal/status/confirmed/date/2021-01-01T13:13:30Z').json()
    print(data_per_day)
    countries = total_data.get('Countries')
    context = {
        'countries': countries,
        'data_per_day': data_per_day,
    }
    return render(request, 'nepal.html', context)