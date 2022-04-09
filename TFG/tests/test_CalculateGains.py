import unittest as utest
import numpy.testing as ntest
from src.objects.wave import ComplexWaveDB

import src.modules.YahooFinanceAPI as yf
import src.objects.Stock as sk

import src.objects.k_means.K_Means as K_Means
import src.objects.graph.VisibilityGraph as vg
import src.objects.graph.ClosenessGraph as cg
import src.procedures.DiversificateAssets as DiversificateAssets
import src.objects.k_means.K_MeansVariation as K_MeansVariation
import src.procedures.CalculateGains as CalculateGains


class TestCalculateGains(utest.TestCase):
     
    @classmethod
    def setUpClass(cls):
        yf1=yf.YahooFinanceAPI(debug=True)
        cls.waves =[]
        for element in yf1.stocks:
            
            wave = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocksTest.csv')
            wave.normalice()
            cls.waves.append(wave)
        
        cls.calculateGains = CalculateGains.CalculateGains()
        cls.closenessGraph = cg.ClosenessGraph()
        cls.kmeans = K_MeansVariation.K_MeansVariation(0)
        cls.diversificateAssets = DiversificateAssets.DiversificateAssets(cls.closenessGraph,cls.waves)

    def test_CalculateGains_SAN(self):
        
        valueList = self.__class__.calculateGains.calculateGainsFromStartToEnd( self.__class__.waves[0], 1000)
        
        self.assertEqual(min(valueList), 728.3473122858786)
        self.assertEqual(max(valueList), 1523.146091254578)
        self.assertEqual(sum(valueList) / len(valueList), 1119.0753976368887) 
        
    def test_CalculateGains_HomogeneousDistribution(self):
        
        valueList = self.__class__.calculateGains.calculateDiversificatedGains( self.__class__.waves, 1000)
        
        self.assertEqual(min(valueList), 914.3460740497637)
        self.assertEqual(max(valueList), 1089.596886510977)
        self.assertEqual(sum(valueList) / len(valueList), 963.1738850645257) 
       
    def test_CalculateGains_GN_GenericDistance_4_Clusters(self):
        
        self.__class__.closenessGraph.distanceCloseness(self.__class__.waves,self.__class__.kmeans.fitDefault,self.__class__.kmeans)
        selectedStocksWaves = self.__class__.diversificateAssets.getStocksGirvanNewman(4)
        valueList = self.__class__.calculateGains.calculateDiversificatedGains( selectedStocksWaves, 1000)
        
        self.assertEqual(min(valueList), 884.9742029448157)
        self.assertEqual(max(valueList), 1084.568352716561)
        self.assertEqual(sum(valueList) / len(valueList), 962.129839177829) 
        
    def test_CalculateGains_GN_Course_4_Clusters(self):
        
        self.__class__.closenessGraph.distanceCloseness(self.__class__.waves,self.__class__.kmeans.fitByCourse,self.__class__.kmeans)
        selectedStocksWaves = self.__class__.diversificateAssets.getStocksGirvanNewman(4)
        valueList = self.__class__.calculateGains.calculateDiversificatedGains( selectedStocksWaves, 1000)
        
        self.assertEqual(min(valueList), 938.345320220516)
        self.assertEqual(max(valueList), 1063.826806093286)
        self.assertEqual(sum(valueList) / len(valueList), 993.4674203449407) 
        
    def test_CalculateGains_GN_CourseValue_4_Clusters(self):
        
        self.__class__.closenessGraph.distanceCloseness(self.__class__.waves,self.__class__.kmeans.fitByCourseValue,self.__class__.kmeans)
        selectedStocksWaves = self.__class__.diversificateAssets.getStocksGirvanNewman(4)
        valueList = self.__class__.calculateGains.calculateDiversificatedGains( selectedStocksWaves, 1000)
        
        self.assertEqual(min(valueList), 839.8365908003973)
        self.assertEqual(max(valueList), 1114.3082638645967)
        self.assertEqual(sum(valueList) / len(valueList), 928.8627236279441) 

    def test_CalculateGains_Kmeans_GenericDistance_4_Clusters(self):
        
        self.__class__.closenessGraph.distanceCloseness(self.__class__.waves,self.__class__.kmeans.fitDefault,self.__class__.kmeans)
        selectedStocksWaves = self.__class__.diversificateAssets.getStocksKmeans(4)
        valueList = self.__class__.calculateGains.calculateDiversificatedGains( selectedStocksWaves, 1000)
        
        self.assertEqual(min(valueList), 917.8202024038031)
        self.assertEqual(max(valueList), 1093.5460809866536)
        self.assertEqual(sum(valueList) / len(valueList), 995.9821176215814) 
        
    def test_CalculateGains_Kmeans_Course_4_Clusters(self):
        
        self.__class__.closenessGraph.distanceCloseness(self.__class__.waves,self.__class__.kmeans.fitByCourse,self.__class__.kmeans)
        selectedStocksWaves = self.__class__.diversificateAssets.getStocksKmeans(4)
        valueList = self.__class__.calculateGains.calculateDiversificatedGains( selectedStocksWaves, 1000)
        
        self.assertEqual(min(valueList), 905.8208845545857)
        self.assertEqual(max(valueList), 1105.6240093432173)
        self.assertEqual(sum(valueList) / len(valueList), 1005.887743195948) 
        
    def test_CalculateGains_Kmeans_CourseValue_4_Clusters(self):
        
        self.__class__.closenessGraph.distanceCloseness(self.__class__.waves,self.__class__.kmeans.fitByCourseValue,self.__class__.kmeans)
        selectedStocksWaves = self.__class__.diversificateAssets.getStocksKmeans(4)
        valueList = self.__class__.calculateGains.calculateDiversificatedGains( selectedStocksWaves, 1000)
        
        self.assertEqual(min(valueList), 877.3976479204921)
        self.assertEqual(max(valueList), 1163.1275171685043)
        self.assertEqual(sum(valueList) / len(valueList), 1013.3289673889219) 
        
if __name__ == '__main__':
    utest.main()