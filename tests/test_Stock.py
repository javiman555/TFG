import unittest as utest
import numpy.testing as ntest
from src.objects.wave import ComplexWaveDB

import src.modules.YahooFinanceAPI as yf
import src.objects.Stock as sk

import src.objects.k_means.K_Means as K_Means
import matplotlib.pyplot as plt
import numpy as np



class TestStock(utest.TestCase):
            
    def test_get_stocks(self):
        yf1=yf.YahooFinanceAPI(debug=False)
        stocks=[]
        
        for element in yf1.stocks:
                        
            sk1=sk.Stock(element,'DataStocks.csv',precision=2)
            stocks.append(sk1)
        self.assertEqual(len(stocks), 35)

        
    def test_get_stocks_debug(self):
        yf1=yf.YahooFinanceAPI(debug=True)
        stocks=[]
        
        for element in yf1.stocks:
                        
            sk1=sk.Stock(element,'DataStocksTest.csv',precision=2)
            stocks.append(sk1)
            
        self.assertEqual(len(stocks), 14)

if __name__ == '__main__':
    utest.main()