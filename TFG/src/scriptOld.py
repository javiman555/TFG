import random as rd
import numpy as np
import objects.wave.ComplexWave as cw
import objects.wave.ComplexWaveDB as ComplexWaveDB
import objects.graph.VisibilityGraph as vg
import objects.graph.ClosenessGraph as cg
import objects.wave.SimpleWave as sw
import modules.YahooFinanceAPI as yf
import modules.Fourier as fou
import modules.Wavelete as wlt
import pandas as pd
import objects.k_means.K_MeansVariation as km
import objects.k_means.K_MeansGraph as K_MeansGraph

import objects.Stock as sk
import networkx as nx
import time
import procedures.WavePrecision as WavePrecision
import procedures.DiversificateAssets as DiversificateAssets
import procedures.CalculateGains as CalculateGains

from networkx.algorithms.community.centrality import girvan_newman
import matplotlib.pyplot as plt
import itertools
import copy



start = time.time()

yf1 = yf.YahooFinanceAPI()
yf1.saveStocks('1y','1d',True,'DataStocks2.csv')

data=pd.read_csv('../resources/data/DataStocks.csv',header=0)
    
criteria = (data['ticker'] =="SAB.MC")
data=data[criteria]
cer=int(data['Open'].size)



yf1=yf.YahooFinanceAPI(debug=True)


imputWaves =[]
graphs = []
stocks=[]
volatility = []

for element in yf1.stocks:
    
    cw3 = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocks.csv')
    
    sk1=sk.Stock(element,'DataStocks.csv',precision=2)
    stocks.append(sk1)

    volatility.append(sk1.volatilityStandarDeviationOpen)
        
    cw3.normalice()
    
    vg2 = vg.VisibilityGraph(cw3.toGraph,cw3.dataName)
    graphs.append(vg2)
    
    imputWaves.append(cw3)


km1 = km.K_MeansVariation(4)
wavesBetweenness = km1.changeGraphToWave(graphs)
orderedWavesBetweenness = km1.order(wavesBetweenness)
waves = orderedWavesBetweenness


WavePrecision = WavePrecision.WavePrecision(waves)
print(WavePrecision.compareWavelete())

listCourseWave=[None]*len(waves)
for i in range(len(waves)):
    
    listCourseWave[i]=km1.changeWaveToCourseValue(waves[i])


cg1 = cg.ClosenessGraph()
dA = DiversificateAssets.DiversificateAssets(cg1,imputWaves)
#cg1.genericDistance(listCourseWave)

kmeans = km.K_MeansVariation(0)
cg1.distanceCloseness(waves,kmeans.fitDefault,kmeans)
cg1.drawGraphByDegree()


realwaves =[]

for element in yf1.stocks:
    
    cw3 = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocks2.csv')
    realwaves.append(cw3)



print('-----Distribución homogenea-----')
cG = CalculateGains.CalculateGains()
valueListDH = cG.calculateDiversificatedGains(imputWaves, 1000)
print(sum(valueListDH) / len(valueListDH))
print(max(valueListDH) - min(valueListDH))
valueListDHP = cG.calculateDiversificatedGains(realwaves, 1000)
print(sum(valueListDHP) / len(valueListDHP))
print(max(valueListDHP) - min(valueListDHP))

n1= 4
print('-----Least Volatile-----')
selectedStocksWaves = dA.getStocksGirvanNewman(1)
dA.drawClusters()

realSelectedStocksWaves = []
for i in range(len(selectedStocksWaves)):
    for wave in realwaves:
        if wave.dataName == selectedStocksWaves[i].dataName:
            realSelectedStocksWaves.append(wave)
            continue
imputSelectedStocksWaves = []
for i in range(len(selectedStocksWaves)):
    for wave in imputWaves:
        if wave.dataName == selectedStocksWaves[i].dataName:
            imputSelectedStocksWaves.append(wave)
            continue
 
cG = CalculateGains.CalculateGains()
valueListLV =cG.calculateDiversificatedGains(imputSelectedStocksWaves, 1000)
print(sum(valueListLV) / len(valueListLV))
print(max(valueListLV) - min(valueListLV))
valueListLVP =cG.calculateDiversificatedGains(realSelectedStocksWaves, 1000)
print(sum(valueListLVP) / len(valueListLVP))
print(max(valueListLVP) - min(valueListLVP))

