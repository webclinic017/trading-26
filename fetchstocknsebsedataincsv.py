import logging
import datetime
import statistics
import numpy as np
from alice_blue import *
import pandas as pd
import csv
import os
import time
import schedule

today = (datetime.date.today())
check= os.path.isfile(f'./{today}.csv')
print(check)
stock = ['AXISBANK', 'HDFCBANK', 'ICICIBANK', 'KOTAKBANK']
fields = [f'{stock[0]}',f'{stock[1]}',f'{stock[2]}',f'{stock[3]}',f'{stock[0]}volume',f'{stock[1]}volume',f'{stock[2]}volume',f'{stock[3]}volume',f'{stock[0]}bid',f'{stock[1]}bid',f'{stock[2]}bid',f'{stock[3]}bid',f'{stock[0]}ask',f'{stock[1]}ask',f'{stock[2]}ask',f'{stock[3]}ask',f'{stock[0]}bidvolume',f'{stock[0]}askvolume',f'{stock[1]}bidvolume',f'{stock[1]}askvolume',f'{stock[2]}bidvolume',f'{stock[2]}askvolume',f'{stock[3]}bidvolume',f'{stock[3]}askvolume',f'{stock[0]}bse',f'{stock[1]}bse',f'{stock[2]}bse',f'{stock[3]}bse',f'{stock[0]}bsevolume',f'{stock[1]}bsevolume',f'{stock[2]}bsevolume',f'{stock[3]}bsevolume',f'{stock[0]}bsebid',f'{stock[1]}bsebid',f'{stock[2]}bsebid',f'{stock[3]}bsebid',f'{stock[0]}bseask',f'{stock[1]}bseask',f'{stock[2]}bseask',f'{stock[3]}bseask',f'{stock[0]}bsebidvolume',f'{stock[0]}bseaskvolume',f'{stock[1]}bsebidvolume',f'{stock[1]}bseaskvolume',f'{stock[2]}bsebidvolume',f'{stock[2]}bseaskvolume',f'{stock[3]}bsebidvolume',f'{stock[3]}bseaskvolume',f'{stock[0]}FUT',f'{stock[1]}FUT',f'{stock[2]}FUT',f'{stock[3]}FUT',f'{stock[0]}FUTvolume',f'{stock[1]}FUTvolume',f'{stock[2]}FUTvolume',f'{stock[3]}FUTvolume',f'{stock[0]}FUTbid',f'{stock[1]}FUTbid',f'{stock[2]}FUTbid',f'{stock[3]}FUTbid',f'{stock[0]}FUTask',f'{stock[1]}FUTask',f'{stock[2]}FUTask',f'{stock[3]}FUTask',f'{stock[0]}FUTbidvolume',f'{stock[0]}FUTaskvolume',f'{stock[1]}FUTbidvolume',f'{stock[1]}FUTaskvolume',f'{stock[2]}FUTbidvolume',f'{stock[2]}FUTaskvolume',f'{stock[3]}FUTbidvolume',f'{stock[3]}FUTaskvolume',f'{stock[0]}vwap',f'{stock[0]}bidvwap',f'{stock[0]}askvwap',f'{stock[1]}vwap',f'{stock[1]}bidvwap',f'{stock[1]}askvwap',f'{stock[2]}vwap',f'{stock[2]}bidvwap',f'{stock[2]}askvwap',f'{stock[3]}vwap',f'{stock[3]}bidvwap',f'{stock[3]}askvwap']
if check == False:
    print(f"creating {today}.csv file")
    filename = f"{today}.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)



filename = f"{today}"
forthreshmv = pd.read_csv(f"{today}.csv")


username = ''
password = ''
api_secret = ''
twoFA = 'a'
logging.basicConfig(level=logging.DEBUG)  # Optional for getting debug messages.
# Config
grit = []
ltplist = []
moneylist = []

