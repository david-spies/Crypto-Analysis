import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import seaborn as sns
from tkinter import *
from tkinter import Menu
import datetime as dt
import tkinter as tk
import requests
import json
import os
from PIL import Image, ImageTk
from idlelib.tooltip import Hovertip


window = tk.Tk()
window.title('CAT - Crypto Analysis Tool')
window.geometry("378x380+620+220")
window.iconbitmap('icons/coinworld.ico')
window.grid_columnconfigure(0, weight=1)

var_1 = StringVar()
var_2 = StringVar()
var_3 = StringVar()


def calc():
    calculator = ("C:\Windows\System32\calc.exe")
    os.system(calculator)   


# **** Realtime Price Functions ****

def btc_cpr():    
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'
    
    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)               
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  BTC  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("Bitcoin")    


def eth_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)               
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  ETH  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("Ethereum")


def ada_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=ADA&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)                
        
        date_time.insert(tk.END, date_time)
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  ADA  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("Cardano")


def xlm_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=XLM&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)                
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  XLM  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("Stellar Lumens")


def dgb_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=DGB&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)                
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  DGB  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("DigiByte")


def trx_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=TRX&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)                
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  TRX  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("Tron")


def xrp_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)                
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  XRP  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("Ripple")


def doge_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)                
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  DOGE  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("Dogecoin")


def dot_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=DOT&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)                
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  DOT  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("Polkadot")


def link_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=LINK&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)                
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  LINK  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("Chainlink")


def xmr_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)                
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  XMR  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("Monero")


def ltc_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)                
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  LTC  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("Litecoin")


def bnb_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=BNB&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)                
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  BNB  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("Binance Coin")


def bch_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=BCH&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)                
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  BCH  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("Bitcoin Cash")


def vet_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=VET&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)                
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  VET  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("VeChain")


def eos_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=EOS&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)                
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  EOS  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("EOS")


def neo_cpr():
    URL = 'https://min-api.cryptocompare.com/data/price?fsym=NEO&tsyms=USD'

    try:
        response = requests.request("GET", URL)
        currentPrice = json.loads(response.text)                
        
        date_time.insert(tk.END, date_time)        
                           
    except:
         text_data = var_1
         text_data.set(currentPrice)
         date_time = dt.datetime.now()
         date_time = date_time.strftime("%m/%d/%y, %H:%M:%S")
         txtt=str(date_time)+ "  NEO  "  + str(currentPrice)
         text_data.set(txtt)
    finally:
         text_data = var_2
         text_data.set("NEO")
         

# **** Candlestick Chart Functions ****

def btc():
    crypto = "BTC"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    btc1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(btc1, type="candle", volume=True, style="yahoo")


def eth():
    crypto = "ETH"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    eth1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(eth1, type="candle", volume=True, style="yahoo")


def ada():
    crypto = "ADA"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    ada1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(ada1, type="candle", volume=True, style="yahoo")


def xlm():
    crypto = "XLM"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    xlm1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(xlm1, type="candle", volume=True, style="yahoo")


def dgb():
    crypto = "DGB"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    dgb1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(dgb1, type="candle", volume=True, style="yahoo")


def eos():
    crypto = "EOS"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    dgb1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(dgb1, type="candle", volume=True, style="yahoo")


def trx():
    crypto = "TRX"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    trx1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(trx1, type="candle", volume=True, style="yahoo")


def xrp():
    crypto = "XRP"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    xrp1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(xrp1, type="candle", volume=True, style="yahoo")


def doge():
    crypto = "DOGE"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    xrp1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(xrp1, type="candle", volume=True, style="yahoo")


def dot():
    crypto = "DOT1"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    dot1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(dot1, type="candle", volume=True, style="yahoo")


def link():
    crypto = "LINK"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    link1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(link1, type="candle", volume=True, style="yahoo")


def xmr():
    crypto = "XMR"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    xmr1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(xmr1, type="candle", volume=True, style="yahoo")


def neo():
    crypto = "NEO"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    xmr1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(xmr1, type="candle", volume=True, style="yahoo")


def ltc():
    crypto = "LTC"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    ltc1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(ltc1, type="candle", volume=True, style="yahoo")


def bnb():
    crypto = "BNB"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    bnb1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(bnb1, type="candle", volume=True, style="yahoo")


def bch():
    crypto = "BCH"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    bch1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(bch1, type="candle", volume=True, style="yahoo")


def vet():
    crypto = "VET"
    currency = "USD"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    vet1 = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
    mpf.plot(vet1, type="candle", volume=True, style="yahoo")


