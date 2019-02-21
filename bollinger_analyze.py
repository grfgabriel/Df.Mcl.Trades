import requests, json
import matplotlib.pyplot as plt
import pandas as pd
import time
import os
import numpy as np

csv_name = "tickers.csv"
existe = os.path.isfile(csv_name)
window = 100
divergence =  1
error_count = 0


if existe :
    pass
else:
    grava = open(csv_name,"w")
    grava.write("bid,ask\n") 
    grava.close()

fig = plt.figure(figsize=(10,5))
ax = fig.gca()

def bollinger_Bands(tickers, window, divergence):
    if len(tickers) > window:
        media = tickers.rolling(window = window).mean()
        rolling_std = tickers.rolling(window = window).std()
        upper_band = media + (rolling_std * divergence)
        lower_band = media - (rolling_std * divergence)
        return media, upper_band, lower_band 
    
    return 0,0,0    

def get_tickers():
    bitfinex_ltc = "https://api.bitfinex.com/v1/pubticker/ltcbtc"
    data_bitfinex = requests.get(url=bitfinex_ltc)
    binary_bitfinex = data_bitfinex.content
    output_bitfinex = json.loads(binary_bitfinex)
    grava = open(csv_name,"a")
    grava.write(str(output_bitfinex['bid'])+","+str(output_bitfinex['ask'])+"\n")
    grava.close()
    time.sleep(1)


##spread is the difference between the highest and lowest in percentage
def spread(bid,ask):
    porcento = ask / 100
    diferenca = ask - bid 
    porcentagem = diferenca / porcento

    return porcentagem

def plot():
    df = pd.read_csv(csv_name)
    if len(df) > 1:
        ax.clear()
        bid = df['bid']
        ask = df['ask']
        diferenca = ask[-1:] - bid[-1:]
        plt.title("Letecoin / BTC")
        ax.set_xlim(len(bid)/10, len(bid)+(len(bid)/4)+5)
        ax.plot(bid,label = "BID - VENDA LTC " + str(np.around(float(bid[-1:]),8)), color = 'green', alpha = .5)
        ax.plot(ask,label = "ASK - VENDA LTC " + str(np.around(float(ask[-1:]),8)), color = 'red', alpha = .5)

        media, upper_band, lower_band = bollinger_Bands(bid, window, divergence)
        ax.plot(media,"--", color = "gray", label = "SMA " + str(window))
        ax.plot(upper_band,"--", color = "blue",  label = "Upper band " + str(window), alpha = .5)
        ax.plot(lower_band,"--", color = "purple", label = "Lower band " + str(window))

        porcentagem = spread(bid[-1:],ask[-1:])
        porcentagem_str = str(porcentagem)
        ax.text(len(ask) + (len(ask)/10), bid[-1:] + (diferenca/2), "Spread " + str(np.around(float(porcentagem),3)) + "%")
        plt.legend()
        plt.pause(1)
        

while True:
    try:
        get_tickers()
    except:
        error_count = error_count + 1
        print(str(error_count))
        time.sleep(2)

    try:
        plot()
    except:
        print("Erro for plot")
        exit()