print('-----GenericDistance '+str(n1)+'-----')
selectedStocksWaves = dA.getStocksKmeans(n1)
dA.drawClusters()

realSelectedStocksWaves = []
for i in range(len(selectedStocksWaves)):
    for wave in realwaves:
        if wave.dataName == selectedStocksWaves[i].dataName:
            realSelectedStocksWaves.append(wave)
            continue
imputSelectedStocksWaves = []
for i in range(len(selectedStocksWaves)):
    for wave in imputWaves:
        if wave.dataName == selectedStocksWaves[i].dataName:
            imputSelectedStocksWaves.append(wave)
            continue
        
cG = CalculateGains.CalculateGains()
valueListGD =cG.calculateDiversificatedGains(imputSelectedStocksWaves, 1000)
print(sum(valueListGD) / len(valueListGD))
print(max(valueListGD) - min(valueListGD))

valueListGDP =cG.calculateDiversificatedGains(realSelectedStocksWaves, 1000)
print(sum(valueListGDP) / len(valueListGDP))
print(max(valueListGDP) - min(valueListGDP))


print('-----Course '+str(n1)+'-----')
cg1.distanceCloseness(waves,kmeans.fitByCourse,kmeans)
selectedStocksWaves = dA.getStocksKmeans(n1)
dA.drawClusters()
realSelectedStocksWaves = []
for i in range(len(selectedStocksWaves)):
    for wave in realwaves:
        if wave.dataName == selectedStocksWaves[i].dataName:
            realSelectedStocksWaves.append(wave)
            continue
imputSelectedStocksWaves = []
for i in range(len(selectedStocksWaves)):
    for wave in imputWaves:
        if wave.dataName == selectedStocksWaves[i].dataName:
            imputSelectedStocksWaves.append(wave)
            continue
        
valueListC =cG.calculateDiversificatedGains(imputSelectedStocksWaves, 1000)
print(sum(valueListC) / len(valueListC))
print(max(valueListC) - min(valueListC))
valueListCP =cG.calculateDiversificatedGains(realSelectedStocksWaves, 1000)

print(sum(valueListCP) / len(valueListCP))
print(max(valueListCP) - min(valueListCP))
    
print('-----CourseValue '+str(n1)+'-----')
cg1.distanceCloseness(waves,kmeans.fitByCourseValue,kmeans)
selectedStocksWaves = dA.getStocksKmeans(n1)
dA.drawClusters()
realSelectedStocksWaves = []
for i in range(len(selectedStocksWaves)):
    for wave in realwaves:
        if wave.dataName == selectedStocksWaves[i].dataName:
            realSelectedStocksWaves.append(wave)
            continue
imputSelectedStocksWaves = []
for i in range(len(selectedStocksWaves)):
    for wave in imputWaves:
        if wave.dataName == selectedStocksWaves[i].dataName:
            imputSelectedStocksWaves.append(wave)
            continue
        
valueListCV =cG.calculateDiversificatedGains(imputSelectedStocksWaves, 1000)
print(sum(valueListCV) / len(valueListCV))
print(max(valueListCV) - min(valueListCV))
valueListCVP =cG.calculateDiversificatedGains(realSelectedStocksWaves, 1000)
print(sum(valueListCVP) / len(valueListCVP))
print(max(valueListCVP) - min(valueListCVP))


plt.figure(figsize = (8, 6))
plt.title('Valor')
x = np.arange(0,1,1.0/len(valueListCVP))
plt.plot(x,valueListDH,'--')
plt.plot(x,valueListLV,'-.')

plt.plot(x,valueListGD,'g')
plt.plot(x,valueListC,'y')
plt.plot(x,valueListCV,'r')

plt.show()
        
plt.figure(figsize = (8, 6))
plt.title('Valor')
x = np.arange(0,1,1.0/len(valueListCVP))
plt.plot(x,valueListDHP,'--')
plt.plot(x,valueListLVP,'-.')

plt.plot(x,valueListGDP,'g')
plt.plot(x,valueListCP,'y')
plt.plot(x,valueListCVP,'r')

plt.show()


km1.fitDefault(waves)
km1.paintAll(2,2)
km1.fitByCourse(waves)
km1.paintAll(2,2)
km1.fitByCourseValue(waves)
km1.paintAll(2,2)


end = time.time()

print(end - start)
  
