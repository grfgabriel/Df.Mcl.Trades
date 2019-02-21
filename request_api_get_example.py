import requests
import json
import pandas as pd
import time


bitfinex_ltc = 'https://api.bitfinex.com/v1/pubticker/ltcbtc'
data_ltc  = requests.get(url = bitfinex_ltc) 

binary_data = data_ltc.content
output_btc = json.loads(binary_data)

print('compra - ', output_btc['bid'])
print('venda - ', output_btc['ask'])