stock1bid = 0
stock1ask = 0
stock2bid = 0
stock2ask = 0
stock3bid = 0
stock3ask = 0
stock4bid = 0
stock4ask = 0
stock1bidvolume = 0
stock1askvolume = 0
stock2bidvolume = 0
stock2askvolume = 0
stock3bidvolume = 0
stock3askvolume = 0
stock4bidvolume = 0
stock4askvolume = 0
futstock1bid = 0
futstock1ask = 0
futstock2bid = 0
futstock2ask = 0
futstock3bid = 0
futstock3ask = 0
futstock4bid = 0
futstock4ask = 0
futstock5bid = 0
futstock5ask = 0
futstock1bidvolume = 0
futstock1askvolume= 0
futstock2bidvolume = 0
futstock2askvolume= 0
futstock3bidvolume = 0
futstock3askvolume= 0
futstock4bidvolume = 0
futstock4askvolume= 0
futstock5bidvolume = 0
futstock5askvolume= 0
ltp1 = 0
ltp2 = 0
ltp3 = 0
ltp4 = 0
ltp1volume = 0
ltp2volume = 0
ltp3volume = 0
ltp4volume = 0
ltp1FUT = 0
ltp2FUT = 0
ltp3FUT = 0
ltp4FUT = 0
ltp5FUT = 0
ltp1FUTvolume = 0
ltp2FUTvolume = 0
ltp3FUTvolume = 0
ltp4FUTvolume = 0
ltp5FUTvolume = 0
ltp1bse = 0
ltp1bsevolume = 0
ltp2bse = 0
ltp2bsevolume = 0
ltp3bse = 0
ltp3bsevolume = 0
ltp4bse = 0
ltp4bsevolume = 0
stock1bsebid = 0
stock1bseask = 0
stock2bsebid = 0
stock2bseask = 0
stock3bsebid = 0
stock3bseask = 0
stock4bsebid = 0
stock4bseask = 0
stock1bsebidvolume = 0
stock1bseaskvolume = 0
stock2bsebidvolume = 0
stock2bseaskvolume = 0
stock3bsebidvolume = 0
stock3bseaskvolume = 0
stock4bsebidvolume = 0
stock4bseaskvolume = 0
ratios = []

tod = "return"
socket_opened = False
alice = None
month = 'JUL'
expdate = datetime.date(2020, 7, 30)
secondslist = []

print("started")



