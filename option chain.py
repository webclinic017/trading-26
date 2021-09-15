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
import mibian
from math import sqrt
zed = [10,20,30,40]cd
def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]
print(closest(zed,15))
stock = ['NIFTY']

username = ''
password = ''
api_secret = ''
twoFA = 'a'
logging.basicConfig(level=logging.DEBUG)  # Optional for getting debug messages.
# Config
grit = []
ltplist = []
moneylist = []
z = 0
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
futstock1askvolume = 0
futstock2bidvolume = 0
futstock2askvolume = 0
futstock3bidvolume = 0
futstock3askvolume = 0
futstock4bidvolume = 0
futstock4askvolume = 0
futstock5bidvolume = 0
futstock5askvolume = 0
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
ltp1option = 0
ltp1optionvolume = 0

ratios = []
strikes = []
optionCE = 0
optionPE = 0
optionbidCE = 0
optionbidPE = 0
optionaskCE = 0
optionaskPE = 0
zrr = 0
ltp1vix = 0

tod = "return"
socket_opened = False
alice = None
month = 'AUG'

daytoexpiry = 3
interestrate = 3.27
expirydate = 3
dayiwant = 1
expdate = datetime.date(2020, 9, 24)
expdateoption = datetime.date(2020, 8, expirydate)
secondslist = []
craft = ["START"]
z = 0
print("started")

crack = []
strikice = 0
strikipe = 0

strikecall = 0
strikeput = 0
strikecall1 = 0
strikeput1 = 0
listtrail = []
trailer = 0
profit = 0
cefile = [1,2,3]
pefile = [11,22,33]
listofstrikesce = ["APACHE"]
listofstrikespe = ["APACHE"]
listofsubcee = 0
listofsubpee = 0

