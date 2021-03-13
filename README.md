## Crypto Analysis Tool

Written in python and utilizing Tkinter for the GUI. The Cryptocurrency Analysis Tool provides functionality to examine certain crypto's in candlestick, logarithmic, and heatmap charts. This tool also includes functionality to retrieve realtime prices from selected crypto's. 


## Prerequisites

The Crypto Analysis code should run on most Windows machines with very few dependencies. 
*Note - this program has not been tested outside the Windows environment.


## Installing / Running

* Download or Clone.
* Run code in your favorite IDE.
* Click on Candlestick, Logarithmic, or Heatmap to explore and launch charts.
* The Heatmap chart will launch and expand to entire window, resize to your preference.
* Click on CPR or select your favorite crypto icon on the toolbar to retrieve realtime prices. 
* The crypto icon selected and clicked will display the realtime price on the GUI when retrieved.


## Source Modules & Packages

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

## Dependencies

* Python 3.8

Built with python and Tkinter GUI library.


Authors

    David Spies