def event_handler_quote_update(message):
    global ltp1
    global ltp1volume
    global ltp2
    global ltp2volume
    global ltp3
    global ltp3volume
    global ltp4
    global ltp4volume
    global stock1bid
    global stock1ask
    global stock2bid
    global stock2ask
    global stock3bid
    global stock3ask
    global stock4bid
    global stock4ask
    global stock1bidvolume
    global stock1askvolume
    global stock2bidvolume
    global stock2askvolume
    global stock3bidvolume
    global stock3askvolume
    global stock4bidvolume
    global stock4askvolume
    global ltp1bse
    global ltp1bsevolume
    global ltp2bse
    global ltp2bsevolume
    global ltp3bse
    global ltp3bsevolume
    global ltp4bse
    global ltp4bsevolume
    global stock1bsebid
    global stock1bseask
    global stock2bsebid
    global stock2bseask
    global stock3bsebid
    global stock3bseask
    global stock4bsebid
    global stock4bseask
    global stock1bsebidvolume
    global stock1bseaskvolume
    global stock2bsebidvolume
    global stock2bseaskvolume
    global stock3bsebidvolume
    global stock3bseaskvolume
    global stock4bsebidvolume
    global stock4bseaskvolume
    global ltp1FUT
    global ltp1FUTvolume
    global ltp2FUT
    global ltp2FUTvolume
    global ltp3FUT
    global ltp3FUTvolume
    global ltp4FUTvolume
    global ltp4FUT
    global ltp4FUTvolume
    global futstock1bid
    global futstock1ask
    global futstock2bid
    global futstock2ask
    global futstock3bid
    global futstock3ask
    global futstock4bid
    global futstock4ask
    global futstock1bidvolume
    global futstock1askvolume
    global futstock2bidvolume
    global futstock2askvolume
    global futstock3bidvolume
    global futstock3askvolume
    global futstock4bidvolume
    global futstock4askvolume

    if message['instrument'][2] == stock[0]:
        ltp1 = ((message)['ltp'])
        ltp1volume = ((message)['volume'])
        stock1bid = ((message)['best_bid_price'])
        stock1ask = ((message)['best_ask_price'])
        stock1bidvolume = message['best_bid_quantity']
        stock1askvolume = message['best_ask_quantity']



    elif message['instrument'][2] == stock[1]:
        ltp2 = ((message)['ltp'])
        ltp2volume = ((message)['volume'])
        stock2bid = ((message)['best_bid_price'])
        stock2ask = ((message)['best_ask_price'])
        stock2bidvolume = message['best_bid_quantity']
        stock2askvolume = message['best_ask_quantity']


    elif message['instrument'][2] == stock[2]:
        ltp3 = ((message)['ltp'])
        ltp3volume = ((message)['volume'])
        stock3bid = ((message)['best_bid_price'])
        stock3ask = ((message)['best_ask_price'])
        stock3bidvolume = message['best_bid_quantity']
        stock3askvolume = message['best_ask_quantity']



    elif message['instrument'][2] == stock[3]:
        ltp4 = ((message)['ltp'])
        ltp4volume = ((message)['volume'])
        stock4bid = ((message)['best_bid_price'])
        stock4ask = ((message)['best_ask_price'])
        stock4bidvolume = message['best_bid_quantity']
        stock4askvolume = message['best_ask_quantity']


    elif message['instrument'][2] == (f"{stock[0]} A"):
        ltp1bse = ((message)['ltp'])
        ltp1bsevolume = ((message)['volume'])
        stock1bsebid = ((message)['best_bid_price'])
        stock1bseask = ((message)['best_ask_price'])
        stock1bsebidvolume = message['best_bid_quantity']
        stock1bseaskvolume = message['best_ask_quantity']



    elif message['instrument'][2] == (f"{stock[1]} A"):
        ltp2bse = ((message)['ltp'])
        ltp2bsevolume = ((message)['volume'])
        stock2bsebid = ((message)['best_bid_price'])
        stock2bseask = ((message)['best_ask_price'])
        stock2bsebidvolume = message['best_bid_quantity']
        stock2bseaskvolume = message['best_ask_quantity']

    elif message['instrument'][2] == (f"{stock[2]} A"):
        ltp3bse = ((message)['ltp'])
        ltp3bsevolume = ((message)['volume'])
        stock3bsebid = ((message)['best_bid_price'])
        stock3bseask = ((message)['best_ask_price'])
        stock3bsebidvolume = message['best_bid_quantity']
        stock3bseaskvolume = message['best_ask_quantity']



    elif message['instrument'][2] == (f"{stock[3]} A"):
        ltp4bse = ((message)['ltp'])
        ltp4bsevolume = ((message)['volume'])
        stock4bsebid = ((message)['best_bid_price'])
        stock4bseask = ((message)['best_ask_price'])
        stock4bsebidvolume = message['best_bid_quantity']
        stock4bseaskvolume = message['best_ask_quantity']


    elif message['instrument'][2] == (f"{stock[0]} {month} FUT"):
        ltp1FUT = ((message)['ltp'])
        ltp1FUTvolume = ((message)['volume'])
        futstock1bid = ((message)['best_bid_price'])
        futstock1ask = ((message)['best_ask_price'])
        futstock1bidvolume = message['best_bid_quantity']
        futstock1askvolume = message['best_ask_quantity']




    elif message['instrument'][2] == (f"{stock[1]} {month} FUT"):
        ltp2FUT = ((message)['ltp'])
        ltp2FUTvolume = ((message)['volume'])

        futstock2bid = ((message)['best_bid_price'])
        futstock2ask = ((message)['best_ask_price'])
        futstock2bidvolume = message['best_bid_quantity']
        futstock2askvolume = message['best_ask_quantity']

    elif message['instrument'][2] == (f"{stock[2]} {month} FUT"):
        ltp3FUT = ((message)['ltp'])
        ltp3FUTvolume = ((message)['volume'])

        futstock3bid = ((message)['best_bid_price'])
        futstock3ask = ((message)['best_ask_price'])
        futstock3bidvolume = message['best_bid_quantity']
        futstock3askvolume = message['best_ask_quantity']



    elif message['instrument'][2] == (f"{stock[3]} {month} FUT"):
        ltp4FUT = ((message)['ltp'])
        ltp4FUTvolume = ((message)['volume'])

        futstock4bid = ((message)['best_bid_price'])
        futstock4ask = ((message)['best_ask_price'])
        futstock4bidvolume = message['best_bid_quantity']
        futstock4askvolume = message['best_ask_quantity']


def open_callback():
    global socket_opened
    socket_opened = True


