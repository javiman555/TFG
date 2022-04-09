import unittest as utest
import numpy.testing as ntest
from src.objects.wave import ComplexWaveDB
import numpy as np

import src.modules.YahooFinanceAPI as yf
import src.objects.Stock as sk

import src.objects.k_means.K_Means as K_Means



class TestVolatility(utest.TestCase):

    
    @classmethod
    def setUpClass(cls):
        yf1=yf.YahooFinanceAPI(debug=True)
        cls.stocks =[]
        
        for element in yf1.stocks:
            
            sk1=sk.Stock(element,'DataStocksTest.csv',precision=2)
            cls.stocks.append(sk1)        
        
        
    def test_get_Volatility_Parkinson(self):
        
        volatilityParkinson = []
        volatilityParkinsonValue = 0
        
        for element in self.__class__.stocks:
                        
            vP=element.volatilityParkinson
            volatilityParkinson.append(vP)
            volatilityParkinsonValue += vP
        self.assertEqual(volatilityParkinson[0], 0.1589865337583388)
        self.assertEqual(volatilityParkinson[13], 0.06718448988324788)
        self.assertEqual(volatilityParkinsonValue,0.9825394061876466)

        
    def test_get_Volatility_Standar_Deviation(self):

        volatilityStandarDeviationOpen = []
        volatilityStandarDeviationClose = []
        volatilityStandarDeviationHigh = []
        volatilityStandarDeviationLow = []
        
        for element in self.__class__.stocks:
                        
            vSDo=element.volatilityStandarDeviationOpen
            vSDc=element.volatilityStandarDeviationClose
            vSDh=element.volatilityStandarDeviationHigh
            vSDl=element.volatilityStandarDeviationLow
            volatilityStandarDeviationOpen.append(vSDo)
            volatilityStandarDeviationClose.append(vSDc)
            volatilityStandarDeviationHigh.append(vSDh)
            volatilityStandarDeviationLow.append(vSDl)

        self.assertEqual(volatilityStandarDeviationOpen[0], 0.0981361788951099)
        self.assertEqual(volatilityStandarDeviationOpen[13], 6.1205761545408475)
        self.assertEqual(volatilityStandarDeviationClose[0], 0.09899302136081992)
        self.assertEqual(volatilityStandarDeviationClose[13], 6.124599647172082)
        self.assertEqual(volatilityStandarDeviationHigh[0], 0.10153075530924194)
        self.assertEqual(volatilityStandarDeviationHigh[13], 6.0677465466157)
        self.assertEqual(volatilityStandarDeviationLow[0], 0.09620846140104289)
        self.assertEqual(volatilityStandarDeviationLow[13], 6.133247144884093)

    def test_get_Volatility_Standar_Deviation_Diference(self):

        volatilityStandarDeviationOpen = 0
        volatilityStandarDeviationClose = 0
        volatilityStandarDeviationHigh = 0
        volatilityStandarDeviationLow = 0
        volatilityStandarDeviationHighLow1=0
        volatilityStandarDeviationHighLow2=0
        volatilityStandarDeviationOpenClose = 0
        volatilityStandarDeviationOpenHigh = 0
        volatilityStandarDeviationOpenLow = 0
        
        for element in self.__class__.stocks:
                        
            vSDo=element.volatilityStandarDeviationOpen
            vSDc=element.volatilityStandarDeviationClose
            vSDh=element.volatilityStandarDeviationHigh
            vSDl=element.volatilityStandarDeviationLow
            
            volatilityStandarDeviationHighLow1+=element.volatilityStandarDeviationHighLow1
            volatilityStandarDeviationHighLow2+=element.volatilityStandarDeviationHighLow2
            
            volatilityStandarDeviationOpen += vSDo
            volatilityStandarDeviationClose += vSDc
            volatilityStandarDeviationHigh += vSDh
            volatilityStandarDeviationLow += vSDl
            volatilityStandarDeviationOpenClose+=np.abs(vSDo-vSDc)
            volatilityStandarDeviationOpenHigh+=np.abs(vSDo-vSDh)
            volatilityStandarDeviationOpenLow+=np.abs(vSDo-vSDl)
        
        self.assertEqual(volatilityStandarDeviationOpenClose, 0.3674107205418932)
        self.assertEqual(volatilityStandarDeviationOpenHigh, 0.5286898786741252)
        self.assertEqual(volatilityStandarDeviationOpenLow, 0.62142566418269)
        
        self.assertEqual(volatilityStandarDeviationOpen,40.59744268525804)
        self.assertEqual(volatilityStandarDeviationClose,40.388054721203760)
        self.assertEqual(volatilityStandarDeviationHigh,40.51456209396203)
        self.assertEqual(volatilityStandarDeviationLow,40.17145425039071)
        self.assertEqual(volatilityStandarDeviationHighLow1,35.702821945360675)
        self.assertEqual(volatilityStandarDeviationHighLow2,45.236017415666964)
        
        
if __name__ == '__main__':
    utest.main()