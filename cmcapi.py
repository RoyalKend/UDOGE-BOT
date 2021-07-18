import requests
import dotenv, os

# from pprint import pprint as pp

dotenv.load_dotenv()

API_KEY = os.environ.get('API_KEY', "")

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

r = requests.get(url, headers=headers)


def getPrice(symbol):
    apiurl = 'https://pro-api.coinmarketcap.com'
    udogeurl = apiurl + '/v1/cryptocurrency/quotes/latest'
    parameters = {'symbol': symbol}
    session = requests.Session()
    session.headers.update(headers)
    r = session.get(udogeurl, params=parameters)
    data = r.json()['data']['UDOGE']['quote']['USD']['price']['total_supply']
    return data


def total_supply(symbol):
    apiurl = 'https://pro-api.coinmarketcap.com'
    udogeurl = apiurl + '/v1/cryptocurrency/quotes/latest'
    parameters = {'symbol': symbol}
    session = requests.Session()
    session.headers.update(headers)
    r = session.get(udogeurl, params=parameters)
    data = r.json()['data']['UDOGE']['total_supply']
    return data


def price():
    udogeprice = getPrice('UDOGE') * 1000000000
    return f"${round(udogeprice, 2)}"


def total_supply():
    udogetotal_supply = total_supply('UDOGE')
    return f"${round(udogetotal_supply, 2)}"


print(price, total_supply())
