import random as rd
import numpy as np
import src.model.objects.wave.ComplexWave as cw
import src.model.objects.wave.ComplexWaveDB as ComplexWaveDB
import src.model.objects.graph.VisibilityGraph as vg
import src.model.objects.graph.ClosenessGraph as cg
import src.model.objects.wave.SimpleWave as sw
import src.model.modules.YahooFinanceAPI as yf
import src.model.modules.Fourier as fou
import src.model.modules.Wavelete as wlt
import pandas as pd
import src.model.objects.k_means.K_MeansVariation as km
import src.model.objects.k_means.K_MeansBetweenness as K_MeansBetweenness
import src.model.objects.k_means.K_MeansGraph as K_MeansGraph

import src.model.objects.Stock as sk
import networkx as nx
import time
import src.model.procedures.WavePrecision as WavePrecision
import src.model.procedures.DiversificateAssets as DiversificateAssets
import src.model.procedures.CalculateGains as CalculateGains

from networkx.algorithms.community.centrality import girvan_newman
import matplotlib.pyplot as plt
import itertools
import copy

class ValueResults:
    
    def __init__(self,debug=True):
        pass
        
    def createWave(self,dateStart,dateEnd,tickerList = [],debug=True):
        yf1=yf.YahooFinanceAPI(debug=debug)
        if tickerList != []:
            yf1.stocks = tickerList

        inputWaves =[]
        
        for element in yf1.stocks:
            
            cw3 = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocks.csv',dateStart,dateEnd)
            cw3.normalice()
            inputWaves.append(cw3)
        return inputWaves
    
    def createWaveGraph(self,dateStart,dateEnd,tickerList = [],debug=True):
        yf1=yf.YahooFinanceAPI(debug=debug)
        if tickerList != []:
            yf1.stocks = tickerList
        
        graphs = []
        
        for element in yf1.stocks:
            
            cw3 = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocks.csv',dateStart,dateEnd)
            cw3.normalice()
            vg2 = vg.VisibilityGraph(cw3.toGraph,cw3.dataName)
            
            graphs.append(vg2)
        
        
        km1 = km.K_MeansVariation(4)
        wavesBetweenness = km1.changeGraphToWave(graphs)
        orderedWavesBetweenness = km1.order(wavesBetweenness)
        return orderedWavesBetweenness

    def valueProcess(self,k,waves,inputWaves,realwaves,money,flag=0):
        
        aproxWave = cw.ComplexWave()
        realWave = cw.ComplexWave()
        
        cG = CalculateGains.CalculateGains()
        cg1 = cg.ClosenessGraph()
        dA = DiversificateAssets.DiversificateAssets(cg1,inputWaves)
        kmeans = km.K_MeansVariation(0)
        
        if flag == 0:
            aproxWave.dataName = "Default Aprox"
            realWave.dataName = "Default"
            cg1.distanceCloseness(waves,kmeans.fitDefault,kmeans)
        elif flag ==1:
            aproxWave.dataName = "Course Aprox"
            realWave.dataName = "Course"
            cg1.distanceCloseness(waves,kmeans.fitByCourse,kmeans)
        elif flag ==2:
            aproxWave.dataName = "CourseValue Aprox"
            realWave.dataName = "CourseValue"
            cg1.distanceCloseness(waves,kmeans.fitByCourseValue,kmeans)
        if flag == 3:
            aproxWave.dataName = "Default Graph Aprox"
            realWave.dataName = "Default Graph"
            cg1.distanceCloseness(waves,kmeans.fitDefault,kmeans)
        elif flag ==4:
            aproxWave.dataName = "Course Graph Aprox"
            realWave.dataName = "Course Graph"
            cg1.distanceCloseness(waves,kmeans.fitByCourse,kmeans)
        elif flag ==5:
            aproxWave.dataName = "CourseValue Graph Aprox"
            realWave.dataName = "CourseValue Graph"
            cg1.distanceCloseness(waves,kmeans.fitByCourseValue,kmeans)
            
        selectedStocksWaves = dA.getStocksKmeans(k)
        imputSelectedStocksWaves = []
        for i in range(len(selectedStocksWaves)):
            for wave in inputWaves:
                if wave.dataName == selectedStocksWaves[i].dataName:
                    imputSelectedStocksWaves.append(wave)
                    continue
        realSelectedStocksWaves = []
        for i in range(len(selectedStocksWaves)):
            for wave in realwaves:
                if wave.dataName == selectedStocksWaves[i].dataName:
                    realSelectedStocksWaves.append(wave)
                    continue    
                
        valueListInp =cG.calculateDiversificatedGains(imputSelectedStocksWaves, money)
        valueListReal =cG.calculateDiversificatedGains(realSelectedStocksWaves, money)   
        
        aproxWave.y = valueListInp
        realWave.y = valueListReal

        aproxWave.date = inputWaves[0].date
        realWave.date = realwaves[0].date


        print(dA.getVolatilityStandarDeviationProcess(valueListInp))
        print(dA.getVolatilityStandarDeviationProcess(valueListReal))
        #return [valueListInp,valueListReal]
        return [aproxWave,realWave]

    def equalDistribution(self,inputWaves,realwaves,money):
        cG = CalculateGains.CalculateGains()
        cg1 = cg.ClosenessGraph()
        dA = DiversificateAssets.DiversificateAssets(cg1,inputWaves)
        
        print('-----Distribución homogenea-----')
        equalDistributionAprox = cG.calculateDiversificatedGains(inputWaves, money)
        print(dA.getVolatilityStandarDeviationProcess(equalDistributionAprox))
        equalDistributionReal = cG.calculateDiversificatedGains(realwaves, money)
        print(dA.getVolatilityStandarDeviationProcess(equalDistributionReal))
        
        equalDistributionAproxWave = cw.ComplexWave()
        equalDistributionRealWave = cw.ComplexWave()
        equalDistributionAproxWave.y = equalDistributionAprox
        equalDistributionRealWave.y = equalDistributionReal
        equalDistributionAproxWave.date = inputWaves[0].date
        equalDistributionRealWave.date = realwaves[0].date   
        equalDistributionAproxWave.dataName = "equalDistributionAprox"
        equalDistributionRealWave.dataName = "equalDistributionReal"
        
        return[equalDistributionAproxWave,equalDistributionRealWave]

    def randomDistribution(self,k,inputWaves,realwaves,money):
        cG = CalculateGains.CalculateGains()
        cg1 = cg.ClosenessGraph()
        dA = DiversificateAssets.DiversificateAssets(cg1,inputWaves)
        
        print('-----Random Pick of '+str(k)+' waves-----')
        randomWaves = rd.sample(inputWaves, k)
        randomAprox = cG.calculateDiversificatedGains(randomWaves, money)
        print(dA.getVolatilityStandarDeviationProcess(randomAprox))
        randomWavesP = []
        for realwave in realwaves:
            for wave in randomWaves:
                if wave.dataName == realwave.dataName:
                    randomWavesP.append(realwave)
        randomReal = cG.calculateDiversificatedGains(randomWavesP, money)
        print(dA.getVolatilityStandarDeviationProcess(randomReal))
        randomAproxWave = cw.ComplexWave()
        randomRealWave = cw.ComplexWave()
        randomAproxWave.y = randomAprox
        randomRealWave.y = randomReal
        randomAproxWave.date = inputWaves[0].date
        randomRealWave.date = realwaves[0].date
        randomAproxWave.dataName = "randomAprox"
        randomRealWave.dataName = "randomReal"
        return [randomAproxWave,randomRealWave]
        
    def executeStandar(self,inputWaves,realwaves,money):
        
        k= len(realwaves)//3
        result =[]
        [aprox,real] = self.equalDistribution(inputWaves,realwaves,money)
        result.append(real)

        [aprox,real] = self.randomDistribution(k,inputWaves,realwaves,money)
        result.append(real)
        
        print('-----Least Volatile-----')
        [valueListLV,valueListLVP] = self.valueProcess(1,inputWaves,inputWaves,realwaves,money,0)        
        valueListLV.dataName = "LeastVolatileAprox"
        valueListLVP.dataName = "LeastVolatileReal"
        
        result.append(valueListLVP)
        
        print('-----------------Normal Wave-------------------')
        
        print('-----GenericDistance '+str(k)+'-----')
        [valueListGD,valueListGDP] = self.valueProcess(k,inputWaves,inputWaves,realwaves,money,0)        
        
        print('-----Course '+str(k)+'-----')
        [valueListC,valueListCP] = self.valueProcess(k,inputWaves,inputWaves,realwaves,money,1)        
        
        print('-----CourseValue '+str(k)+'-----')
        [valueListCV,valueListCVP] = self.valueProcess(k,inputWaves,inputWaves,realwaves,money,2)        
        
        result.append(valueListGDP)
        result.append(valueListCP)
        result.append(valueListCVP)
        return result
    
    def executeFull(self,inputWaves,waves,realwaves,money):
        
        k= len(realwaves)//3
        result =[]
        [aprox,real] = self.equalDistribution(inputWaves,realwaves,money)
        result.append(real)

        [aprox,real] = self.randomDistribution(k,inputWaves,realwaves,money)
        result.append(real)
        
        print('-----Least Volatile-----')
        [valueListLV,valueListLVP] = self.valueProcess(1,inputWaves,inputWaves,realwaves,money,0)        
        valueListLV.dataName = "LeastVolatileAprox"
        valueListLVP.dataName = "LeastVolatileReal"
        
        result.append(valueListLVP)
        
        print('-----------------Normal Wave-------------------')
        
        print('-----GenericDistance '+str(k)+'-----')
        [valueListGD,valueListGDP] = self.valueProcess(k,inputWaves,inputWaves,realwaves,money,0)        
        
        print('-----Course '+str(k)+'-----')
        [valueListC,valueListCP] = self.valueProcess(k,inputWaves,inputWaves,realwaves,money,1)        
        
        print('-----CourseValue '+str(k)+'-----')
        [valueListCV,valueListCVP] = self.valueProcess(k,inputWaves,inputWaves,realwaves,money,2)        
        
        result.append(valueListGDP)
        result.append(valueListCP)
        result.append(valueListCVP)

        print('-----------------Visibility Graph-------------------')
        
        print('-----GenericDistance '+str(k)+'-----')
        [valueListGGD,valueListGGDP] = self.valueProcess(k,waves,inputWaves,realwaves,money,3)        
        
        print('-----Course '+str(k)+'-----')
        [valueListGC,valueListGCP] = self.valueProcess(k,waves,inputWaves,realwaves,money,4)        
        
        print('-----CourseValue '+str(k)+'-----')
        [valueListGCV,valueListGCVP] = self.valueProcess(k,waves,inputWaves,realwaves,money,5)
        
        result.append(valueListGGDP)
        result.append(valueListGCP)
        result.append(valueListGCVP)
        return result
    
    def draw(self,valueListRD,valueListDH,valueListLV,valueListGD,valueListC,valueListCV):
        plt.figure(figsize = (8, 6))
        plt.title('Valor')
        x = np.arange(0,1,1.0/len(valueListLV))
        plt.plot(x,valueListRD,'k')
        plt.plot(x,valueListDH,'--')
        plt.plot(x,valueListLV,'-.')
        
        plt.plot(x,valueListGD,'g')
        plt.plot(x,valueListC,'y')
        plt.plot(x,valueListCV,'r')
        
        plt.show()
    