def main():
    listgot = ['start1', 'start2']
    global socket_opened
    global alice
    global username
    global password
    global twoFA
    global api_secret
    global EMA_CROSS_SCRIP
    minute_close = []
    access_token = AliceBlue.login_and_get_access_token(username=username, password=password, twoFA=twoFA,
                                                        api_secret=api_secret)
    alice = AliceBlue(username=username, password=password, access_token=access_token,
                      master_contracts_to_download=['NSE', 'NFO', 'BSE'])

    socket_opened = False
    alice.start_websocket(subscribe_callback=event_handler_quote_update,
                          socket_open_callback=open_callback,
                          run_in_background=True)
    while (socket_opened == False):  # wait till socket open & then subscribe
        pass

    alice.subscribe([alice.get_instrument_by_symbol('NSE', stock[0]), alice.get_instrument_by_symbol('NSE', stock[1]),
                     alice.get_instrument_by_symbol('NSE', stock[2]), alice.get_instrument_by_symbol('NSE', stock[3]),
                     alice.get_instrument_for_fno(symbol=stock[0], expiry_date=expdate, is_fut=True,
                                                  strike=None, is_CE=False),
                     alice.get_instrument_for_fno(symbol=stock[1], expiry_date=expdate, is_fut=True,
                                                  strike=None, is_CE=False),
                     alice.get_instrument_for_fno(symbol=stock[2], expiry_date=expdate, is_fut=True,
                                                  strike=None, is_CE=False),
                     alice.get_instrument_for_fno(symbol=stock[3], expiry_date=expdate, is_fut=True,
                                                  strike=None, is_CE=False),
                     alice.get_instrument_by_symbol('BSE', f"{stock[0]} A"),
                     alice.get_instrument_by_symbol('BSE', f"{stock[1]} A"),
                     alice.get_instrument_by_symbol('BSE', f"{stock[2]} A"),
                     alice.get_instrument_by_symbol('BSE', f"{stock[3]} A")], LiveFeedType.MARKET_DATA)

    alice.get_all_subscriptions()
    print(alice.get_all_subscriptions())
    count = 1
    while True:
        now = datetime.datetime.now()
        time = now.strftime("%H:%M:%S")
        second = datetime.datetime.now().second
        if  (second not in secondslist) and (listgot[0] != listgot[1] )and  ( ( ltp1 and stock1bidvolume and stock1askvolume and stock1bid and stock1ask and futstock1bidvolume and futstock1askvolume ) != 0) :
            secondslist.append(second)
            if len(secondslist) > 1:
                secondslist.pop(0)
                if count % 3 != 0:
                    listgot[0] = [ltp1, ltp1FUT, stock1bidvolume, futstock1askvolume, stock1bid, stock1ask, futstock1bid,
                                  futstock1ask,
                                  ltp2, ltp2FUT, stock2bidvolume, futstock2askvolume, stock2bid, stock2ask, futstock2bid,
                                  futstock2ask,
                                  ltp3, ltp3FUT, stock3bidvolume, futstock3askvolume, stock3bid, stock3ask, futstock3bid,
                                  futstock3ask,
                                  ltp4, ltp4FUT, stock4bidvolume, futstock4askvolume, stock4bid, stock4ask, futstock4bid,
                                  futstock4ask]
                elif count % 3 == 0:
                    listgot[1] = [ltp1, ltp1FUT, stock1bidvolume, futstock1askvolume, stock1bid, stock1ask, futstock1bid,
                                  futstock1ask,
                                  ltp2, ltp2FUT, stock2bidvolume, futstock2askvolume, stock2bid, stock2ask, futstock2bid,
                                  futstock2ask,
                                  ltp3, ltp3FUT, stock3bidvolume, futstock3askvolume, stock3bid, stock3ask, futstock3bid,
                                  futstock3ask,
                                  ltp4, ltp4FUT, stock4bidvolume, futstock4askvolume, stock4bid, stock4ask, futstock4bid,
                                  futstock4ask]

                count += 1
                forthreshmv = pd.read_csv(f"{filename}.csv")

                if forthreshmv.shape[0] > 0:
                    ltp1vwap = ((np.cumsum(forthreshmv[f'{stock[0]}'] * forthreshmv[f'{stock[0]}volume']) + (ltp1 * ltp1volume)) / (
                        (np.cumsum(forthreshmv[f'{stock[0]}volume'])) + ltp1volume))[-1]
                    ltp1askvwap = ((np.cumsum(forthreshmv[f'{stock[0]}ask'] * forthreshmv[f'{stock[0]}askvolume']) + (stock1ask * stock1askvolume)) / (
                        (np.cumsum(forthreshmv[f'{stock[0]}askvolume'])) + stock1askvolume))[-1]
                    ltp1bidvwap = ((np.cumsum(forthreshmv[f'{stock[0]}bid'] * forthreshmv[f'{stock[0]}bidvolume']) + (stock1bid * stock1bidvolume)) / (
                        (np.cumsum(forthreshmv[f'{stock[0]}bidvolume'])) + stock1bidvolume))[-1]
                    ltp2vwap = ((np.cumsum(forthreshmv[f'{stock[1]}'] * forthreshmv[f'{stock[1]}volume']) + (ltp2 * ltp2volume)) / (
                        (np.cumsum(forthreshmv[f'{stock[1]}volume'])) + ltp2volume))[-1]
                    ltp2askvwap = ((np.cumsum(forthreshmv[f'{stock[1]}ask'] * forthreshmv[f'{stock[1]}askvolume']) + (stock2ask * stock2askvolume)) / (
                        (np.cumsum(forthreshmv[f'{stock[1]}askvolume'])) + stock2askvolume))[-1]
                    ltp2bidvwap = ((np.cumsum(forthreshmv[f'{stock[1]}bid'] * forthreshmv[f'{stock[1]}bidvolume']) + (stock2bid * stock2bidvolume)) / (
                        (np.cumsum(forthreshmv[f'{stock[1]}bidvolume'])) + stock2bidvolume))[-1]
                    ltp3vwap = ((np.cumsum(forthreshmv[f'{stock[2]}'] * forthreshmv[f'{stock[2]}volume']) + (ltp3 * ltp3volume)) / (
                        (np.cumsum(forthreshmv[f'{stock[2]}volume'])) + ltp3volume))[-1]
                    ltp3askvwap = ((np.cumsum(forthreshmv[f'{stock[2]}ask'] * forthreshmv[f'{stock[2]}askvolume']) + (stock3ask * stock3askvolume)) / (
                        (np.cumsum(forthreshmv[f'{stock[2]}askvolume'])) + stock3askvolume))[-1]
                    ltp3bidvwap = ((np.cumsum(forthreshmv[f'{stock[2]}bid'] * forthreshmv[f'{stock[2]}bidvolume']) + (stock3bid * stock3bidvolume)) / (
                        (np.cumsum(forthreshmv[f'{stock[2]}bidvolume'])) + stock3bidvolume))[-1]
                    ltp4vwap = ((np.cumsum(forthreshmv[f'{stock[3]}'] * forthreshmv[f'{stock[3]}volume']) + (ltp4 * ltp4volume)) / (
                        (np.cumsum(forthreshmv[f'{stock[3]}volume'])) + ltp4volume))[-1]
                    ltp4askvwap = ((np.cumsum(forthreshmv[f'{stock[3]}ask'] * forthreshmv[f'{stock[3]}askvolume']) + (stock4ask * stock4askvolume)) / (
                        (np.cumsum(forthreshmv[f'{stock[3]}askvolume'])) + stock4askvolume))[-1]
                    ltp4bidvwap = ((np.cumsum(forthreshmv[f'{stock[3]}bid'] * forthreshmv[f'{stock[3]}bidvolume']) + (stock4bid * stock4bidvolume)) / (
                        (np.cumsum(forthreshmv[f'{stock[3]}bidvolume'])) + stock4bidvolume))[-1]

                elif forthreshmv.shape[0] == 0 :
                    ltp1vwap = ltp1
                    ltp1askvwap = stock1ask
                    ltp1bidvwap = stock1bid
                    ltp2vwap = ltp2
                    ltp2askvwap = stock2ask
                    ltp2bidvwap = stock2bid
                    ltp3vwap = ltp3
                    ltp3askvwap = stock3ask
                    ltp3bidvwap = stock3bid
                    ltp4vwap = ltp4
                    ltp4askvwap = stock4ask
                    ltp4bidvwap = stock4bid

                df = pd.DataFrame(
                    {
                     f'{stock[0]}': ltp1, f'{stock[1]}': ltp2, f'{stock[2]}': ltp3, f'{stock[3]}': ltp4,
                     f'{stock[0]}volume': ltp1volume, f'{stock[1]}volume': ltp2volume, f'{stock[2]}volume': ltp3volume,
                     f'{stock[3]}volume': ltp4volume,
                     f'{stock[0]}bid': stock1bid, f'{stock[1]}bid': stock2bid, f'{stock[2]}bid': stock3bid,
                     f'{stock[3]}bid': stock4bid,
                     f'{stock[0]}ask': stock1ask, f'{stock[1]}ask': stock2ask, f'{stock[2]}ask': stock3ask,
                     f'{stock[3]}ask': stock4ask,
                     f'{stock[0]}bidvolume': stock1bidvolume, f'{stock[0]}askvolume': stock1askvolume,
                     f'{stock[1]}bidvolume': stock2bidvolume, f'{stock[1]}askvolume': stock2askvolume,
                     f'{stock[2]}bidvolume': stock3bidvolume, f'{stock[2]}askvolume': stock3askvolume,
                     f'{stock[3]}bidvolume': stock4bidvolume, f'{stock[3]}askvolume': stock4askvolume,
                     f'{stock[0]}bse': ltp1bse, f'{stock[1]}bse': ltp2bse, f'{stock[2]}bse': ltp3bse, f'{stock[3]}bse': ltp4bse,
                     f'{stock[0]}bsevolume': ltp1bsevolume, f'{stock[1]}bsevolume': ltp2bsevolume,
                     f'{stock[2]}bsevolume': ltp3bsevolume, f'{stock[3]}bsevolume': ltp4bsevolume,
                     f'{stock[0]}bsebid': stock1bsebid, f'{stock[1]}bsebid': stock2bsebid, f'{stock[2]}bsebid': stock3bsebid,
                     f'{stock[3]}bsebid': stock4bsebid,
                     f'{stock[0]}bseask': stock1bseask, f'{stock[1]}bseask': stock2bseask, f'{stock[2]}bseask': stock3bseask,
                     f'{stock[3]}bseask': stock4bseask,
                     f'{stock[0]}bsebidvolume': stock1bsebidvolume, f'{stock[0]}bseaskvolume': stock1bseaskvolume,
                     f'{stock[1]}bsebidvolume': stock2bsebidvolume, f'{stock[1]}bseaskvolume': stock2bseaskvolume,
                     f'{stock[2]}bsebidvolume': stock3bsebidvolume, f'{stock[2]}bseaskvolume': stock3bseaskvolume,
                     f'{stock[3]}bsebidvolume': stock4bsebidvolume, f'{stock[3]}bseaskvolume': stock4bseaskvolume,
                     f'{stock[0]}FUT': ltp1FUT, f'{stock[1]}FUT': ltp2FUT, f'{stock[2]}FUT': ltp3FUT, f'{stock[3]}FUT': ltp4FUT,
                     f'{stock[0]}FUTvolume': ltp1FUTvolume, f'{stock[1]}FUTvolume': ltp2FUTvolume,
                     f'{stock[2]}FUTvolume': ltp3FUTvolume,
                     f'{stock[3]}FUTvolume': ltp4FUTvolume,
                     f'{stock[0]}FUTbid': futstock1bid, f'{stock[1]}FUTbid': futstock2bid, f'{stock[2]}FUTbid': futstock3bid,
                     f'{stock[3]}FUTbid': futstock4bid,
                     f'{stock[0]}FUTask': futstock1ask, f'{stock[1]}FUTask': futstock2ask, f'{stock[2]}FUTask': futstock3ask,
                     f'{stock[3]}FUTask': futstock4ask,
                     f'{stock[0]}FUTbidvolume': futstock1bidvolume, f'{stock[0]}FUTaskvolume': futstock1askvolume,
                     f'{stock[1]}FUTbidvolume': futstock2bidvolume, f'{stock[1]}FUTaskvolume': futstock2askvolume,
                     f'{stock[2]}FUTbidvolume': futstock3bidvolume, f'{stock[2]}FUTaskvolume': futstock3askvolume,
                     f'{stock[3]}FUTbidvolume': futstock4bidvolume, f'{stock[3]}FUTaskvolume': futstock4askvolume,
                     f'{stock[0]}vwap': ltp1vwap, f'{stock[0]}bidvwap': ltp1bidvwap,
                     f'{stock[0]}askvwap': ltp1askvwap,
                     f'{stock[1]}vwap': ltp2vwap, f'{stock[1]}bidvwap': ltp2bidvwap,
                     f'{stock[1]}askvwap': ltp2askvwap,
                     f'{stock[2]}vwap': ltp3vwap, f'{stock[2]}bidvwap': ltp3bidvwap,
                     f'{stock[2]}askvwap': ltp3askvwap,
                     f'{stock[3]}vwap': ltp4vwap, f'{stock[3]}bidvwap': ltp4bidvwap,
                     f'{stock[3]}askvwap': ltp4askvwap
                     }, index=[time])
                df.to_csv(f"{filename}.csv", mode='a', header=False)
                print(df)

        elif (listgot[0] == listgot[1]):
            print(listgot[0])
            print(listgot[1])
            secondslist.clear()
            main()

