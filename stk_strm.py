from alpha_vantage.timeseries import TimeSeries
import pandas
from alpha_vantage.techindicators import TechIndicators as ti
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import time
from kafka import KafkaProducer

#HOST, PORT = "localhost", 9092

# Create a socket (SOCK_STREAM means a TCP socket)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

timeout = 3600   # [seconds]
timeout_start = time.time()

while time.time() < timeout_start + timeout:
    ts = TimeSeries(key='84HSVW90JOWIQ0X1',output_format='pandas')
    data, meta_data = ts.get_intraday(symbol='AAPL',interval='1min', outputsize = "compact")
    data.to_csv('/Users/kunalsharma/TechField/Python/Stock_stream/1 min/aapl_stock_ticker.csv', mode='a', index=True)
    #producer.send('stocks',(data + "\n"))
    time.sleep(300)
