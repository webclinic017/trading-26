import logging
from time import sleep
from alice_blue import *
import time
# Config
import numpy as np
import pandas as pd
import datetime
space = 1
forthreshmv = pd.read_csv("demon911.csv").iloc[::space,:]
username = ''
password = ''
api_secret = ''
twoFA = 'a'
logging.basicConfig(level=logging.DEBUG)  # Optional for getting debug messages.
# Config
instru = 'AXISBANK'
month = 'JUN'
diff11  = pd.read_csv("myfile.csv")['diff'].iloc[-1]
trail = pd.read_csv("myfile.csv")['trail'].iloc[-1]
trackbuy = []
tracksell = []
consta = []
checklist1 = ["START", "START", "START"]
check = "START"
forthreshmv = pd.read_csv("demon911.csv").iloc[::1, :]

socket_opened = False
alice = None
def zscore(series):
    return (series - series.mean()) / np.std(series)


def event_handler_quote_update(message):
    global ltp1
    global ltp1volume
    global ltp1FUT
    global ltp1FUTvolume
    global stock1bid
    global stock1ask
    global stock1bidvolume
    global stock1askvolume
    global futstock1bid
    global futstock1ask
    global futstock1bidvolume
    global futstock1askvolume

    if message['instrument'][2] == instru:
        ltp1 = (message)['ltp']
        ltp1volume = (message)['volume']
        stock1bid = ((message)['best_bid_price'])
        stock1ask = ((message)['best_ask_price'])
        stock1bidvolume = message['best_bid_quantity']
        stock1askvolume = message['best_ask_quantity']

    elif message['instrument'][2] == (f"{instru} {month} FUT"):
        ltp1FUT = (message)['ltp']
        ltp1FUTvolume = (message)['volume']
        futstock1bid = ((message)['best_bid_price'])
        futstock1ask = ((message)['best_ask_price'])
        futstock1bidvolume = message['best_bid_quantity']
        futstock1askvolume = message['best_ask_quantity']


def open_callback():
    global socket_opened
    socket_opened = True


def main():
    global socket_opened
    global alice
    global username
    global password
    global twoFA
    global api_secret
    global EMA_CROSS_SCRIP
    access_token = AliceBlue.login_and_get_access_token(username=username, password=password, twoFA=twoFA,
                                                        api_secret=api_secret)
    alice = AliceBlue(username=username, password=password, access_token=access_token,
                      master_contracts_to_download=['NSE', 'NFO'])
    print(alice.get_profile())  # get profile

    socket_opened = False
    alice.start_websocket(subscribe_callback=event_handler_quote_update,
                          socket_open_callback=open_callback,
                          run_in_background=True)
    while (socket_opened == False):  # wait till socket open & then subscribe
        pass
    stock11 = alice.get_instrument_by_symbol('NSE', instru)
    futstock11 = alice.get_instrument_for_fno(symbol=instru, expiry_date=datetime.date(2020, 6, 25), is_fut=True,
                                              strike=None, is_CE=False)
    alice.subscribe([stock11, futstock11], LiveFeedType.MARKET_DATA)

    print(alice.get_all_subscriptions())

    print("started")
    quantity = 5

    count = 0


    while True:
        #forthreshmv = pd.read_csv("demon911.csv")
        forthreshmv = pd.read_csv("demon911.csv").iloc[::space, :]
        rowcount = forthreshmv.shape[0]
        if (count <= rowcount):

        #if  (rowcount % 60)  :
            count = rowcount
            count = count + 1
            ltp1 = forthreshmv[f'{instru}']
            ltp1volume = forthreshmv[f'{instru}volume']
            ltp1bid = forthreshmv[f'{instru}bid']
            ltp1ask = forthreshmv[f'{instru}ask']
            stock1bidvolume = forthreshmv[f'{instru}bidvolume']
            stock1askvolume = forthreshmv[f'{instru}askvolume']
            ltp1FUT = forthreshmv[f'{instru}FUT']
            ltp1FUTvolume = forthreshmv[f'{instru}FUTvolume']
            ltp1FUTbid = forthreshmv[f'{instru}FUTbid']
            ltp1FUTask = forthreshmv[f'{instru}FUTask']
            futstock1bidvolume = forthreshmv[f'{instru}FUTbidvolume']
            futstock1askvolume = forthreshmv[f'{instru}FUTaskvolume']
            ltp1askvwap = (np.cumsum(forthreshmv[f'{instru}ask'] * forthreshmv[f'{instru}askvolume']) / (np.cumsum(forthreshmv[f'{instru}askvolume'])))
            ltp1bidvwap = (np.cumsum(forthreshmv[f'{instru}bid'] * forthreshmv[f'{instru}bidvolume']) / (np.cumsum(forthreshmv[f'{instru}bidvolume'])))
            futstock1bidvwap = (np.cumsum(forthreshmv[f'{instru}FUTbid'] * forthreshmv[f'{instru}FUTbidvolume']) / (np.cumsum(forthreshmv[f'{instru}FUTbidvolume'])))
            futstock1askvwap = (np.cumsum(forthreshmv[f'{instru}FUTask'] * forthreshmv[f'{instru}FUTaskvolume']) / (np.cumsum(forthreshmv[f'{instru}FUTaskvolume'])))
            ltp1FUTvwap = (np.cumsum(forthreshmv[f'{instru}FUT']*forthreshmv[f'{instru}FUTvolume']) / (np.cumsum(forthreshmv[f'{instru}FUTvolume'])))
            ltp1vwap = (np.cumsum(forthreshmv[f'{instru}']*forthreshmv[f'{instru}volume']) / (np.cumsum(forthreshmv[f'{instru}volume'])))

            diffbuy =  (ltp1FUTvwap[-1] - ltp1FUT.iloc[-1])
            trackbuy.append(diffbuy)
            diffsell = (ltp1FUT.iloc[-1] - ltp1FUTvwap[-1] )
            tracksell.append(diffsell)
            diff11 = pd.read_csv("myfile.csv")['diff'].iloc[-1]
            trail = pd.read_csv("myfile.csv")['trail'].iloc[-1]
            if ( diff11 < diffbuy < (max(trackbuy)  - trail)) and (checklist1[0] == 'START'):
                print(f"buy :- {ltp1.iloc[-1]+ 0.05}")

                def place1():
                    alice.place_order(transaction_type=TransactionType.Buy,
                                      instrument=stock11 ,
                                      quantity=quantity,
                                      order_type=OrderType.Limit,
                                      product_type=ProductType.Intraday,
                                      price=ltp1.iloc[-1]+ 0.05
                                      )

                starttime = time.time()
                place1()
                tradesell = ltp1bid
                quantity = 10
                checklist1[0] = ''
                checklist1[1] = 'START'
                trackbuy.clear()

            elif (diff11 < diffsell < (max(tracksell) - trail)) and (checklist1[1] == 'START'):
                print(f"sell :- {ltp1.iloc[-1]- 0.05}")


                def place2():
                    alice.place_order(transaction_type=TransactionType.Sell,
                                      instrument=stock11 ,
                                      quantity=quantity,
                                      order_type=OrderType.Limit,
                                      product_type=ProductType.Intraday,
                                      price=ltp1.iloc[-1] - 0.05
                                      )

                starttime = time.time()
                place2()
                tradebuy = ltp1ask
                quantity = 10
                checklist1[1] = ''
                checklist1[0] = 'START'
                tracksell.clear()


if (__name__ == '__main__'):
    while True:
        try:
            main()
        except Exception as e:
            print(e)



