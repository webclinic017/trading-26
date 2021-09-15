# trading
1.DIVIDEND YIELD PROJECT- 
https://bsey.herokuapp.com/
https://github.com/akashrajcashrayz/bsey
Use - flask web app To pick up the stocks that are having highest dividend yield in the upcoming dates for swing trading.
Theory- downloaded latest company announcement from bse official website. and extracting ex dividend date and dividend
       getting end of  the day price from bhavcopy .
       apply dividend yield formula sorting them in decending dividend yield order.

2.fetchstocknsebsedataincsv-
https://github.com/akashrajcashrayz/trading/blob/main/fetchstocknsebsedataincsv.py
use- fetching banks data like (ltp,bid,ask,futureprice,volume)in both bse and nse and write them in csv to use csv file as a 
database for backtest and to apply calculations of indicator like vwap.which require historical prices.using aliceblue python api

3.find_cointegratedpair.py-
https://github.com/akashrajcashrayz/trading/blob/main/find_cointegratedpair.py
use- to find out cointegrated bank pairs to arbitrage next day.using statsmodel api using csv file created in 'fetchstocknsebsedataincsv' as a database.

4.bidaskalice.py
https://github.com/akashrajcashrayz/trading/blob/main/bidaskalice.py
use- arbitrage on cointegrated pairs using z score strategy.
strategy- when zscore becomes greater then threshold which we buy and sell those pairs in which we get most profit in previous day backtest and threshold we get in backtest.

5.nsearbitrage.py
https://github.com/akashrajcashrayz/trading/blob/main/nsearbitrage.py
use- interexchange arbitrage of stock

strategy - only sell and buy : if (bidprice of exchange1 - askprice of exchange2 ) > (0.10 + profitwewant + brokerage) and (bid and ask price of exchange1) >(bid and ask price of exchange2) : 
  then we sell exchange1 stock at bidprice -0.05 and buy exchange2 stock at bidprice +0.05

6.optionchain.py
https://github.com/akashrajcashrayz/trading/blob/main/option%20chain.py
use - its normal strangle strategy.
strategy = finding out the volatilty range of nifty by using indiavix.nifty is used for strangle due to less volatility.
on getting range we fetch list of out of the money strikeprices and their bid ask prices. and searching strikes with closest bid prices in call and put and also having high liquidy ie less bid ask difference.
on getting required call and put strikes we write them both .and on matching with other bid prices we book profit from unmatched and make position in matched.
till it become straddle. and on becoming straddle we cover them with buying out of the money strikes of next expiry due to less time decay.

7.vwapcodefuture.py
https://github.com/akashrajcashrayz/trading/blob/main/vwapcodefuture.py
strategy - it is vwap reversal strategy after certain difference in vwap and ltp some stocks bounce back to their vwap.on backtesting i found axisbank show this behaviour.
also used trailing to maximize profit.threshold difference are calculted from backtesting of prevous day data.

8.backtestingatr
https://github.com/akashrajcashrayz/trading/blob/main/supertrend_using_atr.ipynb
strategy - we buy when stocks give closing above the upper atr range and sell if stock goes below lower atr range.in this code we backtested the strategy to find optimized parameters for this atr startegy
like. target percenage ,timeperiod of candle stick,and also how much profitable trades and loss trades
	STOCK	CANDLE	PERIOD	mult	BUYTARGETACHIEVED	SELLTARGETACHIEVED	PROFITABLETRADES	LOSSTRADES	TOTALTRADES	PNL
0	NIFTY-I.NFO	10	4	2	7	5	12	12	24	2567.15                  12              24             2567    
1	BANKNIFTY-I.NFO	15	3	2	6	4	10	7	17	12946.60                 7               17              12946.60


9.alpha_datandreport
https://github.com/akashrajcashrayz/trading/blob/main/alpha_datandreport.ipynb
strategy - this code is to create septrate csv files of different time frames of stocks to ease the backtesting.

10.alpha_finalexecution
https://github.com/akashrajcashrayz/trading/blob/main/alpha_finalexecution.ipynb
strategy - on ignoring first 5minute data.and taking the next 30min high low range.if stock give closing above high of 30min range. its buy and if below low of 30min range its sell
this code is to find optimized candle period and target percent .and maximum profit 
example-
	STOCK	PERIOD	CANDLE	BUYTARGETPERCENT	SELLTARGETPERCENTT	BUYTARGETACHIEVED	SELLTARGETACHIEVED	PROFITABLETRADES	LOSSTRADES	TOTALTRADES	PNL	TIMEFRAME
0	MOTHERSUMI-I.NFO	fromDEC2019	5	3	-3	20	16	44	65	109	2.0115	30

MACHINE LEARNING PROJECTS-
1.face_expression_recognisation
https://github.com/akashrajcashrayz/face_expression_recognisation
use - to detect emotion using webcam

2. sign language recognisation
https://github.com/akashrajcashrayz/signn
use - to detect hand sign for those who cant speek


