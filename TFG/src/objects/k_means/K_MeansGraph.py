import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import networkx as nx
import random

class K_MeansGraph:

    def __init__(self, k, maxLoop = 50):
        self.k = k
        self.maxLoop = maxLoop
        self.boxes = {}
        
    def fitGraph(self,graph):
        self.boxes = self.fitGraphProcess(graph)
    
    def fitGraphProcess(self,graph):
        
		#initialize the centroids, the first distinct 'k' elements in the dataset will be our initial centroids 
        centroids = self.initializeClustersFirstElements(graph,self.k)
        #centroids = self.initializeClustersRandom(graph,self.k)
        
        nLoops = 0
		#begin iterations
        while True:
            boxes = {}
            #Now when we inicialize the boxes we can add the centroids to the cluster
            #that is because this is not really kmeas but kmedoids
            centroidNodes = []
            for i in range(self.k):
                boxes[i] = []
                boxes[i].append(centroids[i])
                centroidNodes.append(centroids[i])
            nonCentroidNodes = graph.nodes()-centroidNodes
            
			#find the distance between the point and cluster; choose the nearest centroid
            for node in nonCentroidNodes:
                
                distances = self.calculateDistancesDijkstra(graph,node,centroids)

                classification = distances.index(min(distances))
                boxes[classification].append(node)
            previousCentroids = dict(centroids)

			#As a graph we can't average the cluster datapoints to re-calculate the centroids
            #We need to get allways a node as centroid
            
            #centroids = self.newCentroids(centroids,boxes,graph)
            centroids = self.newCentroidsSubgraph(centroids,boxes,graph)

            isOptimal =self.isOptimal(previousCentroids,centroids,graph)
			#break out of the main loop if the results are optimal, ie. the centroids don't change their positions much(more than our tolerance)
            if (isOptimal or nLoops > self.maxLoop) :
                return boxes
            nLoops += 1
        
        
	#initialize the centroids, the first 'k' elements in the dataset will be our initial centroids 
    def initializeClustersFirstElements(self, graph,k):
        output = {}
        j = 0
        for i in graph.nodes():
            if j < k:
                output[j] = i
                j +=1
            else:
                break
        return output
    
	#initialize the centroids, the first 'k' elements in the dataset will be our initial centroids 
    def initializeClustersRandom(self, graph,k):
        output = {}
        j = 0
        randomNodes = random.sample(graph.nodes(), k)
        for i in randomNodes:
            if j < k:
                output[j] = i
                j +=1
            else:
                break
    
        return output
    
    def newCentroidsSubgraph(self,centroids,boxes,graph):
        newCentroids = {}
        sub = []
        i = 0
        for classification in boxes.values():
            subgraph = graph.subgraph(classification)
            sub.append(subgraph)
            betweenness = nx.betweenness_centrality(subgraph, k=None, normalized=True, weight=None, endpoints=False, seed=None)
            
            maxBetweenness = 0
            currentCentroid = centroids[i]
            for node in betweenness:
                if maxBetweenness < betweenness[node]:
                    maxBetweenness = betweenness[node]
                    currentCentroid = node
            
            newCentroids[i] = currentCentroid
            i += 1

            
        return newCentroids
    def newCentroids (self,centroids,boxes,graph):
        newCentroids = {}
        sub = []
        i = 0
        for classification in boxes.values():
            betweenness = nx.betweenness_centrality(graph, k=None, normalized=True, weight=None, endpoints=False, seed=None)
            maxBetweenness = 0
            currentCentroid = classification[0]
            for node in classification:
                if maxBetweenness < betweenness[node]:
                    maxBetweenness = betweenness[node]
                    currentCentroid = node
            newCentroids[i] = currentCentroid
            i += 1

            
        return newCentroids
    #We say the proccess isOptimal if the centroids don't change
    def isOptimal(self,previousCentroids,centroids,graph):
        return previousCentroids == centroids
    
    #Uses the Dijkstra Algorithm k times
    def calculateDistancesDijkstra(self, graph, node, centroids):
        output = []
        for centroidNode in centroids.values():
            output.append(self.dijkstra(graph,node,centroidNode))
        return output
    
    #For now just calls the dijkstra of networkx and handles disconected graphs
    def dijkstra (self, graph, start, end):
        aux = (graph.subgraph(c) for c in nx.connected_components(graph))
        connectedComponents = list(aux)
        for subgraph in connectedComponents:
            if start in subgraph and end in subgraph:
                return nx.dijkstra_path_length(graph, source=start, target=end)
 
        return np.inf
    