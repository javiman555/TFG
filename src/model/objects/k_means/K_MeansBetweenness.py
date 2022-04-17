import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from src.model.objects.k_means.K_Means import K_Means
import objects.wave.ComplexWave as ComplexWave
import networkx as nx

#Obsolete
class K_MeansBetweenness(K_Means):
    
    def __init__(self, k, precision = 0.0001):
        K_Means.__init__(self,k, precision)

    #K-means con distancia generica sobre el arrary de Betweenness de los nodos del grafo 
    def fitDefault(self,listGraph):
        
        listComplexWave = self.changeGraphToWave(listGraph)
        return K_Means.fitDefault(listComplexWave)

    #K-means con distancia generica sobre el arrary ordenado de mayor a menor de Betweenness de los nodos del grafo 
    def fitDefaultOrdered(self,listGraph):
        listComplexWave = self.changeGraphToWave(listGraph)
        orderedListComplexWave = self.order(listComplexWave)
        return K_Means.fitDefault(self,orderedListComplexWave)