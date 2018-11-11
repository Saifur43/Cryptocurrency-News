from django.shortcuts import render
import requests
import json


def home(request):
    # price data
    price_req = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTC,"
                             "XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_req.content)

    # news
    api_req = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_req.content)
    return render(request, 'home.html', {'api': api, 'price': price})
