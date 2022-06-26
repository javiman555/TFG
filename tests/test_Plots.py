import unittest as utest
import numpy.testing as ntest
from src.model.objects.wave import ComplexWaveDB
from src.model.objects.wave import ComplexWaveRandom

import src.model.objects.graph.VisibilityGraph as vg
import src.model.objects.k_means.K_MeansVariation as K_MeansVariation

import src.model.modules.YahooFinanceAPI as yf
import src.model.objects.Stock as sk
import src.model.modules.Wavelete as Wavelete
import src.model.modules.Fourier as Fourier

import src.model.objects.k_means.K_Means as K_Means
import src.model.objects.graph.ClosenessGraph as cg
import matplotlib.pyplot as plt
import numpy as np


#@utest.SkipTest
class TestPlots(utest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        yf1=yf.YahooFinanceAPI(debug=False)
        cls.waves =[]
        cls.vgraphs = []
        cls.stocks=[]
        for element in yf1.stocks:
            
            wave = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocks.csv')
                        
            stock=sk.Stock(element,'DataStocks.csv',precision=2)
            cls.stocks.append(stock)
            
            #wave.draw(wave.y)
                
            wave.normalice()
            cls.waves.append(wave)  
            
            vgraph = vg.VisibilityGraph(wave.toGraph,wave.dataName)  # 3700 ms
            cls.vgraphs.append(vgraph)
    @utest.SkipTest        
    def test_draw_artificial_wave(self):
        wave = ComplexWaveRandom.ComplexWaveRandom(2,10,10,10,365)
        wave.draw(wave.y) 
    @utest.SkipTest    
    def test_draw_wave(self):
        wave = self.__class__.waves[1]
        wave.draw(wave.y)  
        
    @utest.SkipTest     
    def test_draw_wave_course(self):
        kmeans = K_MeansVariation.K_MeansVariation(4)
        wave = self.__class__.waves[1]
        wave = kmeans.changeWaveToCourse(wave)
        wave.draw(wave.y)
    @utest.SkipTest   
    def test_draw_wave_course_value(self):
        kmeans = K_MeansVariation.K_MeansVariation(4)
        wave = self.__class__.waves[1]
        wave = kmeans.changeWaveToCourseValue(wave)
        wave.draw(wave.y)  
        
    @utest.SkipTest    
    def test_draw_wave_fourier(self):
        fourier = Fourier.Fourier()
        wave = self.__class__.waves[1]
        wave = fourier.DFT(wave)
        wave.draw(wave.y)
    @utest.SkipTest    
    def test_draw_wave_wavelete(self):
        wavelet = Wavelete.Wavelete()
        
        wave = self.__class__.waves[1]
        wave = wavelet.simplificationComplexWave(wave)
        wave.draw(wave.y)
        wave = wavelet.simplificationComplexWave(wave)
        wave.draw(wave.y)
        wave = wavelet.simplificationComplexWave(wave)
        wave.draw(wave.y)
        wave = wavelet.simplificationComplexWave(wave)
        wave.draw(wave.y)

    #@utest.SkipTest    
    def test_draw_VisibilityGraph(self):
        
        vgraph = self.__class__.vgraphs[1]
        plt.title('Visibility Graph of Wave: '+vgraph.dataName+' by Degree')
        vgraph.drawGraphByDegreeFancy()
        plt.title('Representation of Visibility Graph: '+vgraph.dataName+' by Betweenness')
        vgraph.drawVisibilityByBetweenness()
        plt.figure(figsize=(4,3))
        plt.title('Visibility Graph: '+vgraph.dataName+' Betweenness')
        vgraph.drawGraphByBetweennessFancy()
    @utest.SkipTest
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
        plt.suptitle('RxR representation',fontsize=20)
        plt.scatter([.9],[.2],color="black",zorder=10)
        plt.ylim([0,1])
        plt.xlim([0,1])
        plt.show
        kmeans.paintAll(2,2)
    @utest.SkipTest    
    def test_draw_ClosenessGraph(self):
        n=12
        plt.figure(figsize=(n,n)) 
        kmeans = K_MeansVariation.K_MeansVariation(1)
        cgraph = cg.ClosenessGraph()
        plt.title('Graph by cyclic K-means')
        cgraph.distanceCloseness(self.__class__.waves,kmeans.fitDefault,kmeans)
        cgraph.drawGraphByBetweenness()
        plt.figure(figsize=(n,n)) 
        plt.title('Graph by cyclic K-means (not inverted)')
        cgraph.calibrateWeightMax()
        cgraph.drawGraphByBetweenness()
        plt.figure(figsize=(n,n)) 
        plt.title('ClosenessGraph by course with kmeans')
        cgraph.distanceCloseness(self.__class__.waves,kmeans.fitByCourse,kmeans)
        cgraph.drawGraphByBetweenness()
        plt.figure(figsize=(n,n)) 
        plt.title('ClosenessGraph by course value with kmeans')
        cgraph.distanceCloseness(self.__class__.waves,kmeans.fitByCourseValue,kmeans)
        cgraph.drawGraphByBetweenness()
        plt.figure(figsize=(n,n)) 
        plt.title('ClosenessGraph by generic distance without kmeans')
        cgraph.genericDistance(self.__class__.waves)
        cgraph.drawGraphByDegree()
        
        listCourseWave=[None]*len(self.__class__.waves)
        for i in range(len(self.__class__.waves)):
            listCourseWave[i]=kmeans.changeWaveToCourse(self.__class__.waves[i])
        plt.title('ClosenessGraph by course pseudodistance without kmeans')
        cgraph.genericDistance(listCourseWave)
        cgraph.drawGraphByDegree()
    @utest.SkipTest    
    def test_draw_stock_high_low(self):
        
        stock = self.__class__.stocks[1]
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