# **** Logarithmic Chart Functions ****

def btc_log():    
    currency = "USD"
    metric = "Close"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    crypto = ['BTC', 'ETH', 'LTC']
    colnames = []

    first = True

    for ticker in crypto:
        data = web.DataReader(f'{ticker}-{currency}', 'yahoo', start, end)
        if first:
              combined = data[[metric]].copy()
              colnames.append(ticker)
              combined.columns = colnames
              first = False
        else:
            combined = combined.join(data[metric])
            colnames.append(ticker)
            combined.columns = colnames

    plt.yscale('log')

    for ticker in crypto:
        plt.plot(combined[ticker], label=ticker)

    plt.legend(loc="upper right")

    plt.show()


def ada_log():    
    currency = "USD"
    metric = "Close"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    crypto = ['BTC', 'ADA', 'XLM']
    colnames = []

    first = True

    for ticker in crypto:
        data = web.DataReader(f'{ticker}-{currency}', 'yahoo', start, end)
        if first:
              combined = data[[metric]].copy()
              colnames.append(ticker)
              combined.columns = colnames
              first = False
        else:
            combined = combined.join(data[metric])
            colnames.append(ticker)
            combined.columns = colnames

    plt.yscale('log')

    for ticker in crypto:
        plt.plot(combined[ticker], label=ticker)

    plt.legend(loc="upper right")

    plt.show()


def xlm_log():    
    currency = "USD"
    metric = "Close"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    crypto = ['BTC', 'DGB', 'XRP']
    colnames = []

    first = True

    for ticker in crypto:
        data = web.DataReader(f'{ticker}-{currency}', 'yahoo', start, end)
        if first:
              combined = data[[metric]].copy()
              colnames.append(ticker)
              combined.columns = colnames
              first = False
        else:
            combined = combined.join(data[metric])
            colnames.append(ticker)
            combined.columns = colnames

    plt.yscale('log')

    for ticker in crypto:
        plt.plot(combined[ticker], label=ticker)

    plt.legend(loc="upper right")

    plt.show()


def trx_log():    
    currency = "USD"
    metric = "Close"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    crypto = ['BTC', 'TRX', 'DOGE']
    colnames = []

    first = True

    for ticker in crypto:
        data = web.DataReader(f'{ticker}-{currency}', 'yahoo', start, end)
        if first:
              combined = data[[metric]].copy()
              colnames.append(ticker)
              combined.columns = colnames
              first = False
        else:
            combined = combined.join(data[metric])
            colnames.append(ticker)
            combined.columns = colnames

    plt.yscale('log')

    for ticker in crypto:
        plt.plot(combined[ticker], label=ticker)

    plt.legend(loc="upper right")

    plt.show()


def dot_log():    
    currency = "USD"
    metric = "Close"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    crypto = ['BTC', 'DOT1', 'LINK']
    colnames = []

    first = True

    for ticker in crypto:
        data = web.DataReader(f'{ticker}-{currency}', 'yahoo', start, end)
        if first:
              combined = data[[metric]].copy()
              colnames.append(ticker)
              combined.columns = colnames
              first = False
        else:
            combined = combined.join(data[metric])
            colnames.append(ticker)
            combined.columns = colnames

    plt.yscale('log')

    for ticker in crypto:
        plt.plot(combined[ticker], label=ticker)

    plt.legend(loc="upper right")

    plt.show()


def eos_log():    
    currency = "USD"
    metric = "Close"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    crypto = ['BTC', 'NEO', 'EOS']
    colnames = []

    first = True

    for ticker in crypto:
        data = web.DataReader(f'{ticker}-{currency}', 'yahoo', start, end)
        if first:
              combined = data[[metric]].copy()
              colnames.append(ticker)
              combined.columns = colnames
              first = False
        else:
            combined = combined.join(data[metric])
            colnames.append(ticker)
            combined.columns = colnames

    plt.yscale('log')

    for ticker in crypto:
        plt.plot(combined[ticker], label=ticker)

    plt.legend(loc="upper right")

    plt.show()


def xmr_log():    
    currency = "USD"
    metric = "Close"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    crypto = ['BTC', 'XMR', 'BNB']
    colnames = []

    first = True

    for ticker in crypto:
        data = web.DataReader(f'{ticker}-{currency}', 'yahoo', start, end)
        if first:
              combined = data[[metric]].copy()
              colnames.append(ticker)
              combined.columns = colnames
              first = False
        else:
            combined = combined.join(data[metric])
            colnames.append(ticker)
            combined.columns = colnames

    plt.yscale('log')

    for ticker in crypto:
        plt.plot(combined[ticker], label=ticker)

    plt.legend(loc="upper right")

    plt.show()


