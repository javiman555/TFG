import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import src.objects.k_means.K_Means as K_Means
import src.objects.graph.Graph as Graph
import src.objects.k_means.K_MeansVariation as K_MeansVariation


class ClosenessGraph(Graph.Graph):
    
    
    def __init__(self):
        
        Graph.Graph.__init__(self);
        
    def genericDistance(self,listComplexWave):
        self.dataDetails = listComplexWave

        self.startGraph(listComplexWave)
        for startWave in listComplexWave:
            for endWave in listComplexWave:
                if startWave.dataName != endWave.dataName:
                    if self.has_edge(startWave.dataName, endWave.dataName):
                        pass
                    else:
                        self.add_edge(startWave.dataName, endWave.dataName, weight= np.linalg.norm(startWave.y-endWave.y))
        
    def distanceCloseness(self,listComplexWave,kmeansType,kmeans):
       
        
        self.dataDetails = listComplexWave
        self.maxWeight = 0
        self.startGraph(listComplexWave)
        for i in range(len(listComplexWave)//3,len(listComplexWave)//3 + 1):
            kmeans.k=i+1
            mutalbeListComplexWave = listComplexWave.copy()
            for complexWave in listComplexWave:
                self.maxWeight += 1
                kmeansType(mutalbeListComplexWave)

                self.saveWaveCloseness(kmeans)
                mutalbeListComplexWave.pop(0)
                mutalbeListComplexWave.append(complexWave)
        self.calibrateWeightMax()
        #self.calibrateWeight()
        
        
    def kmeansLoop(self,listComplexWave,precision):
        self.dataDetails = listComplexWave
        
        self.startGraph(listComplexWave)
        kmeans = K_MeansVariation.K_MeansVariation(0)
        for i in range(len(listComplexWave)//precision,len(listComplexWave)-len(listComplexWave)//precision):
            kmeans.k=i+1
            mutalbeListComplexWave = listComplexWave.copy()
            for complexWave in listComplexWave:
                kmeans.fitDefault(mutalbeListComplexWave)
                self.saveWaveCloseness(kmeans)
                mutalbeListComplexWave.pop(0)
                mutalbeListComplexWave.append(complexWave)
        self.calibrateWeightMax()
        #self.calibrateWeight()

    def calibrateWeight(self):
            
        for u,v,d in self.edges(data = True):
            d['weight']= 1/d['weight']

    def calibrateWeightMax(self):
        for u,v,d in self.edges(data = True):
            d['weight']= self.maxWeight-d['weight']

    def startGraph(self,listComplexWave):
        self.remove_edges_from(self.edges())
        for wave in listComplexWave:
            self.add_node(wave.dataName, data = wave)

    def saveWaveCloseness(self,kmeans):
        for box in kmeans.boxes.values():
            for startWave in box:
                for endWave in box:
                    if startWave != endWave:
                        if self.has_edge(startWave.dataName, endWave.dataName):
                             self[startWave.dataName][endWave.dataName]['weight'] += 0.5
                        else:
                            self.add_edge(startWave.dataName, endWave.dataName, weight=0.5)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        