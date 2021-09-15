import pandas as pd
import urllib.request
import requests
import csv
import numpy as np
from statsmodels.tsa.stattools import coint
import csv
import time

from datetime import datetime, timedelta
timeframe = pd.Timedelta('9 hours 30 min')


nifty = pd.read_csv("nifty50.csv")
print(nifty["Symbol"])
nifty50list = []
for i in nifty["Symbol"]:
    nifty50list.append(i)
print(nifty50list)

nifty50 = ['ADANIPORTS', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE', 'BAJAJFINSV', 'BPCL', 'BHARTIARTL', 'INFRATEL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DRREDDY', 'EICHERMOT', 'GAIL', 'GRASIM', 'HCLTECH', 'HDFCBANK', 'HEROMOTOCO', 'HINDALCO', 'HINDUNILVR', 'HDFC', 'ICICIBANK', 'ITC', 'IOC', 'INDUSINDBK', 'INFY', 'JSWSTEEL', 'KOTAKBANK', 'LT',  'MARUTI', 'NTPC', 'NESTLEIND', 'ONGC', 'POWERGRID', 'RELIANCE', 'SHREECEM', 'SBIN', 'SUNPHARMA', 'TCS', 'TATAMOTORS', 'TATASTEEL', 'TECHM', 'TITAN', 'UPL', 'ULTRACEMCO', 'VEDL', 'WIPRO', 'ZEEL']
niftybank = ['HDFCBANK','ICICIBANK']
stock = ["IDFCFIRSTB","SBIN", "PNB", "BANKBARODA", "RBLBANK", "FEDERALBNK", "HDFCBANK", "KOTAKBANK", "BANDHANBNK", "AXISBANK",
         "ICICIBANK", "INDUSINDBK"]




def gett():
    count = 0
    for i in niftybank:
            url = (
            "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=NSE:{}&outputsize=full&interval=1min&apikey=OK7426649A18Y5PR&datatype=csv".format(
                i))
            req = requests.get(url)
            url_content = req.content
            csv_file = open(('{}1min.csv'.format(i)), 'wb')

            csv_file.write(url_content)
            csv_file.close()
            print(url)
            print(count)
            count += 1
            #time.sleep(13)
gett()




def find_cointegrated_pairs(data):
    n = data.shape[1]
    score_matrix = np.zeros((n, n))
    pvalue_matrix = np.ones((n, n))
    keys = data.keys()
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            S1 = data[keys[i]]
            S2 = data[keys[j]]
            result = coint(S1, S2)
            score = result[0]
            pvalue = result[1]
            score_matrix[i, j] = score
            pvalue_matrix[i, j] = pvalue
            if pvalue == pvalue_matrix.min():
                pairs.append((keys[i], keys[j]))
    return score_matrix, pvalue_matrix, pairs



def cointtest():

    df1 = pd.DataFrame()
    for i in nifty50:
        data_frame = pd.read_csv("{}.csv".format(i))
        print(i)
        print(data_frame)
        data_frame["timestamp"] = pd.to_datetime(data_frame["timestamp"])

        # make the required change
        without_date = (data_frame["timestamp"]+ timeframe).apply(lambda d: d.time()).astype(str)
        data_frame["timestamp"] = without_date
        data_frame = data_frame.iloc[::-1].set_index("timestamp")
        df2 = (data_frame.rename(columns={"close": i})[i])
        df1[i] = df2
    print(df1)
    df3 = df1


    scores, pvalues, pairs = find_cointegrated_pairs(df3)

    print(scores)
    print(pvalues)
    print(pairs[-1])
    print(pvalues.min())
    return df3

df3 = cointtest()
print(df3)