def bch_log():    
    currency = "USD"
    metric = "Close"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    crypto = ['BTC', 'BCH', 'VET']
    colnames = []

    first = True

    for ticker in crypto:
        data = web.DataReader(f'{ticker}-{currency}', 'yahoo', start, end)
        if first:
              combined = data[[metric]].copy()
              colnames.append(ticker)
              combined.columns = colnames
              first = False
        else:
            combined = combined.join(data[metric])
            colnames.append(ticker)
            combined.columns = colnames

    plt.yscale('log')

    for ticker in crypto:
        plt.plot(combined[ticker], label=ticker)

    plt.legend(loc="upper right")

    plt.show()


# **** Heatmap Chart Function ****

def btc_all_heat():
    currency = "USD"
    metric = "Close"

    start = dt.datetime(2020, 1, 1)
    end = dt.datetime.now()

    crypto = ['BTC', 'ETH', 'ADA', 'XLM', 'DGB', 'TRX', 'XRP', 'NEO', 'DOGE', 'DOT1', 'LINK', 'XMR', 'LTC', 'EOS',
              'BNB', 'BCH', 'VET']
    colnames = []

    first = True

    for ticker in crypto:
        data = web.DataReader(f'{ticker}-{currency}', 'yahoo', start, end)
        if first:
              combined = data[[metric]].copy()
              colnames.append(ticker)
              combined.columns = colnames
              first = False
        else:
            combined = combined.join(data[metric])
            colnames.append(ticker)
            combined.columns = colnames

    combined = combined.pct_change().corr(method="pearson")

    sns.heatmap(combined, annot=True, cmap="coolwarm")
    plt.get_current_fig_manager().window.state('zoomed')
    plt.show()
        

# **** Assigned to Exit Command ****

def close():
    window.destroy()


# **** Cascading Menus ****

# **** Candlestick Charts ****
menu = Menu(window)
window.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="Candlestick", menu=subMenu)
subMenu.add_command(label="Candlestick Charts", font=8, foreground="#88bb65")
subMenu.add_command(label="BTC - Bitcoin", command=btc)
subMenu.add_command(label="ETH - Etherium", command=eth)
subMenu.add_command(label="ADA - Cardano", command=ada)
subMenu.add_command(label="XLM - Stellar_Lumens", command=xlm)
subMenu.add_command(label="DGB - Digibyte", command=dgb)
subMenu.add_command(label="EOS - EOS", command=eos)
subMenu.add_command(label="TRX - Tron", command=trx)
subMenu.add_command(label="XRP - Ripple", command=xrp)
subMenu.add_command(label="DOGE - Dogecoin", command=doge)
subMenu.add_command(label="DOT - Polkadot", command=dot)
subMenu.add_command(label="LINK - Chainlink", command=link)
subMenu.add_command(label="XMR - Monero", command=xmr)
subMenu.add_command(label="NEO - NEO", command=neo)
subMenu.add_command(label="LTC - Litecoin", command=ltc)
subMenu.add_command(label="BNB - Binance_Coin", command=bnb)
subMenu.add_command(label="BCH - Bitcoin_Cash", command=bch)
subMenu.add_command(label="VET - VeChain", command=vet)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=close)


# **** Logarithmic Charts ****
subMenu = Menu(menu)
menu.add_cascade(label="Logarithmic", menu=subMenu)
subMenu.add_command(label="Logarithmic Charts", font=8, foreground="#88bb65")
subMenu.add_command(label="BTC - ETH - LTC", command=btc_log)
subMenu.add_command(label="BTC - ADA - XLM", command=ada_log)
subMenu.add_command(label="BTC - DGB - XRP", command=xlm_log)
subMenu.add_command(label="BTC - TRX - DOGE", command=trx_log)
subMenu.add_command(label="BTC - DOT - LINK", command=dot_log)
subMenu.add_command(label="BTC - NEO - EOS", command=eos_log)
subMenu.add_command(label="BTC - XMR - BNB", command=xmr_log)
subMenu.add_command(label="BTC - BCH - VET", command=bch_log)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=close)


# **** Heatmap Chart ****
subMenu = Menu(menu)
menu.add_cascade(label="Heatmap", menu=subMenu)
subMenu.add_command(label="Heatmap Chart", font=8, foreground="#88bb65")
subMenu.add_command(label="Pearson Correlation", font=8, foreground="#88bb65")
subMenu.add_command(label="BTC - ALL", command=btc_all_heat)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=close)


