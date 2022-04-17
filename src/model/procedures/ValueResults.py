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
        self.actualizedStocks = self.createRealWave(debug=debug)
        self.inputStocks = self.createWave(debug=debug)
        self.inputStocksByGraph = self.createWaveGraph(debug=debug)
        
    def createRealWave(self,debug=True):
        
        yf1=yf.YahooFinanceAPI(debug=debug)
        if not debug:
            yf1.saveStocksStartEnd('2021-01-01','2023-01-01','1d',True,'DataStocks2.csv')
            #yf1.saveStocks('1y','1d',True,'DataStocks2.csv')
        
        realwaves =[]
        
        for element in yf1.stocks:
            
            cw3 = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocks2.csv')
            realwaves.append(cw3)
        return realwaves
    
    def createWave(self,debug=True):
        yf1=yf.YahooFinanceAPI(debug=debug)
        if not debug:
            yf1.saveStocksStartEnd('2021-01-01','2022-01-01','1d',True,'DataStocks.csv')
        
        inputWaves =[]
        
        for element in yf1.stocks:
            
            cw3 = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocks.csv')
            cw3.normalice()
            inputWaves.append(cw3)
        return inputWaves
    
    def createWaveGraph(self,debug=True):
        yf1=yf.YahooFinanceAPI(debug=debug)
        
        
        inputWaves =[]
        graphs = []
        
        for element in yf1.stocks:
            
            cw3 = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocks.csv')
            cw3.normalice()
            vg2 = vg.VisibilityGraph(cw3.toGraph,cw3.dataName)
            
            graphs.append(vg2)
            inputWaves.append(cw3)
        
        
        km1 = km.K_MeansVariation(4)
        wavesBetweenness = km1.changeGraphToWave(graphs)
        orderedWavesBetweenness = km1.order(wavesBetweenness)
        return orderedWavesBetweenness

    def valueProcess(self,k,waves,inputWaves,realwaves,flag=0):
        
        cG = CalculateGains.CalculateGains()
        cg1 = cg.ClosenessGraph()
        dA = DiversificateAssets.DiversificateAssets(cg1,inputWaves)
        kmeans = km.K_MeansVariation(0)
        
        if flag == 0:
            cg1.distanceCloseness(waves,kmeans.fitDefault,kmeans)
        elif flag ==1:
            cg1.distanceCloseness(waves,kmeans.fitByCourse,kmeans)
        elif flag ==2:
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
                
        valueListInp =cG.calculateDiversificatedGains(imputSelectedStocksWaves, 1000)
        valueListReal =cG.calculateDiversificatedGains(realSelectedStocksWaves, 1000)

        print(dA.getVolatilityStandarDeviationProcess(valueListInp))
        print(dA.getVolatilityStandarDeviationProcess(valueListReal))
        return [valueListInp,valueListReal]

    def execute(self):
        
        inputWaves = self.inputStocks
        
        waves = self.inputStocksByGraph
        
        
        realwaves = self.actualizedStocks
        
        
        print('-----Distribución homogenea-----')
        cG = CalculateGains.CalculateGains()
        cg1 = cg.ClosenessGraph()
        dA = DiversificateAssets.DiversificateAssets(cg1,inputWaves)
        
        valueListDH = cG.calculateDiversificatedGains(inputWaves, 1000)
        print(dA.getVolatilityStandarDeviationProcess(valueListDH))

        valueListDHP = cG.calculateDiversificatedGains(realwaves, 1000)
        print(dA.getVolatilityStandarDeviationProcess(valueListDHP))

        k= len(realwaves)//3
        print('-----Random Pick of '+str(k)+' waves-----')
        randomWaves = rd.sample(inputWaves, k)
        cumulativeValue = cG.calculateDiversificatedGains(randomWaves, 1000)
        print(dA.getVolatilityStandarDeviationProcess(cumulativeValue))
        randomWavesP = []
        for realwave in realwaves:
            for wave in randomWaves:
                if wave.dataName == realwave.dataName:
                    randomWavesP.append(realwave)
        cumulativeValueP = cG.calculateDiversificatedGains(randomWavesP, 1000)
        print(dA.getVolatilityStandarDeviationProcess(cumulativeValueP))        
        
        print('-----Least Volatile-----')
        [valueListLV,valueListLVP] = self.valueProcess(1,inputWaves,inputWaves,realwaves,0)        
        
        print('-----------------Normal Wave-------------------')
        
        print('-----GenericDistance '+str(k)+'-----')
        [valueListGD,valueListGDP] = self.valueProcess(k,inputWaves,inputWaves,realwaves,0)        
        
        print('-----Course '+str(k)+'-----')
        [valueListC,valueListCP] = self.valueProcess(k,inputWaves,inputWaves,realwaves,1)        
        
        print('-----CourseValue '+str(k)+'-----')
        [valueListCV,valueListCVP] = self.valueProcess(k,inputWaves,inputWaves,realwaves,2)        

        
        self.draw(cumulativeValue,valueListDH,valueListLV,valueListGD,valueListC,valueListCV)
        
        self.draw(cumulativeValueP,valueListDHP,valueListLVP,valueListGDP,valueListCP,valueListCVP)
        
        print('-----------------Visibility Graph-------------------')
        
        print('-----GenericDistance '+str(k)+'-----')
        [valueListGD,valueListGDP] = self.valueProcess(k,waves,inputWaves,realwaves,0)        
        
        print('-----Course '+str(k)+'-----')
        [valueListC,valueListCP] = self.valueProcess(k,waves,inputWaves,realwaves,1)        
        
        print('-----CourseValue '+str(k)+'-----')
        [valueListCV,valueListCVP] = self.valueProcess(k,waves,inputWaves,realwaves,2)

        self.draw(cumulativeValue,valueListDH,valueListLV,valueListGD,valueListC,valueListCV)
        
        self.draw(cumulativeValueP,valueListDHP,valueListLVP,valueListGDP,valueListCP,valueListCVP)

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
    