subscription = 0
subscription1 = 0
zrr = 0
profit = 0
subribedpack = 0
symbolmatch = 0
peisout = "OUT"
ceisout = "OUT"
listofsubce = []
listofsubpe = []
takedown = "UNDONE"
special = 0
def event_handler_quote_update(message):
    global ltp1FUT
    global ltp1FUTvolume
    global futstock1bid
    global futstock1ask
    global futstock1bidvolume
    global futstock1askvolume
    global option
    global ltp1option
    global ltp1optionvolume
    global optionbidCE
    global optionaskCE
    global optionbidvolumeCE
    global optionaskvolumeCE
    global optionbidPE
    global optionaskPE
    global optionbidvolumePE
    global optionaskvolumePE
    global callorput
    global callorputCE
    global callorputPE
    global optionCE
    global optionPE
    global ltp1vix
    global cefile
    global pefile
    global takedown
    global ltp1

    option = message['instrument'][2]
    callorput = option.split()[-1]

    if callorput == "CE":
        optionCE = message['instrument'][2]
        optionbidCE = ((message)['best_bid_price'])
        optionaskCE = ((message)['best_ask_price'])
        optionbidvolumeCE = message['best_bid_quantity']
        optionaskvolumeCE = message['best_ask_quantity']
        cefile = [optionCE, optionbidCE, optionaskCE]
    if callorput == "PE":
        optionPE = message['instrument'][2]
        optionbidPE = ((message)['best_bid_price'])
        optionaskPE = ((message)['best_ask_price'])
        optionbidvolumePE = message['best_bid_quantity']
        optionaskvolumePE = message['best_ask_quantity']
        pefile = [optionPE,optionbidPE,optionaskPE]
    if message['instrument'][2] == (f"{stock[0]} {month} FUT"):
        ltp1FUT = ((message)['ltp'])
        ltp1FUTvolume = ((message)['volume'])
        futstock1bid = ((message)['best_bid_price'])
        futstock1ask = ((message)['best_ask_price'])
        futstock1bidvolume = message['best_bid_quantity']
        futstock1askvolume = message['best_ask_quantity']

    if message['instrument'][2] == 'India VIX':

        ltp1vix = ((message)['ltp'])

    if message['token'] == 26000:

        ltp1 = ((message)['ltp'])

    if ((optionbidCE == optionbidPE) or (ceisout == "OUT" and peisout != "OUT") or (ceisout != "OUT" and peisout == "OUT")) and takedown != "DONE" and optionbidCE!= 0 and optionbidPE != 0 :
        strikice = optionCE
        strikipe = optionPE
        if ceisout == "OUTt":
            for i in listofsubce:
                alice.unsubscribe(
                    alice.get_instrument_for_fno(symbol=stock[0], expiry_date=expdateoption, is_fut=False,
                                                 strike=i, is_CE=True), LiveFeedType.MARKET_DATA)
            alice.subscribe(
                alice.get_instrument_by_symbol('NFO', strikice), LiveFeedType.MARKET_DATA)

            strikecall = optionbidCE
            strikecall1 = optionaskCE
        if peisout == "OUTt":
            for i in listofsubpe:
                alice.unsubscribe(
                    alice.get_instrument_for_fno(symbol=stock[0], expiry_date=expdateoption, is_fut=False,
                                                 strike=i, is_CE=False), LiveFeedType.MARKET_DATA)
            alice.subscribe(
                alice.get_instrument_by_symbol('NFO', strikipe), LiveFeedType.MARKET_DATA)
            strikeput = optionbidPE
            strikeput1 = optionaskPE
            takedown = "DONE"
            print(alice.get_all_subscriptions())



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
                      master_contracts_to_download=['NFO','NSE'])

    socket_opened = False
    alice.start_websocket(subscribe_callback=event_handler_quote_update,
                          socket_open_callback=open_callback,
                          run_in_background=True)
    while (socket_opened == False):  # wait till socket open & then subscribe
        pass

    all_sensex_scrips = alice.search_instruments('NFO', stock[0])

    for i in all_sensex_scrips:
        strikes.append(i[2])
    strikeprices = []
    callput = []

    for k in strikes:
        x = k.split()
        if (f'{stock[0]}' in x) and (f'{month}' in x) :
            strikeprices.append([k, (x[-2]), x[-1]])

    CE = []
    PE = []
    for i in strikeprices:
        if i[-1] == "CE" and int(i[-2]) not in CE:
            CE.append(int(i[-2]))



    #alice.subscribe(alice.get_instrument_for_fno(symbol=stock[0], expiry_date=expdate, is_fut=True,strike=None, is_CE=False), LiveFeedType.MARKET_DATA)

    #alice.subscribe(alice.get_instrument_by_symbol('NSE', 'TATASTEEL'), LiveFeedType.MARKET_DATA)
    alice.subscribe(alice.get_instrument_by_symbol('NFO', f'{stock[0]} {month} FUT'), LiveFeedType.MARKET_DATA)
    alice.subscribe(alice.get_instrument_by_symbol('NSE', 'India VIX'), LiveFeedType.MARKET_DATA)
    NIFTYY = alice.search_instruments('NSE', stock[0])
    alice.subscribe(alice.get_instrument_by_token('NSE', 26000), LiveFeedType.MARKET_DATA)

    trade = "no trade"
    print("onmyway")
    diifinstrike = abs(CE[-1] - CE[-2])
    shift = abs(CE[-1] - CE[-2])/2
    shift1 =abs(CE[-1] - CE[-2])/4

    quantity = 75
    soldstrike1 = 0

    def myround(x, base=shift):
        return base * round(x / base)



    subscription = 0
    subscription1 = 0
    zrr = 0
    profit = 0
    subribedpack = 0
    symbolmatch= 0
    todaydate =18
    peisout = "OUT"
    ceisout = "OUT"
    daytoexpiry = 20 - todaydate
    interestrate = 3.27
    dayremainingforfuture = 27 - todaydate
    special = 0
    while True:
        if ltp1FUT != 0 and ltp1vix != 0  and ltp1 != 0 and futstock1bidvolume!= 0 and futstock1askvolume !=0  :
            fairfutureprice = ltp1*(1 + 0.01*(interestrate)*(dayremainingforfuture/365))



            sigma = myround(ltp1FUT)
            difference = abs(ltp1FUT - sigma)
            closeststrike = closest(CE, ltp1FUT)


            range = ltp1vix / sqrt(360/dayiwant)
            aboverange = ltp1FUT * ((100 + range) / 100)
            lowrange = ltp1FUT * ((100 - range) / 100)



            aboverangece = closest(CE,aboverange)
            lowrangece = closest(CE, lowrange)
            if aboverangece == (aboverange - shift):
                aboverangece = closest(CE, aboverange + shift)


            uprange = closest(CE, aboverange) + diifinstrike
            downrange = closest(CE, lowrange) - diifinstrike
            uprange1 = closest(CE, aboverange)
            downrange1 = closest(CE, lowrange)
            uprange2 = closest(CE, aboverange) - diifinstrike
            downrange2 = closest(CE, lowrange) - diifinstrike


            differenceofce = abs(aboverange - aboverangece)
            differenceofpe = abs(lowrange - lowrangece)
            if subribedpack != "DONE":
                listofsubce = []
                listofsubpe = []


                for i in CE:
                    if ceisout == "OUT" and i >= aboverangece - diifinstrike and (i <= (aboverangece + 3*diifinstrike)):
                        alice.subscribe(
                            alice.get_instrument_for_fno(symbol=stock[0], expiry_date=expdateoption, is_fut=False,
                                                         strike=i, is_CE=True), LiveFeedType.MARKET_DATA)
                        listofsubce.append(i)
                print(listofsubce)


                for i in CE:
                    if peisout == "OUT" and i <= lowrangece + diifinstrike and (i >= (lowrangece - 3*diifinstrike)):
                        alice.subscribe(
                            alice.get_instrument_for_fno(symbol=stock[0], expiry_date=expdateoption, is_fut=False,
                                                         strike=i, is_CE=False), LiveFeedType.MARKET_DATA)
                        listofsubpe.append(i)
                print(listofsubpe)

                subribedpack = "DONE"

            if abs(optionbidCE - optionbidPE) <= max(optionbidCE,optionbidPE)*0.005  and (10 <(optionbidCE and optionbidPE and optionaskCE and optionaskPE) < 300) and symbolmatch != "DONE" and subribedpack == "DONE":
                print([ltp1FUT,aboverange,lowrange,optionCE, optionbidCE,optionaskCE, optionPE, optionbidPE,optionaskPE])
                strikice = optionCE
                strikipe = optionPE
                strikecall = optionbidCE
                strikecall1 = optionaskCE
                strikeput = optionbidPE
                strikeput1 = optionaskPE

                spotprice = ltp1
                callprice = strikecall
                putprice = strikeput
                strikeofce = strikice.split()[-2]
                strikeofpe = strikipe.split()[-2]


                def callgreeks(spotprice, strikeofce, interestrate, daytoexpiry):
                    c = mibian.BS([spotprice, strikeofce, interestrate, daytoexpiry], callPrice=callprice)
                    volatilityofcall = round(c.impliedVolatility)
                    c = mibian.BS([spotprice, strikeofce, interestrate, daytoexpiry], volatility=volatilityofcall)
                    return [c.callPrice, c.callDelta, c.callTheta, c.vega, c.gamma,spotprice, strikeofce, interestrate, daytoexpiry,callprice]

                callgre = (callgreeks(spotprice, strikeofce, interestrate, daytoexpiry))

                def putgreeks(spotpripe, strikeofpe, interestrate, daytoexpiry):
                    c = mibian.BS([spotprice, strikeofpe, interestrate, daytoexpiry], putPrice=putprice)
                    volatilityofput = round(c.impliedVolatility)
                    c = mibian.BS([spotpripe, strikeofpe, interestrate, daytoexpiry], volatility=volatilityofput)
                    return [c.putPrice, c.putDelta, c.putTheta, c.vega, c.gamma,spotpripe, strikeofpe, interestrate, daytoexpiry,putprice]

                putgre = (putgreeks(spotprice, strikeofpe, interestrate, daytoexpiry))

                if (abs(strikecall - strikeput)<= 0.005*max(strikecall,strikeput)) or (ceisout == "OUT" and peisout != "OUT" or callgre[0] < strikecall ) or (ceisout != "OUT" and peisout == "OUT" or putgre[0] < strikeput) :

                    if ceisout == "OUT":
                        for i in listofsubce:
                            alice.unsubscribe(
                                alice.get_instrument_for_fno(symbol=stock[0], expiry_date=expdateoption, is_fut=False,
                                                             strike=i, is_CE=True), LiveFeedType.MARKET_DATA)
                        alice.subscribe(
                            alice.get_instrument_by_symbol('NFO', strikice), LiveFeedType.MARKET_DATA)


                    if peisout == "OUT":
                        for i in listofsubpe:
                            alice.unsubscribe(
                                alice.get_instrument_for_fno(symbol=stock[0], expiry_date=expdateoption, is_fut=False,
                                                             strike=i, is_CE=False), LiveFeedType.MARKET_DATA)
                        alice.subscribe(
                            alice.get_instrument_by_symbol('NFO', strikipe), LiveFeedType.MARKET_DATA)


                    print(alice.get_all_subscriptions())

                    stock11 = alice.get_instrument_by_symbol('NFO', strikice)
                    stock22 = alice.get_instrument_by_symbol('NFO', strikipe)

                    order1 = {"instrument": stock11,
                              "order_type": OrderType.Limit,
                              "quantity": quantity,
                              "price": strikecall,
                              "transaction_type": TransactionType.Sell,
                              "product_type": ProductType.Intraday}
                    order2 = {"instrument": stock22,
                              "order_type": OrderType.Limit,
                              "quantity": quantity,
                              "price": strikeput,
                              "transaction_type": TransactionType.Sell,
                              "product_type": ProductType.Intraday}
                    order = []
                    if ceisout== "OUT":
                        order.append(order1)
                    if peisout == "OUT":
                        order.append(order2)
                    print(alice.place_basket_order(order))
                    order.clear()


                    listofsubce.clear()
                    listofsubpe.clear()

                    print([ltp1FUT, aboverange, lowrange, optionCE, optionbidCE, optionPE, optionbidPE])

                    print(alice.get_all_subscriptions())
                    symbolmatch = "DONE"
                    trade = "BOUGHT"



            elif trade == "BOUGHT" and (((max(optionaskCE,optionaskPE)/min(optionaskCE,optionaskPE)) > 3) or (2 < profit < trailer)):
                if (3 < profit < trailer):
                    special = "EXITING"
                print(optionCE,optionPE)

                print([strikice,strikipe,optionaskCE,optionaskPE])
                print([strikecall1,strikeput1,strikecall,strikeput])
                print("buying")

                if strikecall!= optionbidCE and strikeput!= optionbidPE \
                    and strikecall1!= optionaskCE and strikeput1 != optionaskPE:
                    print("bought")
                    print([ltp1FUT,optionCE,optionaskCE, optionPE,optionaskPE])
                    print(strikecall - optionaskCE + strikeput- optionaskPE )



                    trade = "no trade"
                    stock11 =  alice.get_instrument_by_symbol('NFO',optionCE)

                    stock22 =  alice.get_instrument_by_symbol('NFO',optionPE)

                    order1 = {"instrument": stock11,
                              "order_type": OrderType.Limit,
                              "quantity": quantity,
                              "price": optionaskCE,
                              "transaction_type": TransactionType.Buy,
                              "product_type": ProductType.Intraday}
                    order2 = {"instrument": stock22,
                              "order_type": OrderType.Limit,
                              "quantity": quantity,
                              "price": optionaskPE,
                              "transaction_type": TransactionType.Buy,
                              "product_type": ProductType.Intraday}

                    if special != "EXITING":
                        order = []
                        if min(optionaskCE,optionaskPE) == optionaskPE :
                            order.append(order2)
                        if min(optionaskCE,optionaskPE) == optionaskCE:
                            order.append(order1)

                        print(alice.place_basket_order(order))
                        order.clear()
                        if min(optionaskCE,optionaskPE) == optionaskPE:
                            alice.unsubscribe(
                                alice.get_instrument_by_symbol('NFO', optionPE), LiveFeedType.MARKET_DATA)
                            peisout = "OUT"
                            ceisout = "NOTOUT"
                        if min(optionaskCE,optionaskPE) == optionaskCE:
                            alice.unsubscribe(
                                alice.get_instrument_by_symbol('NFO', optionCE), LiveFeedType.MARKET_DATA)
                            ceisout = "OUT"
                            peisout = "NOTOUT"


                        print(alice.get_all_subscriptions())

                    if special == "EXITING":
                        order = [order1,order2]
                        print(alice.place_basket_order(order))
                        alice.unsubscribe(
                            alice.get_instrument_by_symbol('NFO', optionPE), LiveFeedType.MARKET_DATA)
                        alice.unsubscribe(
                            alice.get_instrument_by_symbol('NFO', optionCE), LiveFeedType.MARKET_DATA)
                        order.clear()


                    subscription = "UNDONE"
                    trade == "UNDONE"
                    subribedpack = "UNDONE"

                    subscription1 = "UNDONE"
                    symbolmatch = "UNDONE"
                    special = 0


            elif trade == "BOUGHT" and symbolmatch == "DONE":
                profit =(strikecall - optionaskCE + strikeput - optionaskPE)
                listtrail.append(profit)
                trailer  = max(listtrail) - 1





if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(e)

