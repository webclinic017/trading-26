import numpy as np
import pandas as pd
import time
import multiprocessing
from multiprocessing import Pool
from alicebl import event_handler_quote_update
cave = ["break","return","pass"]
tod = "fdfdfde"
#print(tod)
df = pd.read_csv("12052020.csv")

'''pair = ['KOTAKBANK', 'ICICIBANK']
S1 = df[pair[0]]
S2 = df[pair[1]]
pair1 = [S1, S2]
pair2 = [S2, S1]'''
crazy, stock11, stock22, window11, window22, thresh11, minthresh11 = [], [], [], [], [], [], []


#pair1 = [df["AXISBANK"], df["HDFCBANK"], df["AXISBANK"], df["ICICIBANK"], df["AXISBANK"], df["KOTAKBANK"], df["HDFCBANK"], df["ICICIBANK"], df["HDFCBANK"], df["KOTAKBANK"], df["ICICIBANK"], df["KOTAKBANK"]]
#pair2 = [df["HDFCBANK"], df["AXISBANK"], df["ICICIBANK"], df["AXISBANK"], df["KOTAKBANK"], df["AXISBANK"], df["ICICIBANK"], df["HDFCBANK"], df["KOTAKBANK"], df["HDFCBANK"], df["KOTAKBANK"], df["ICICIBANK"]]

#11.050000000000011 215 AXISBANK ICICIBANK 1 4 1.0 1.0 day 3

print("chaaaaaaaaaaaaaaaaaaaaaaaaaaoo")



def zscore(series):
    return (series - series.mean()) / np.std(series)


def trade(stock1, stock2, window1, window2, thresh, minthresh):
    # If window length is 0, algorithm doesn't make sense, so exit
    if (window1 == 0) or (window2 == 0):
        return 0

    # Compute rolling mean and rolling standard deviation
    ratios = stock1 / stock2
    ma1 = ratios.rolling(window=window1,
                         center=False).mean()
    ma2 = ratios.rolling(window=window2,
                         center=False).mean()
    std = ratios.rolling(window=window2,
                         center=False).std()
    zscore = (ma1 - ma2) / std

    # Simulate trading
    # Start with no money and no positions
    money = 0

    check = ["begin", "begin", "begin"]
    p = 1

    consta = []
    for i in range(len(ratios)):
        if zscore[i] > thresh and check[0] == "begin" and check[1] == "begin":
            if (ratios[i]) > 1:
                consta.append(p)
                consta.append(p * (round(ratios[i])))
            elif (ratios[i]) < 1:
                consta.append(p*(round(1/ratios[i])))
                consta.append(p)
            sell = stock1[i] * consta[0]
            buy = stock2[i] * consta[1]
            #print(f"sell {stock1.name} {consta[0]} quanity at {sell} buy {stock2.name} {consta[1]} quanity at {buy} at zscore {zscore[i]} ")

            check[0] = ""
            check[1] = "step1"
        elif zscore[i] < -thresh and check[0] == "begin" and check[1] == "begin":
            if (ratios[i]) > 1:
                consta.append(p)
                consta.append(p * (round(ratios[i])))
            elif (ratios[i]) < 1:
                consta.append(p*(round(1/ratios[i])))
                consta.append(p)
            buy = stock1[i]*consta[0]
            sell = stock2[i]*consta[1]
            #print(f"buy {stock1.name} {consta[0]} quanity at {buy} sell {stock2.name} {consta[1]} quanity at {sell} at zscore {zscore[i]} ")
            check[0] = ""
            check[1] = "step2"
        # Clear positions if the z-score between -.5 and .5
        elif abs(zscore[i]) < minthresh and check[0] == "" and check[1] != "begin":
                if check[1] == "step1":
                    mtm1 = (sell - stock1[i] * consta[0])
                    mtm2 = (stock2[i] * consta[1] - buy)
                    z = mtm1+mtm2
                    if z < 0 and tod == "break":
                        print("breaking")
                        break
                    elif z < 0 and tod == "return":
                        print("returning")
                        return
                    #print(f"buy {stock1.name} {consta[0]} quantity  at {stock1[i]*consta[0]} sell {stock2.name} {consta[1]} quantity  at {stock2[i]* consta[1]} mtm at {stock1.name} {mtm1} mtm at {stock2.name} {mtm2} total mtm {mtm1 + mtm2} zscore {zscore[i]}")

                    check[0] = "begin"
                    check[1] = "begin"
                    money = money + z
                    #print(money)
                elif check[1] == "step2":
                    mtm1 = (stock1[i] * consta[0] - buy)
                    mtm2 = (sell - stock2[i] * consta[1])
                    z = mtm1 + mtm2
                    if z < 0 and tod == "break":
                        print("breaking")
                        break
                    elif z < 0 and tod == "return":
                        print("returning")
                        return
                    #print(f"sell {stock1.name} {consta[0]} quantity  at {stock1[i]*consta[0]} buy {stock2.name} {consta[1]} quantity  at {stock2[i]* consta[1]} mtm at {stock1.name} {mtm1} mtm at {stock2.name} {mtm2} total mtm {mtm1 + mtm2} zscore {zscore[i]}")

                    check[0] = "begin"
                    check[1] = "begin"
                    money = money+z
                    #print(money)
                consta.clear()
                buy = 0
                sell = 0


    crazy.append(money)
    maximumoney = max(crazy)
    indexofmax = crazy.index(maximumoney)
    stock11.append(stock1.name)
    stock22.append(stock2.name)
    window11.append(window1)
    window22.append(window2)
    thresh11.append(thresh)
    minthresh11.append(minthresh)

    #print("{}  {}  {}  {}  {}  {}  {} ".format(money, stock1.name, stock2.name, window1, window2, thresh, minthresh))

    print(("result: {} {} {} {} {} {} {} {}").format(maximumoney, indexofmax, stock11[(indexofmax)],
                                                   stock22[(indexofmax)], window11[(indexofmax)],
                                                   window22[(indexofmax)], thresh11[(indexofmax)],
                                                   minthresh11[(indexofmax)]))
#trade(df["HDFCBANK"],df["ICICIBANK"],2,6,1.25,0.25)

if __name__ == '__main__':
    starttime = time.time()
    print("going tooooooooooooooooooooooooo")
    def task():

        pool = multiprocessing.Pool()
        pool = Pool()
        for mt in np.arange(0, 1.85, 0.05):
                pool.apply_async(trade, (df['ICICIBANK'], df['AXISBANK'], 1, 6, 1.85,mt))

        pool.close()
        pool.join()
    task()
    #trade(df['AXISBANK'],df['ICICIBANK'],1,8,2.08,1.20)
    print('That took {} seconds'.format(time.time() - starttime))
