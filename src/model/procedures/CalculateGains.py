import src.model.objects.graph.ClosenessGraph as cg
import src.model.objects.wave.ComplexWave as ComplexWave
import src.model.modules.Wavelete as Wavelete
import src.model.modules.Fourier as Fourier
import networkx as nx
import itertools
import matplotlib.pyplot as plt
import numpy as np

from typing import List,Any

class CalculateGains:
    
    def __init__(self):
        pass
    
    def calculateDiversificatedGains(self,listStocks : List[Any], money : float) -> List[float]:
        valueList = [0] * len(listStocks[0].y)
        for i in range(len(listStocks)):
            #This si the value that you have if you invest in each time point
            #valueList = np.add(valueList,self.calculateGainsFromStartToEnd(listStocks[i], money/len(listStocks)))
            #This is to get the value if you put all at the start
            valueList = np.add(valueList,self.calculateAccumulatedValue(listStocks[i], money/len(listStocks)))

        return valueList
    
    def calculateAccumulatedValue(self,stock : Any,money : float)->List[float]:
        
        valueList =[]
        for i in range(len(stock.y)):
            valueList.append(self.calculateGains(stock,money,0,i))
        return valueList
    
    def calculateGainsFromStartToEnd(self,stock : Any,money : float)->List[float]:
        
        valueList =[]
        for i in range(len(stock.y)):
            valueList.append(self.calculateGains(stock,money,i,len(stock.y)-1))
        return valueList
        
    def calculateGains(self,stock : Any, money : float, start : int, end : int)->float:
        buyPrice = stock.y[start]
        sellPrice = stock.y[end]
        
        value = (money/buyPrice)*sellPrice
        return value

