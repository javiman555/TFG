import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from src.objects.k_means.K_Means import K_Means
import src.objects.wave.ComplexWave as ComplexWave
import networkx as nx
import copy

class K_MeansVariation(K_Means):
    
    def __init__(self, k, precision = 0.0001):
        K_Means.__init__(self,k, precision)

    def fitByCourse(self,listComplexWave):
        listCourseWave=[None]*len(listComplexWave)
        for i in range(len(listComplexWave)):
            listCourseWave[i]=self.changeWaveToCourse(listComplexWave[i])
        courseBoxes=self.fitDefaultProcess(listCourseWave)
        self.boxes=self.returnToDefaultWave(listComplexWave,courseBoxes)
    
    def fitByCourseValue(self,listComplexWave):
        listCourseWave=[None]*len(listComplexWave)
        for i in range(len(listComplexWave)):
            listCourseWave[i]=self.changeWaveToCourseValue(listComplexWave[i])
        courseBoxes=self.fitDefaultProcess(listCourseWave)
        self.boxes=self.returnToDefaultWave(listComplexWave,courseBoxes)
    
    def fitDefaultGraph(self,listGraph):
        listComplexWave = self.changeGraphToWave(listGraph)
        orderedListComplexWave = self.order(listComplexWave)
        return K_Means.fitDefault(self,orderedListComplexWave)
    
    def changeWaveToCourseValue(self,wave):
        course =copy.deepcopy(wave)
        for i in range(len(wave.y)-1):
            if i == len(wave.y)-1:
                course.y[i]=0
            else:
                course.y[i]= wave.y[i+1] - wave.y[i]
        return course    
    
    def changeWaveToCourse(self,wave):
        course =copy.deepcopy(wave)
        for i in range(len(wave.y)-1):
            if i == len(wave.y)-1:
                course.y[i]=0.5
            elif wave.y[i] > wave.y[i+1]:
                course.y[i]=0
            elif wave.y[i] == wave.y[i+1]:
                course.y[i]=0.5
            elif wave.y[i] < wave.y[i+1]:
                course.y[i]=1
        return course
    
    def returnToDefaultWave(self,listComplexWave,courseBoxes):
        newBoxes={}
        for key, value in courseBoxes.items():
            newBoxesValue=[None]*len(value)
            for i in range(len(value)):
                newBoxesValue[i]= self.findWaveByName(listComplexWave,value[i].dataName)        
            newBoxes[key] = newBoxesValue
        return newBoxes

    def findWaveByName(self,listComplexWave,name):
        for wave in listComplexWave:
            if wave.dataName == name:
                return wave
    
    def fitNumberOfGains(self,listComplexWave):
        
        self.centroids = {}

		#initialize the centroids, the first distinct 'k' elements in the dataset will be our initial centroids 
        i = 0
        j = 0
        while i < self.k :
            if j >= len(listComplexWave):
                nextCentroid = max(self.centroids.values()) + 1
            else :
                nextCentroid = self.positionNumberOfGains(listComplexWave[j])
            
            j = j + 1
            if (not nextCentroid in self.centroids.values()):
                self.centroids[i] =nextCentroid
                i = i + 1

		#begin iterations
        while True:
            self.boxes = {}
            for i in range(self.k):
                self.boxes[i] = []

			#find the distance between the point and cluster; choose the nearest centroid
            for wave in listComplexWave:
                
                distances = self.calculateDistancesNumberOfGains(wave)

                classification = distances.index(min(distances))
                self.boxes[classification].append(wave)
            previousCentroids = dict(self.centroids)

			#average the cluster datapoints to re-calculate the centroids
            isOptimal =self.averageClusterNumberOfGains(previousCentroids)
			#break out of the main loop if the results are optimal, ie. the centroids don't change their positions much(more than our tolerance)
            if isOptimal:
                break
            
    #average the cluster datapoints to re-calculate the centroids and returs if we finish the proccess
    def averageClusterNumberOfGains(self,previousCentroids):
        for classification in self.boxes:
                
            self.centroids[classification]=[] 
            for i in range(len(self.boxes[classification])):
                self.centroids[classification].append(self.positionNumberOfGains(self.boxes[classification][i]))
                    
            self.centroids[classification] = np.average(self.centroids[classification], axis = 0)


        for centroid in self.centroids:

            original_centroid = previousCentroids[centroid]
            curr = self.centroids[centroid]
            change = np.nansum(abs(((curr - original_centroid)/original_centroid )* 100.0))
                
            if change > self.precision:
                return False
        return True
    
    #Defines the 1 dimensional position of the wave
    def positionNumberOfGains(self,complexWave):
        counter = 0
        for i in range(len(complexWave.y)-1):
            if complexWave.y[i+1] > complexWave.y[i]:
                counter = counter + 1
        return counter
    
    #Uses the norm of n dimensions to get distance
    def calculateDistancesNumberOfGains(self, wave):
        output = []
        for centroid in self.centroids:
            output.append(np.linalg.norm(self.positionNumberOfGains(wave) - self.centroids[centroid]))
        return output
    
    def changeGraphToWave(self,listGraph):
        
        listComplexWave = []
        
        for graph in listGraph:
            newComplexWave = ComplexWave.ComplexWave(2)
            newComplexWave.dataName = graph.dataName
            betweenness = nx.betweenness_centrality(graph, k=None, normalized=True, weight=None, endpoints=False, seed=None)
            newComplexWave.y = [*betweenness.values()]
            listComplexWave.append(newComplexWave)
        return listComplexWave
    
    def order (self,listComplexWave):
        orderedListComplexWave = []
        for wave in listComplexWave:
            wave.y.sort(reverse=True)
            orderedListComplexWave.append(wave)
        return orderedListComplexWave