if __name__ == '__main__':
    while True:
            main()


# AXISBANK,HDFCBANK,ICICIBANK,KOTAKBANK,AXISBANKvolume,HDFCBANKvolume,ICICIBANKvolume,KOTAKBANKvolume,AXISBANKbid,HDFCBANKbid,ICICIBANKbid,KOTAKBANKbid,AXISBANKask,HDFCBANKask,ICICIBANKask,KOTAKBANKask,AXISBANKbidvolume,AXISBANKaskvolume,HDFCBANKbidvolume,HDFCBANKaskvolume,ICICIBANKbidvolume,ICICIBANKaskvolume,KOTAKBANKbidvolume,KOTAKBANKaskvolume,AXISBANKbse,HDFCBANKbse,ICICIBANKbse,KOTAKBANKbse,AXISBANKbsevolume,HDFCBANKbsevolume,ICICIBANKbsevolume,KOTAKBANKbsevolume,AXISBANKbsebid,HDFCBANKbsebid,ICICIBANKbsebid,KOTAKBANKbsebid,AXISBANKbseask,HDFCBANKbseask,ICICIBANKbseask,KOTAKBANKbseask,AXISBANKbsebidvolume,AXISBANKbseaskvolume,HDFCBANKbsebidvolume,HDFCBANKbseaskvolume,ICICIBANKbsebidvolume,ICICIBANKbseaskvolume,KOTAKBANKbsebidvolume,KOTAKBANKbseaskvolume,AXISBANKFUT,HDFCBANKFUT,ICICIBANKFUT,KOTAKBANKFUT,AXISBANKFUTvolume,HDFCBANKFUTvolume,ICICIBANKFUTvolume,KOTAKBANKFUTvolume,AXISBANKFUTbid,HDFCBANKFUTbid,ICICIBANKFUTbid,KOTAKBANKFUTbid,AXISBANKFUTask,HDFCBANKFUTask,ICICIBANKFUTask,KOTAKBANKFUTask,AXISBANKFUTbidvolume,AXISBANKFUTaskvolume,HDFCBANKFUTbidvolume,HDFCBANKFUTaskvolume,ICICIBANKFUTbidvolume,ICICIBANKFUTaskvolume,KOTAKBANKFUTbidvolume,KOTAKBANKFUTaskvolume
# AXISBANK,HDFCBANK,ICICIBANK,KOTAKBANK,AXISBANKvolume,HDFCBANKvolume,ICICIBANKvolume,KOTAKBANKvolume,AXISBANKbid,HDFCBANKbid,ICICIBANKbid,KOTAKBANKbid,AXISBANKask,HDFCBANKask,ICICIBANKask,KOTAKBANKask,AXISBANKbidvolume,AXISBANKaskvolume,HDFCBANKbidvolume,HDFCBANKaskvolume,ICICIBANKbidvolume,ICICIBANKaskvolume,KOTAKBANKbidvolume,KOTAKBANKaskvolume,AXISBANKFUT,HDFCBANKFUT,ICICIBANKFUT,KOTAKBANKFUT,AXISBANKFUTvolume,HDFCBANKFUTvolume,ICICIBANKFUTvolume,KOTAKBANKFUTvolume,AXISBANKFUTbid,HDFCBANKFUTbid,ICICIBANKFUTbid,KOTAKBANKFUTbid,AXISBANKFUTask,HDFCBANKFUTask,ICICIBANKFUTask,KOTAKBANKFUTask,AXISBANKFUTbidvolume,AXISBANKFUTaskvolume,HDFCBANKFUTbidvolume,HDFCBANKFUTaskvolume,ICICIBANKFUTbidvolume,ICICIBANKFUTaskvolume,KOTAKBANKFUTbidvolume,KOTAKBANKFUTaskvolume
#1995-08-14 00:00:00.631137,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
