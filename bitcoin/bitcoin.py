import requests
import json
import sys

link = 'https://rest.coincap.io/v3/assets/bitcoin?apiKey=0fb27e076632c2a61cf107a4216f4e9285fe3587c5997342eb821458a28b3c55'

if len(sys.argv) < 2:
    sys.exit('Missing Commandline argument')

try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit('command line argument is not a number')
else:
    try:
        response = requests.get(link)



    except requests.RequestException:
        sys.exit('Failed')
    else:
        response_parse = response.json()
        price_per = float(response_parse.get('data').get('priceUsd'))
        price = bitcoin * price_per
        print(f'${price:,.4f}')