# **** Crypto Prices Realtime ****
subMenu = Menu(menu)
menu.add_cascade(label="CPR", menu=subMenu)
subMenu.add_command(label="Crypto Prices Realtime", font=8, foreground="#88bb65")
subMenu.add_command(label="BTC - Bitcoin", command=btc_cpr)
subMenu.add_command(label="ETH - Etherium", command=eth_cpr)
subMenu.add_command(label="ADA - Cardano", command=ada_cpr)
subMenu.add_command(label="XLM - Stellar_Lumens", command=xlm_cpr)
subMenu.add_command(label="DGB - Digibyte", command=dgb_cpr)
subMenu.add_command(label="EOS - EOS", command=eos_cpr)
subMenu.add_command(label="TRX - Tron", command=trx_cpr)
subMenu.add_command(label="XRP - Ripple", command=xrp_cpr)
subMenu.add_command(label="DOGE - Dogecoin", command=doge_cpr)
subMenu.add_command(label="DOT - Polkadot", command=dot_cpr)
subMenu.add_command(label="LINK - Chainlink", command=link_cpr)
subMenu.add_command(label="XMR - Monero", command=xmr_cpr)
subMenu.add_command(label="NEO - Neo", command=neo_cpr)
subMenu.add_command(label="LTC - Litecoin", command=ltc_cpr)
subMenu.add_command(label="BNB - Binance_Coin", command=bnb_cpr)
subMenu.add_command(label="BCH - Bitcoin_Cash", command=bch_cpr)
subMenu.add_command(label="VET - VeChain", command=vet_cpr)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=close)


# **** Toolbar Images ****
img1 = Image.open(r'icons/btc.png')
useImg1 = ImageTk.PhotoImage(img1)
img2 = Image.open(r'icons/eth.png')
useImg2 = ImageTk.PhotoImage(img2)
img3 = Image.open(r'icons/ada.png')
useImg3 = ImageTk.PhotoImage(img3)
img4 = Image.open(r'icons/xlm.png')
useImg4 = ImageTk.PhotoImage(img4)
img5 = Image.open(r'icons/dgb.png')
useImg5 = ImageTk.PhotoImage(img5)
img6 = Image.open(r'icons/trx.png')
useImg6 = ImageTk.PhotoImage(img6)
img7 = Image.open(r'icons/xrp.png')
useImg7 = ImageTk.PhotoImage(img7)
img8 = Image.open(r'icons/doge.png')
useImg8 = ImageTk.PhotoImage(img8)
img9 = Image.open(r'icons/eos.png')
useImg9 = ImageTk.PhotoImage(img9)


# **** Toolbar Images 2 ****
img11 = Image.open(r'icons/dot.png')
useImg11 = ImageTk.PhotoImage(img11)
img12 = Image.open(r'icons/link.png')
useImg12 = ImageTk.PhotoImage(img12)
img13 = Image.open(r'icons/xmr.png')
useImg13 = ImageTk.PhotoImage(img13)
img14 = Image.open(r'icons/ltc.png')
useImg14 = ImageTk.PhotoImage(img14)
img15 = Image.open(r'icons/bnb.png')
useImg15 = ImageTk.PhotoImage(img15)
img16 = Image.open(r'icons/bch.png')
useImg16 = ImageTk.PhotoImage(img16)
img17 = Image.open(r'icons/vet.png')
useImg17 = ImageTk.PhotoImage(img17)
img18 = Image.open(r'icons/neo.png')
useImg18 = ImageTk.PhotoImage(img18)
img19 = Image.open(r'icons/Calculator.png')
useImg19 = ImageTk.PhotoImage(img19)


