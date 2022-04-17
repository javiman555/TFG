import src.model.objects.graph.ClosenessGraph as cg
import src.model.modules.Wavelete as Wavelete
import src.model.modules.Fourier as Fourier
import src.model.objects.k_means.K_MeansGraph as K_MeansGraph

import networkx as nx
import itertools
import matplotlib.pyplot as plt
import numpy as np


class DiversificateAssets:
    
    def __init__(self,graph,realStockList):
        self.graph = graph
        self.realStockList = realStockList
    
    def getStocksKmeans(self,k):
        
        k_MeansGraph = K_MeansGraph.K_MeansGraph(k)
        k_MeansGraph.fitGraph(self.graph)
        
        self.clusters = self.adaptKmeansBoxes(self.graph,k_MeansGraph.boxes)
        
        
        selectedStocks = self.getSafeStocks(self.clusters)
        
        return selectedStocks    
    
    def getStocksGirvanNewman(self,k):
        
        
        self.clusters = self.clusterGirvanNewman(self.graph,k)
        
        
        
        selectedStocks = self.getSafeStocks(self.clusters)
        
        return selectedStocks
        
    def getSafeStocks(self,clusters):
        
        diverseStocks = []
        for cluster in clusters:
            diverseStocks.append(self.getMinVolatilityStock(cluster))
        return diverseStocks
        
    def getMinVolatilityStock(self,cluster):
        minVolatility = np.Inf
        for stockName in cluster:
            stock = self.getStockFromName(stockName,self.realStockList)
            currentVolatility = self.getVolatilityStandarDeviationProcess(stock.y)
            if currentVolatility < minVolatility:
                minVolatility = currentVolatility
                minVolatilityStock = stock
        return minVolatilityStock

    def getMaxVolatilityStock(self,cluster):
        maxVolatility = - np.Inf
        for stockName in cluster:
            stock = self.getStockFromName(stockName,self.realStockList)
            currentVolatility = self.getVolatilityStandarDeviationProcess(stock.y)
            if currentVolatility > maxVolatility:
                maxVolatility = currentVolatility
                maxVolatilityStock = stock
        return maxVolatilityStock

    def getStockFromName(self,name,realStockList):
        for stock in realStockList:
            if stock.dataName == name:
                return stock
            
    def getStockFromNameGraph(self,name,graph):
        stock = graph.nodes[name]['data']
        return stock
            
    def getVolatilityStandarDeviation(self,data,magnitude):
        data = data*magnitude
        return self.getVolatilityStandarDeviationProcess(data)
    
    def getVolatilityStandarDeviationProcess(self,data):
        counter = 0
        #Calculate mean
        for i in range(len(data)):
            counter +=data[i]
        mean = counter/len(data)
        #Calculate Deviation
        deviationSquared=0
        for i in range(len(data)):
            deviationSquared += (data[i] - mean)**2
        variance = deviationSquared/len(data)
        #If prices are randomly sampled from a normal distribution,
        #then about 68% of all data values will fall within one standard deviation
        # 95% in 2*standarDeviation
        standarDeviation = np.sqrt(variance)
        return standarDeviation
    
    
    def clusterGirvanNewman(self,graph,k):        
        comp = nx.algorithms.community.centrality.girvan_newman(graph)
        limited = itertools.takewhile(lambda c: len(c) <= k, comp)
        clusters = [(tuple(graph.nodes))]
        for communities in limited:
            clusters=(tuple(sorted(c) for c in communities))
        return clusters
    
    def adaptKmeansBoxes(self,graph,boxes):
        output = []
        
        for box in boxes.values():
            output.append(box)
        
        
        return output
    
    
    def drawClusters(self):

        color_map = []
        for node in self.graph:
            if node in self.clusters[0]:
                color_map.append('blue')
            elif node in self.clusters[1]:
                color_map.append('red')
            elif node in self.clusters[2]:
                color_map.append('pink')
            elif node in self.clusters[3]:
                color_map.append('orange')
            elif node in self.clusters[4]:
                color_map.append('yellow')
            elif node in self.clusters[5]:
                color_map.append('black')
            else:
                color_map.append('green')
        nx.draw(self.graph, node_color=color_map, with_labels=True)
        plt.show()