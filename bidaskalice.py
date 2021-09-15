import logging
import datetime
import statistics
from time import sleep
from alice_blue import *
import multiprocessing
from multiprocessing import Pool
import pprint
import threading
import numpy as np
# Config
import numpy as np
import pandas as pd
from pprint import pprint
from scrat import trade


username = ''
password = ''
api_secret = ''
twoFA = 'a'
logging.basicConfig(level=logging.DEBUG)  # Optional for getting debug messages.
# Config

ltp1 = 0
ltp2 = 0
ratios = []
bid1ask2ratios = []
ask1bid2ratios = []
df = pd.DataFrame(columns=['ltp11', 'ltp22'])
money = 0
buy = 0
sell = 0
p = 1
consta = []
checklist1 = ['START', 'START', 'START']
stock = ["AXISBANK","HDFCBANK"]

tod = "break"
thresh = 1
profit = 0.5
socket_opened = False
alice = None
buy = 0
sell = 0
def zscore(series):
    return (series - series.mean()) / np.std(series)
def event_handler_quote_update(message):
    global ltp1
    global ltp2
    global stock1bidprice
    global stock1askprice
    global stock2bidprice
    global stock2askprice
    if message['instrument'][2] == stock[0] :
        ltp1=((message)['ltp'])
        stock1bidprice = ((message)['best_bid_price']) -0.05
        stock1askprice = ((message)['best_ask_price']) +0.05


    elif message['instrument'][2] == stock[1]:
        ltp2=((message)['ltp'])
        stock2bidprice = ((message)['best_bid_price']) -0.05
        stock2askprice = ((message)['best_ask_price']) + 0.05




def open_callback():
    global socket_opened
    socket_opened = True


def buy_signal(ins_scrip,quantity,price):
    global alice
    alice.place_order(transaction_type=TransactionType.Buy,
                      instrument=ins_scrip,
                      quantity=quantity,
                      order_type=OrderType.Limit,
                      product_type=ProductType.Intraday,
                      price=price,
                      trigger_price=None,
                      stop_loss=None,
                      square_off=None,
                      trailing_sl=None,
                      is_amo=False)


def sell_signal(ins_scrip,quantity,price):
    global alice
    alice.place_order(transaction_type=TransactionType.Sell,
                      instrument=ins_scrip,
                      quantity=quantity,
                      order_type=OrderType.Limit,
                      product_type=ProductType.Intraday,
                      price=price,
                      trigger_price=None,
                      stop_loss=None,
                      square_off=None,
                      trailing_sl=None,
                      is_amo=False)


