from django.shortcuts import render
import requests



def show_weather(request):
    city = "Riga"
    key = "63378bc4ba1b4920b4d72446230506"
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}"
    response = requests.get(url).json()
    return render(request, 'show_weather.html',
                  {"response": response})
