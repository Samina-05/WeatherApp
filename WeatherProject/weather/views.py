# weather/views.py

from django.shortcuts import render
from .forms import CityForm
import requests

def get_weather_data(city):
    api_key = '43260ec4f337b27efcffca1f6409df42'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    return response.json()

def home(request):
    form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            weather_data = get_weather_data(city_name)
            context = {'form': form, 'weather_data': weather_data}
            return render(request, 'weather/home.html', context)

    context = {'form': form}
    return render(request, 'weather/home.html', context)