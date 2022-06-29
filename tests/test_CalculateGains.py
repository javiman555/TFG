import unittest as utest
import numpy.testing as ntest
from src.model.objects.wave import ComplexWaveDB

import src.model.modules.YahooFinanceAPI as yf
import src.model.objects.Stock as sk

import src.model.objects.k_means.K_Means as K_Means
import src.model.objects.graph.VisibilityGraph as vg
import src.model.objects.graph.ClosenessGraph as cg
import src.model.procedures.DiversificateAssets as DiversificateAssets
import src.model.objects.k_means.K_MeansVariation as K_MeansVariation
import src.model.procedures.CalculateGains as CalculateGains


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
        
        self.assertEqual(min(valueList), 936.885997447037)
        self.assertEqual(max(valueList), 1120.5408882289091)
        self.assertEqual(sum(valueList) / len(valueList), 1061.0839892761371) 
       
    def test_CalculateGains_GN_GenericDistance_4_Clusters(self):
        
        self.__class__.closenessGraph.distanceCloseness(self.__class__.waves,self.__class__.kmeans.fitDefault,self.__class__.kmeans)
        selectedStocksWaves = self.__class__.diversificateAssets.getStocksGirvanNewman(4)
        valueList = self.__class__.calculateGains.calculateDiversificatedGains( selectedStocksWaves, 1000)
        
        self.assertEqual(min(valueList), 974.8577531648356)
        self.assertEqual(max(valueList), 1206.6563680705563)
        self.assertEqual(sum(valueList) / len(valueList), 1110.301960639932) 
        
    def test_CalculateGains_GN_Course_4_Clusters(self):
        
        self.__class__.closenessGraph.distanceCloseness(self.__class__.waves,self.__class__.kmeans.fitByCourse,self.__class__.kmeans)
        selectedStocksWaves = self.__class__.diversificateAssets.getStocksGirvanNewman(4)
        valueList = self.__class__.calculateGains.calculateDiversificatedGains( selectedStocksWaves, 1000)
        
        self.assertEqual(min(valueList), 989.1558061985547)
        self.assertEqual(max(valueList), 1119.1423910843205)
        self.assertEqual(sum(valueList) / len(valueList), 1059.4877483145247) 
        
    def test_CalculateGains_GN_CourseValue_4_Clusters(self):
        
        self.__class__.closenessGraph.distanceCloseness(self.__class__.waves,self.__class__.kmeans.fitByCourseValue,self.__class__.kmeans)
        selectedStocksWaves = self.__class__.diversificateAssets.getStocksGirvanNewman(4)
        valueList = self.__class__.calculateGains.calculateDiversificatedGains( selectedStocksWaves, 1000)
        
        self.assertEqual(min(valueList), 840.5533607148506)
        self.assertEqual(max(valueList), 1015.3496848609175)
        self.assertEqual(sum(valueList) / len(valueList), 955.9712631781456) 

    def test_CalculateGains_Kmeans_GenericDistance_4_Clusters(self):
        
        self.__class__.closenessGraph.distanceCloseness(self.__class__.waves,self.__class__.kmeans.fitDefault,self.__class__.kmeans)
        selectedStocksWaves = self.__class__.diversificateAssets.getStocksKmeans(4)
        valueList = self.__class__.calculateGains.calculateDiversificatedGains( selectedStocksWaves, 1000)
        
        self.assertEqual(min(valueList), 995.5872161568872)
        self.assertEqual(max(valueList), 1204.9514027826972)
        self.assertEqual(sum(valueList) / len(valueList), 1098.425957588624) 
        
    def test_CalculateGains_Kmeans_Course_4_Clusters(self):
        
        self.__class__.closenessGraph.distanceCloseness(self.__class__.waves,self.__class__.kmeans.fitByCourse,self.__class__.kmeans)
        selectedStocksWaves = self.__class__.diversificateAssets.getStocksKmeans(4)
        valueList = self.__class__.calculateGains.calculateDiversificatedGains( selectedStocksWaves, 1000)
        
        self.assertEqual(min(valueList), 952.0767859617446)
        self.assertEqual(max(valueList), 1107.5214774205947)
        self.assertEqual(sum(valueList) / len(valueList), 1027.2736178749096) 
        
    def test_CalculateGains_Kmeans_CourseValue_4_Clusters(self):
        
        self.__class__.closenessGraph.distanceCloseness(self.__class__.waves,self.__class__.kmeans.fitByCourseValue,self.__class__.kmeans)
        selectedStocksWaves = self.__class__.diversificateAssets.getStocksKmeans(4)
        valueList = self.__class__.calculateGains.calculateDiversificatedGains( selectedStocksWaves, 1000)
        
        self.assertEqual(min(valueList), 918.0268822134751)
        self.assertEqual(max(valueList), 1077.7606546408413)
        self.assertEqual(sum(valueList) / len(valueList), 1025.9289784225482) 
        
if __name__ == '__main__':
    utest.main()