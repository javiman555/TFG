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


class TestDiversificateAssets(utest.TestCase):
     
    @classmethod
    def setUpClass(cls):
        yf1=yf.YahooFinanceAPI(debug=True)
        waves =[]
        for element in yf1.stocks:
            
            wave = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocksTest.csv')
            wave.normalice()
            waves.append(wave)

        closenessGraph = cg.ClosenessGraph()
        kmeans = K_MeansVariation.K_MeansVariation(0)
        closenessGraph.distanceCloseness(waves,kmeans.fitDefault,kmeans)
        cls.diversificateAssets = DiversificateAssets.DiversificateAssets(closenessGraph,waves)

    def test_get_DiversificateAssets_clusters_Kmeans_4(self):
        
        da4=self.__class__.diversificateAssets
        selectedStocks = da4.getStocksKmeans(4)
        
        self.assertEqual(len(da4.clusters), 4)
        self.assertEqual(len(da4.clusters[0]), 5)
        self.assertEqual(len(da4.clusters[1]), 2)
        
        self.assertEqual(len(selectedStocks), 4)
        self.assertEqual(selectedStocks[0].dataName, 'CABK.MC (Open)') 
        self.assertEqual(selectedStocks[1].dataName, 'SAN.MC (Open)') 
        self.assertEqual(selectedStocks[2].dataName, 'ENG.MC (Open)') 
        self.assertEqual(selectedStocks[3].dataName, 'ELE.MC (Open)')
       
    def test_get_DiversificateAssets_clusters_GN_4(self):
        
        da4=self.__class__.diversificateAssets
        selectedStocks = da4.getStocksGirvanNewman(4)
        
        self.assertEqual(len(da4.clusters), 4)
        self.assertEqual(len(da4.clusters[0]), 5)
        self.assertEqual(len(da4.clusters[1]), 7)
        
        self.assertEqual(len(selectedStocks), 4)
        self.assertEqual(selectedStocks[0].dataName, 'CABK.MC (Open)') 
        self.assertEqual(selectedStocks[1].dataName, 'ENG.MC (Open)') 
        self.assertEqual(selectedStocks[2].dataName, 'GRF.MC (Open)') 
        self.assertEqual(selectedStocks[3].dataName, 'CLNX.MC (Open)') 

        



if __name__ == '__main__':
    utest.main()