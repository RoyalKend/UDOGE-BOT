import json
import requests
import threading
import os
import dotenv
from dotenv import dotenv_values
config = dotenv_values(".env")

dotenv.load_dotenv()
API_KEY = os.environ.get('API_KEY')




url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': config.get("API_KEY")
}


def coindata(symbol):
    apiurl = 'https://pro-api.coinmarketcap.com'
    udogeurl = apiurl + '/v1/cryptocurrency/quotes/latest'
    parameters = {'symbol': symbol}
    session = requests.Session()
    session.headers.update(headers)
    r = session.get(udogeurl, params=parameters)
    data = r.json()['data'][symbol]
    return data

def startup():
    threading.Timer(600, startup).start()
    coindata = {
        "perbillionprice": price(),
        "supply": supply(),
        "singleprice": singleprice(),
        "btcprice": btcprice(),
        "ethprice": ethprice(),
        "volume24h": volume24h(),
        "source": source()
    }
    with open("coindata.json", "w") as f:
        f.seek(0)
        json.dump(coindata, f, indent=5)


def price():
    udogeprice = coindata('UDOGE')['quote']['USD']['price'] * 1000000000
    return f"${round(udogeprice, 2)}"

def supply():
    udogesupply = coindata('UDOGE')['max_supply']
    return udogesupply

def volume24h():
    udogevolume = coindata('UDOGE')['quote']['USD']['volume_24h']
    return udogevolume

def btcprice():
    btc = coindata('BTC')['quote']['USD']['price']
    udogebtcprice = coindata('UDOGE')['quote']['USD']['price'] / btc
    return "{:.15f}".format(udogebtcprice)

def ethprice():
    eth = coindata('ETH')['quote']['USD']['price']
    udogeethprice = coindata('UDOGE')['quote']['USD']['price'] / eth
    return "{:.15f}".format(udogeethprice)

def singleprice():
    return "{:.15f}".format(coindata('UDOGE')['quote']['USD']['price'])

def source():
    return "https://coinmarketcap.com/currencies/uncle-doge/"

def data():
    print(coindata('UDOGE'))

startup()
