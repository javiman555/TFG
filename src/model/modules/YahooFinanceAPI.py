import yfinance as yf
import pandas as pd
import os
import datetime as dt
from config.definitions import ROOT_DIR

'''
data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = "SPY AAPL MSFT",

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "ytd",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1m",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # adjust all OHLC automatically
        # (optional, default is False)
        auto_adjust = True,

        # download pre/post regular market hours data
        # (optional, default is False)
        prepost = True,

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )
'''
class YahooFinanceAPI():
    
    def __init__(self,debug=False):
        if debug:
            self.stocks =['SAB.MC', 'SAN.MC', 'AENA.MC', 'ELE.MC', 'NTGY.MC', 'PHM.MC', 'ENG.MC', 'GRF.MC', 'CABK.MC', 'ITX.MC', 'BKT.MC', 'VIS.MC', 'REE.MC', 'CLNX.MC']
        else:
            self.stocks =['SAB.MC', 'SAN.MC', 'AENA.MC', 'ELE.MC', 'NTGY.MC', 'PHM.MC', 'ENG.MC', 'GRF.MC', 'CABK.MC', 'ITX.MC', 'BKT.MC', 'VIS.MC', 'REE.MC', 'CLNX.MC', 'BBVA.MC', 'MRL.MC', 'FER.MC', 'MTS.MC', 'MAP.MC', 'COL.MC', 'ACX.MC', 'ACS.MC', 'IBE.MC', 'FDR.MC', 'TEF.MC', 'ANA.MC', 'IAG.MC', 'AMS.MC', 'SGRE.MC', 'MEL.MC','ALM.MC','CIE.MC','IDR.MC','ROVI.MC','SLR.MC']
            #INDEX.txt
            #self.stocks = ['ADDC', 'ADRA', 'ADRE', 'ADRS', 'ADRT', 'ADVT', 'ADVV', 'AMX', 'ASHR', 'AVDE', 'AVDV', 'AVDX', 'AVLR', 'AVRE', 'AVRN', 'BGMD', 'CAC', 'CASH', 'COMP', 'CPC', 'DAX', 'DCTH', 'DECN', 'DSCF', 'DSCR', 'DSGT', 'DSOL', 'DSPC', 'DSTL', 'DUSL', 'HIGA', 'IDX', 'INDS', 'KSI', 'LOWC', 'MADI', 'MAHI', 'MAHN', 'MYDX', 'MYHI', 'NADA', 'NAHD', 'NCTW', 'NYLE', 'PCVX', 'SBES', 'SCSC', 'SDPI', 'SGLN', 'SGMA', 'SIFI', 'SLAC', 'SMPR', 'SMTI', 'SNTE', 'SPAB', 'SPFI', 'SPIN', 'SPIR', 'SPRL', 'SPUS', 'SPXT', 'SSFI', 'SSIC', 'SSOF', 'SSTU', 'STNC', 'STRA', 'STRB', 'STRC', 'STRL', 'STRN', 'STRS', 'STRT', 'SVFD', 'TACK', 'TRIN', 'TRIQ', 'YTFD']
        
    def getStocksIndex(self,file):
        source = os.path.join(ROOT_DIR, 'resources', 'data')
        if not os.path.exists(source):
            os.makedirs(source)
          
        stocks =[]
        
        with open(os.path.join(source,file)) as inputfile:
            for line in inputfile:
                stocks.append(line.split()[0])
        return stocks
        

    def addStock(self,stockName):
        self.stocks.append(stockName)
        
    def removeStock(self,stockName):
        self.stocks.remove(stockName)
        
    def saveStocks(self,period,interval,threads,file):
        source = os.path.join(ROOT_DIR, 'resources', 'data')
        bd = list()
        realStocks = []
        
        
        for ticker in self.stocks:
            
            data = yf.download(ticker, group_by="Ticker",threads =threads, period=period,interval=interval)
            #Need next line to have a pseudo id from the ticker+date
            if not data.empty:
                data['ticker'] = ticker
                bd.append(data)
                realStocks.append(ticker)
        self.stocks = realStocks
            
        if not os.path.exists(source):
            os.makedirs(source)
        
        # combine all dataframes into a single dataframe
        df = pd.concat(bd) 
        # save to csv
        df.to_csv(os.path.join(source,file))
        
    def saveStocksStartEnd(self,start,end,interval,threads,file):
        source = os.path.join(ROOT_DIR, 'resources', 'data')

        bd = list()
        realStocks = []
        
        startdate = dt.datetime.strptime(start, "%Y-%m-%d").date()
        enddate = dt.datetime.strptime(end, "%Y-%m-%d").date()
        
        for ticker in self.stocks:
            
            data = yf.download(ticker, group_by="Ticker",threads =threads, start=startdate, end=enddate,interval=interval)
            #Need next line to have a pseudo id from the ticker+date
            if not data.empty:
                data['ticker'] = ticker
                bd.append(data)
                realStocks.append(ticker)
        self.stocks = realStocks
            
        if not os.path.exists(source):
            os.makedirs(source)
        # combine all dataframes into a single dataframe
        df = pd.concat(bd)
        # save to csv
        df.to_csv(os.path.join(source,file))