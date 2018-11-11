from django.shortcuts import render
import requests
import json


def home(request):
    api_req = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_req.content)
    return render(request, 'home.html', {'api': api})
