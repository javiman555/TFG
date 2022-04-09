import unittest as utest
import numpy.testing as ntest
from src.objects.wave import ComplexWaveDB
import src.objects.graph.VisibilityGraph as vg
import src.objects.k_means.K_MeansVariation as K_MeansVariation

import src.modules.YahooFinanceAPI as yf
import src.objects.Stock as sk

import src.objects.k_means.K_Means as K_Means
import src.objects.graph.ClosenessGraph as cg
import matplotlib.pyplot as plt
import numpy as np


@utest.SkipTest
class TestPlots(utest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        yf1=yf.YahooFinanceAPI(debug=True)
        cls.waves =[]
        cls.vgraphs = []
        cls.stocks=[]
        
        for element in yf1.stocks:
            
            wave = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocksTest.csv')
            wave.normalice()
            cls.waves.append(wave)  
                        
            stock=sk.Stock(element,precision=2)
            cls.stocks.append(stock)
            
            vgraph = vg.VisibilityGraph(wave.toGraph,wave.dataName)  # 3700 ms
            cls.vgraphs.append(vgraph)
            
    def test_draw_wave(self):
        
        wave = self.__class__.waves[0]
        wave.draw(wave.y)
        
    def test_draw_VisibilityGraph(self):
        
        vgraph = self.__class__.vgraphs[0]
        plt.title('Visibility Graph of Wave: '+vgraph.dataName+' by Degree')
        vgraph.drawGraphByDegreeFancy()
        plt.title('Representation in Wave of Visibility Graph: '+vgraph.dataName+' by Degree')
        vgraph.drawVisibilityByDegree()
        plt.title('Visibility Graph of Wave: '+vgraph.dataName+' by Degree')
        vgraph.drawGraphByBetweennessFancy()

    def test_draw_kmeans_boxes(self):
        
        waves = self.__class__.waves
        kmeans = K_MeansVariation.K_MeansVariation(4)
        kmeans.fitDefault(waves)
        plt.figure(figsize=(16,12))
        plt.suptitle('Kmeans generic distance',fontsize=20)
        kmeans.paintAll(2,2)
        kmeans.fitByCourse(waves)
        plt.figure(figsize=(16,12))
        plt.suptitle('Kmeans generic course',fontsize=20)
        kmeans.paintAll(2,2)
        kmeans.fitByCourseValue(waves)
        plt.figure(figsize=(16,12))
        plt.suptitle('Kmeans generic course value',fontsize=20)
        kmeans.paintAll(2,2)
        
    def test_draw_ClosenessGraph(self):
        
        kmeans = K_MeansVariation.K_MeansVariation(0)
        cgraph = cg.ClosenessGraph()
        plt.title('ClosenessGraph by generic distance with kmeans')
        cgraph.distanceCloseness(self.__class__.waves,kmeans.fitDefault,kmeans)
        cgraph.drawGraphByBetweenness()
        plt.title('ClosenessGraph by course with kmeans')
        cgraph.distanceCloseness(self.__class__.waves,kmeans.fitByCourse,kmeans)
        cgraph.drawGraphByBetweenness()
        plt.title('ClosenessGraph by course value with kmeans')
        cgraph.distanceCloseness(self.__class__.waves,kmeans.fitByCourseValue,kmeans)
        cgraph.drawGraphByBetweenness()
        plt.title('ClosenessGraph by generic distance without kmeans')
        cgraph.genericDistance(self.__class__.waves)
        cgraph.drawGraphByDegree()
        
        listCourseWave=[None]*len(self.__class__.waves)
        for i in range(len(self.__class__.waves)):
            listCourseWave[i]=kmeans.changeWaveToCourse(self.__class__.waves[i])
        plt.title('ClosenessGraph by course pseudodistance without kmeans')
        cgraph.genericDistance(listCourseWave)
        cgraph.drawGraphByDegree()
        
    def test_draw_stock_high_low(self):
        
        stock = self.__class__.stocks[0]
        high =stock.high.y
        low =stock.low.y
        
        mean = self.mean(high,low)

        #Calculate points for max volatility
        average =[]
        highPart=[]
        lowPart=[]
        for i in range(len(high)):
            average.append((high[i]+low[i])/2)
            averageValue=((high[i]+low[i])/2)
            if averageValue <= mean:
                highPart.append(mean)
                lowPart.append(low[i])
            else:
                highPart.append(high[i])
                lowPart.append(mean)
        
        plt.title('Stock maximum volatility')
        self.drawplot(highPart,'g')
        self.drawplot(lowPart,'r')
        plt.axhline(y = mean, color = 'k', linestyle = '-')
        plt.show()

        plt.title('Stock maximum volatility')
        self.drawplot(average,'b')
        plt.axhline(y = mean, color = 'k', linestyle = '-')
        stock.drawHighLow()
        
        
    def drawplot(self,data,colour):
        sr = len(data)
        # sampling interval
        ts = 1.0/sr
        x = np.arange(0,1,ts)
        if len(x) != len(data):
            x = np.delete(x,0)
            
        plt.plot(x,data,colour)

    def mean(self,high,low):
        counter = 0
        for i in range(len(high)):
            counter +=high[i]+low[i]
        mean = counter/(2*len(high))
        return mean

if __name__ == '__main__':
    utest.main()