def main():
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
                      master_contracts_to_download=['NSE'])

    print(alice.get_balance())  # get balance / margin limits
    print(alice.get_profile())  # get profile
    print(alice.get_daywise_positions())  # get daywise positions
    print(alice.get_netwise_positions())  # get netwise positions
    print(alice.get_holding_positions())  # get holding positions
    print(alice.get_trade_book())
    print(alice.get_order_history())

    socket_opened = False
    alice.start_websocket(subscribe_callback=event_handler_quote_update,
                          socket_open_callback=open_callback,
                          run_in_background=True)
    while (socket_opened == False):  # wait till socket open & then subscribe
        pass
    stock11 = alice.get_instrument_by_symbol('NSE', stock[0])
    stock22 =  alice.get_instrument_by_symbol('NSE', stock[1])

    alice.subscribe([stock11, stock22],
                    LiveFeedType.MARKET_DATA)
    pprint(alice.get_all_subscriptions())

    money = 0
    buy = 0
    sell = 0

    while True:
        if (ltp1 and ltp2 and stock1askprice and stock1bidprice and stock2askprice and stock2bidprice)!= 0:
            ratio = ltp1/ltp2
            bid1ask2ratio = stock1bidprice/stock2askprice
            ask1bid2ratio = stock1askprice/stock2bidprice
            #print(f"{ltp1} {ltp2}")
            bid1ask2ratios.append(bid1ask2ratio)
            ask1bid2ratios.append(ask1bid2ratio)
            ratios.append(ratio)
            mv = 5
            if (len(ratios) >= mv):
                sma_1 = statistics.mean(ratios[-1:])
                sma_20 = statistics.mean(ratios[-mv:])
                std_20 = statistics.stdev(ratios[-mv:])
                sma_1bid1ask2 = statistics.mean(bid1ask2ratios[-1:])
                sma_20bid1ask2 = statistics.mean(bid1ask2ratios[-mv:])
                std_20bid1ask2 = statistics.stdev(bid1ask2ratios[-mv:])
                sma_1ask1bid2 = statistics.mean(ask1bid2ratios[-1:])
                sma_20ask1bid2 = statistics.mean(ask1bid2ratios[-mv:])
                std_20ask1bid2 = statistics.stdev(ask1bid2ratios[-mv:])
                if (sma_1 and sma_20 and std_20 and sma_1bid1ask2 and sma_20bid1ask2 and std_20bid1ask2 and sma_1ask1bid2 and sma_20ask1bid2 and std_20ask1bid2 ) != 0:
                    zscore = (sma_1-sma_20)/std_20
                    zscorebid1ask2 = (sma_1bid1ask2-sma_20bid1ask2)/std_20bid1ask2
                    zscoreask1bid2 = (sma_1ask1bid2 - sma_20ask1bid2) / std_20ask1bid2
                    #print(f" zscore :{zscore} zscorebid1ask2:{zscorebid1ask2} zscoreask1bid2:{zscoreask1bid2}")
                    if zscorebid1ask2 > thresh and (checklist1[0] == 'START') and (checklist1[1] == 'START'):
                        if (bid1ask2ratio) > 1:
                            consta.append(p)
                            consta.append(p * (round(bid1ask2ratio)))
                        elif (bid1ask2ratio) < 1:
                            consta.append(p * (round(1 / bid1ask2ratio)))
                            consta.append(p)
                        sell = stock1bidprice * consta[0]
                        buy = stock2askprice * consta[1]
                        print(
                            f"sell {stock[0]} {consta[0]} quanity at {sell} buy {stock[1]} {consta[1]} quanity at {buy} at zscorebid1ask2 {zscorebid1ask2} ")
                        sell_signal(stock11,consta[0],stock1bidprice)
                        buy_signal(stock22,consta[1],stock2askprice)

                        checklist1[0] = 'DONE'
                        checklist1[1] = ''
                        checklist1[2] = 'first'
                    elif zscoreask1bid2 < -thresh or (checklist1[0] == 'DONE') and (checklist1[1] == '') and (
                            checklist1[2] == 'first'):
                        mtm1 = (sell - stock1askprice * consta[0])
                        mtm2 = (stock2bidprice * consta[1] - buy)
                        z = mtm1 + mtm2
                        print(z)
                        if z > profit and tod == "break":
                            print(
                                f"buy {stock[0]} {consta[0]} quantity  at {stock1askprice * consta[0]} "
                                f"sell {stock[1]} {consta[1]} quantity  at {stock2bidprice * consta[1]} "
                                f"mtm at {stock[0]} {mtm1} mtm at {stock[1]} {mtm2} total mtm {mtm1 + mtm2} "
                                f"zscoreask1bid2 {zscoreask1bid2}")
                            buy_signal(stock11, 2*consta[0], stock1askprice)
                            sell_signal(stock22, 2*consta[1], stock2bidprice)
                            money = money + z
                            print(money)
                            consta.clear()

                            if (ask1bid2ratio) > 1:
                                consta.append(p)
                                consta.append(p * (round(ask1bid2ratio)))
                            elif (ask1bid2ratio) < 1:
                                consta.append(p * (round(1 / ask1bid2ratio)))
                                consta.append(p)
                            buy = stock1askprice * consta[0]
                            sell = stock2bidprice * consta[1]
                            print(
                                f"buy {stock[0]} {consta[0]} quanity at {buy} sell {stock[1]} {consta[1]} quanity at {sell} at zscoreask1bid2 {zscoreask1bid2} ")


                            checklist1[0] = ''
                            checklist1[1] = 'DONE'
                            checklist1[2] = 'first'
                    elif zscorebid1ask2 > thresh or (checklist1[0] == '') and (checklist1[1] == 'DONE') and (
                            checklist1[2] == 'first'):
                        mtm1 = (stock1bidprice * consta[0] - buy)
                        mtm2 = (sell - stock2askprice * consta[1])
                        z = mtm1 + mtm2
                        print(z)

                        if z > profit and tod == "break":

                            print(
                                f"sell {stock[0]} {consta[0]} quantity  at {stock1bidprice * consta[0]} "
                                f"buy {stock[1]} {consta[1]} quantity  at {stock2askprice * consta[1]} "
                                f"mtm at {stock[0]} {mtm1} mtm at {stock[1]} {mtm2} total mtm {mtm1 + mtm2}"
                                f" zscorebid1ask2 {zscorebid1ask2}")
                            sell_signal(stock11, 2*consta[0], stock1bidprice)
                            buy_signal(stock22, 2*consta[1], stock2askprice)
                            money = money + z
                            print(money)
                            consta.clear()

                            if (bid1ask2ratio) > 1:
                                consta.append(p)
                                consta.append(p * (round(bid1ask2ratio)))
                            elif (bid1ask2ratio) < 1:
                                consta.append(p * (round(1 / bid1ask2ratio)))
                                consta.append(p)
                            # print('Selling Ratio %s %s %s %s'%(money, ratio, countS1,countS2))
                            # Buy long if the z-score is < -1
                            sell = stock1bidprice * consta[0]
                            buy = stock2askprice * consta[1]
                            print(
                                f"sell {stock[0]} {consta[0]} quanity at {sell} buy {stock[1]} {consta[1]} quanity at {buy} at zscorebid1ask2 {zscorebid1ask2} ")
                            checklist1[0] = 'DONE'
                            checklist1[1] = ''
                            checklist1[2] = 'first'

                    elif zscoreask1bid2 < -thresh and (checklist1[0] == 'START') and (checklist1[1] == 'START'):
                        if (ask1bid2ratio) > 1:
                            consta.append(p)
                            consta.append(p * (round(ask1bid2ratio)))
                        elif (ask1bid2ratio) < 1:
                            consta.append(p * (round(1 / ask1bid2ratio)))
                            consta.append(p)
                        buy = stock1askprice * consta[0]
                        sell = stock2bidprice * consta[1]
                        print(
                            f"buy {stock[0]} {consta[0]} quanity at {buy} sell {stock[1]} {consta[1]} quanity at {sell} at zscoreask1bid2 {zscoreask1bid2} ")
                        buy_signal(stock11, consta[0], stock1askprice)
                        sell_signal(stock22, consta[1], stock2bidprice)

                        checklist1[0] = 'DONE'
                        checklist1[1] == ''
                        checklist1[2] = 'second'
                    elif zscorebid1ask2 > thresh or (checklist1[0] == 'DONE') and (checklist1[1] == '') and (
                            checklist1[2] == 'second'):
                        mtm1 = (stock1bidprice * consta[0] - buy)
                        mtm2 = (sell - stock2askprice * consta[1])
                        z = mtm1 + mtm2
                        print(z)

                        if z > profit and tod == "break":

                            print(
                                f"sell {stock[0]} {consta[0]} quantity  at {stock1bidprice * consta[0]}"
                                f" buy {stock[1]} {consta[1]} quantity  at {stock2askprice * consta[1]}"
                                f" mtm at {stock[0]} {mtm1} mtm at {stock[1]} {mtm2} total mtm {mtm1 + mtm2}"
                                f" zscorebid1ask2 {zscorebid1ask2}")
                            sell_signal(stock11, 2 * consta[0], stock1bidprice)
                            buy_signal(stock22, 2 * consta[1], stock2askprice)
                            money = money + z
                            print(money)
                            consta.clear()

                            if (bid1ask2ratio) > 1:
                                consta.append(p)
                                consta.append(p * (round(bid1ask2ratio)))
                            elif (bid1ask2ratio) < 1:
                                consta.append(p * (round(1 / bid1ask2ratio)))
                                consta.append(p)

                            sell = stock1bidprice * consta[0]
                            buy = stock2askprice * consta[1]
                            print(
                                f"sell {stock[0]} {consta[0]} quanity at {sell} buy {stock[1]} {consta[1]} quanity at {buy} at zscorebid1ask2 {zscorebid1ask2} ")

                            checklist1[0] = ''
                            checklist1[1] = 'DONE'
                            checklist1[2] = 'second'
                    elif zscoreask1bid2 < -thresh or (checklist1[0] == '') and (checklist1[1] == 'DONE') and (
                            checklist1[2] == 'second'):
                        mtm1 = (sell - stock1askprice * consta[0])
                        mtm2 = (stock2bidprice * consta[1] - buy)
                        z = mtm1 + mtm2
                        print(z)

                        if z > profit and tod == "break":

                            print(
                                f"buy {stock[0]} {consta[0]} quantity  at {stock1askprice * consta[0]} "
                                f"sell {stock[1]} {consta[1]} quantity  at {stock2bidprice * consta[1]}"
                                f" mtm at {stock[0]} {mtm1} mtm at {stock[1]} {mtm2} total mtm {mtm1 + mtm2}"
                                f" zscoreask1bid2 {zscoreask1bid2}")
                            buy_signal(stock11, 2 * consta[0], stock1askprice)
                            sell_signal(stock22, 2 * consta[1], stock2bidprice)
                            money = money + z
                            print(money)
                            consta.clear()

                            if (ask1bid2ratio) > 1:
                                consta.append(p)
                                consta.append(p * (round(ask1bid2ratio)))
                            elif (ask1bid2ratio) < 1:
                                consta.append(p * (round(1 / ask1bid2ratio)))
                                consta.append(p)
                            buy = stock1askprice * consta[0]
                            sell = stock2bidprice * consta[1]
                            print(
                                f"buy {stock[0]} {consta[0]} quanity at {buy} sell {stock[1]} {consta[1]} quanity at {sell} at zscoreask1bid2 {zscoreask1bid2} ")


                            checklist1[0] = 'DONE'
                            checklist1[1] = ''
                            checklist1[2] = 'second'

            sleep(0.1)
        sleep(0.0001)



#tradehai()

if (__name__ == '__main__'):
    main()