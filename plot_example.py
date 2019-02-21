import matplotlib.pyplot as plt 
from coinmarketcap import Market
import pandas as pd
import time


def recebe(lista):
    market = Market()
    ticker = market.ticker(convert="BRL")
    data = ticker['data']['1']['quotes']['BRL']['price']
    btc = data
    lista.append(btc)
    return lista

lista = []

fig = plt.figure(figsize=(10,10))
ax = fig.gca()

while True:
    ax.clear()
    ax.plot(recebe(lista))
    plt.pause(1)