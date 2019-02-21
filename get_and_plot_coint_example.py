import requests, json
import matplotlib.pyplot as plt
import pandas as pd
import time

fig = plt.figure(figsize=(20,20))
ax = fig.gca()

csv_name = "tickers.csv"
grava = open(csv_name,"w")
grava.write("bid,ask\n") 
grava.close()


def get_tickers():
    bitfinex_ltc = "https://api.bitfinex.com/v1/pubticker/ltcbtc"
    data_bitfinex = requests.get(url=bitfinex_ltc)
    binary_bitfinex = data_bitfinex.content
    output_bitfinex = json.loads(binary_bitfinex)
    grava = open("tickers.csv","a")
    grava.write(str(output_bitfinex['bid'])+","+str(output_bitfinex['ask'])+"\n")
    grava.close()



def plot():
    df = pd.read_csv(csv_name)
    if len(df)> 1 :
        ax.clear()
        bid = df['bid']
        ask = df['ask']
        ax.plot(bid, label = "Bid - Venda LTC "+str(float(bid[-1:])))
        ax.plot(ask, label = "Ask - Compra LTC "+str(float(ask[-1:])))
        plt.legend()
        plt.pause(2)
  
while True:
    try:
        get_tickers()
        time.sleep(1)

    except:
        print("Erro no servidor")
        time.sleep(5)
    try:
        plot()
    except:
        print("Erro na plotagem")
        time.sleep(1)