# ***** Toolbar *****
toolbar = Frame(window, bg="#dedcdc")
insertB1 = Button(toolbar, image=useImg1, activebackground='#00ff00', command=btc_cpr)
Tip1 = Hovertip(insertB1, 'Bitcoin')
insertB1.pack(side=LEFT, padx=2, pady=2)
insertB2 = Button(toolbar, image=useImg2, activebackground='#00ff00', command=eth_cpr)
Tip2 = Hovertip(insertB2, 'Ethereum')
insertB2.pack(side=LEFT, padx=2, pady=2)
insertB3 = Button(toolbar, image=useImg3, activebackground='#00ff00', command=ada_cpr)
Tip3 = Hovertip(insertB3, 'Cardano')
insertB3.pack(side=LEFT, padx=2, pady=2)
insertB4 = Button(toolbar, image=useImg4, activebackground='#00ff00', command=xlm_cpr)
Tip4 = Hovertip(insertB4, 'Stellar Lumens')
insertB4.pack(side=LEFT, padx=2, pady=2)
insertB5 = Button(toolbar, image=useImg5, activebackground='#00ff00', command=dgb_cpr)
Tip5 = Hovertip(insertB5, 'DigiByte')
insertB5.pack(side=LEFT, padx=2, pady=2)
insertB6 = Button(toolbar, image=useImg6, activebackground='#00ff00', command=trx_cpr)
Tip6 = Hovertip(insertB6, 'Tron')
insertB6.pack(side=LEFT, padx=2, pady=2)
insertB7 = Button(toolbar, image=useImg7, activebackground='#00ff00', command=xrp_cpr)
Tip7 = Hovertip(insertB7, 'Ripple')
insertB7.pack(side=LEFT, padx=2, pady=2)
insertB8 = Button(toolbar, image=useImg8, activebackground='#00ff00', command=doge_cpr)
Tip8 = Hovertip(insertB8, 'Dogecoin')
insertB8.pack(side=LEFT, padx=2, pady=2)
insertB9 = Button(toolbar, image=useImg9, activebackground='#00ff00', command=eos_cpr)
Tip9 = Hovertip(insertB9, 'EOS')
insertB9.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

# ***** Toolbar 2 *****
toolbar = Frame(window, bg="#dedcdc")
insertB11 = Button(toolbar, image=useImg11, activebackground='#00ff00', command=dot_cpr)
Tip11 = Hovertip(insertB11, 'Polkadot')
insertB11.pack(side=LEFT, padx=2, pady=2)
insertB12 = Button(toolbar, image=useImg12, activebackground='#00ff00', command=link_cpr)
Tip12 = Hovertip(insertB12, 'Chainlink')
insertB12.pack(side=LEFT, padx=2, pady=2)
insertB13 = Button(toolbar, image=useImg13, activebackground='#00ff00', command=xmr_cpr)
Tip13 = Hovertip(insertB13, 'Monero')
insertB13.pack(side=LEFT, padx=2, pady=2)
insertB14 = Button(toolbar, image=useImg14, activebackground='#00ff00', command=ltc_cpr)
Tip14 = Hovertip(insertB14, 'Litecoin')
insertB14.pack(side=LEFT, padx=2, pady=2)
insertB15 = Button(toolbar, image=useImg15, activebackground='#00ff00', command=bnb_cpr)
Tip15 = Hovertip(insertB15, 'Binance Coin')
insertB15.pack(side=LEFT, padx=2, pady=2)
insertB16 = Button(toolbar, image=useImg16, activebackground='#00ff00', command=bch_cpr)
Tip16 = Hovertip(insertB16, 'Bitcoin Cash')
insertB16.pack(side=LEFT, padx=2, pady=2)
insertB17 = Button(toolbar, image=useImg17, activebackground='#00ff00', command=vet_cpr)
Tip17 = Hovertip(insertB17, 'VeChain')
insertB17.pack(side=LEFT, padx=2, pady=2)
insertB18 = Button(toolbar, image=useImg18, activebackground='#00ff00', command=neo_cpr)
Tip18 = Hovertip(insertB18, 'Neo')
insertB18.pack(side=LEFT, padx=2, pady=2)
insertB19 = Button(toolbar, image=useImg19, activebackground='#00ff00', command=calc)
Tip19 = Hovertip(insertB19, 'Calculator')
insertB19.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)


# **** Text Label ****

textlabel = Label(window, text="CPR - Crypto Prices Realtime", font=('arial', 11), fg="#88bb65", bd=4, anchor=CENTER)
textlabel.pack(fill=X, pady=6)


# **** Text Name ****

textbox = Label(window, text=[tk.StringVar], font=('arial', 12), bd=2, anchor=CENTER,
                textvariable=var_2)
textbox.pack(side=TOP, fill=X, padx=28, pady=2)


# **** Textbox ****

textbox = Label(window, text=[tk.StringVar], font=('arial', 10), bg="#ffffff", bd=4, relief=SUNKEN, anchor=CENTER,
                textvariable=var_1)
textbox.pack(side=TOP, fill=X, padx=30, pady=1)


# **** Coin Rank ****

textbox = Label(window, text=[tk.StringVar], font=('arial', 12), bd=2, anchor=CENTER,
                textvariable=var_3)
textbox.pack(side=TOP, fill=X, padx=28, pady=2)


# **** Status Bar ****

status = Label(window, text="Crypto Analysis Tool: David Spies", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

if __name__ == "__main__":
    window.mainloop()
