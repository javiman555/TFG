import unittest as utest
import numpy.testing as ntest
from src.model.objects.wave import ComplexWaveDB

import src.model.modules.YahooFinanceAPI as yf
import src.model.objects.Stock as sk

import src.model.objects.k_means.K_MeansVariation as K_MeansVariation
import src.model.objects.graph.VisibilityGraph as vg
import src.model.objects.graph.ClosenessGraph as cg


class TestGraph(utest.TestCase):
     
    @classmethod
    def setUpClass(cls):
        yf1=yf.YahooFinanceAPI(debug=True)
        cls.waves =[]
        
        for element in yf1.stocks:
            
            wave = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocksTest.csv')
            wave.normalice()
            cls.waves.append(wave)        
        
        
       
    def test_get_closeness_graph_distanceCloseness(self):
        closenessGraph = cg.ClosenessGraph()
        kmeans = K_MeansVariation.K_MeansVariation(0)
        closenessGraph.distanceCloseness(self.__class__.waves,kmeans.fitDefault,kmeans)
        self.assertEqual(len(closenessGraph.edges), 39)
        self.assertEqual(len(closenessGraph.nodes), 14)
        
    def test_get_closeness_graph_kmeansLoop_1(self):
        closenessGraph = cg.ClosenessGraph()
        closenessGraph.kmeansLoop(self.__class__.waves,1)
        self.assertEqual(len(closenessGraph.edges), 0)
        self.assertEqual(len(closenessGraph.nodes), 14)
    
    #Does not work but kmeansLoop is not used
    '''    
    def test_get_closeness_graph_kmeansLoop_Max(self):
        closenessGraph = cg.ClosenessGraph()
        closenessGraph.kmeansLoop(self.__class__.waves,100)
        self.assertEqual(len(closenessGraph.edges), 91)
        self.assertEqual(len(closenessGraph.nodes), 14) 
    '''   
    def test_get_visibility_graph_form_SAB_MC(self):
        wave=self.__class__.waves[0]
        visibilityGraph = vg.VisibilityGraph(wave.toGraph,wave.dataName)  # 3700 ms
        self.assertEqual(visibilityGraph.dataName, 'SAB.MC (Open)')
        self.assertEqual(len(visibilityGraph.edges), 1558)
        self.assertEqual(len(visibilityGraph.nodes), 258)
        


if __name__ == '__main__':
    utest.main()