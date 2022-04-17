import unittest as utest
import numpy.testing as ntest
from src.model.objects.wave import ComplexWaveDB

import src.model.modules.YahooFinanceAPI as yf

import src.model.objects.k_means.K_Means as K_Means
import src.model.objects.k_means.K_MeansVariation as K_MeansVariation



class TestKMeans(utest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        yf1=yf.YahooFinanceAPI(debug=True) 
        
        cls.waves =[]

        
        for element in yf1.stocks:
            
            complexWave = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocksTest.csv')
            complexWave.normalice()
            cls.waves.append(complexWave)
            
    def test_generic_kmeans_14_waves_1_boxes(self):
        waves = self.__class__.waves
        kMeans = K_Means.K_Means(1)
        kMeans.fitDefault(waves)
        self.assertEqual(len(kMeans.boxes[0]), 14)
        
    def test_generic_kmeans_14_waves_4_boxes(self):
        waves = self.__class__.waves
        kMeans = K_Means.K_Means(4)
        kMeans.fitDefault(waves)
        self.assertEqual(len(kMeans.boxes[0]), 1)
        self.assertEqual(len(kMeans.boxes[1]), 4)
        self.assertEqual(len(kMeans.boxes[2]), 7)
        self.assertEqual(len(kMeans.boxes[3]), 2)
        
    def test_generic_kmeans_14_waves_14_boxes(self):
        waves = self.__class__.waves
        kMeans = K_Means.K_Means(14)
        kMeans.fitDefault(waves)
        self.assertEqual(len(kMeans.boxes), 14)

    def test_course_kmeans_14_waves_4_boxes(self):
        waves = self.__class__.waves
        kMeans = K_MeansVariation.K_MeansVariation(4)
        kMeans.fitByCourse(waves)
        self.assertEqual(len(kMeans.boxes[0]), 2)
        self.assertEqual(len(kMeans.boxes[1]), 2)
        self.assertEqual(len(kMeans.boxes[2]), 3)
        self.assertEqual(len(kMeans.boxes[3]), 7)

        
    def test_numberOfGains_kmeans_14_waves_4_boxes(self):
        waves = self.__class__.waves
        kMeans = K_MeansVariation.K_MeansVariation(4)
        kMeans.fitNumberOfGains(waves)
        self.assertEqual(len(kMeans.boxes[0]), 3)
        self.assertEqual(len(kMeans.boxes[1]), 5)
        self.assertEqual(len(kMeans.boxes[2]), 2)
        self.assertEqual(len(kMeans.boxes[3]), 4)

        
if __name__ == '__main__':
    utest.main()