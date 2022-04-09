import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import src.objects.k_means.K_Means as K_Means


class Graph(nx.Graph):
    
    
    def __init__(self):
        
        nx.Graph.__init__(self);

    def maxDegree(self):
        
        degree=0
        
        for node in self.nodes():
            
            if self.degree(node) >= degree:
                
                degree=self.degree(node)
                
        return degree

    
    def drawGraphByDegree(self,label=True):
        
        degree=self.maxDegree()
        color_map = []

        
        for node in self.nodes():
            
            if (self.degree(node) == degree):
                color_map.append('black')
            elif (self.degree(node) < degree and self.degree(node) >= (degree*0.75)):
                color_map.append('red')
            elif (self.degree(node) < degree*0.75 and self.degree(node) >= (degree*0.50)):
                color_map.append('orange')
            elif (self.degree(node) < degree*0.50 and self.degree(node) >= (degree*0.25)):
                color_map.append('yellow')
            elif (self.degree(node) < degree*0.25 ):
                color_map.append('#34F907')
        
        nx.draw(self, node_color=color_map, with_labels=label)
        plt.show()
        
        
        
        
    def drawGraphByBetweenness(self,label=True):
        
        betweenness = nx.betweenness_centrality(self, k=None, normalized=True, weight='weight', endpoints=False, seed=None)
        degree=max(betweenness.values())
        color_map = []
 
        
        for node in betweenness:
            
            if (betweenness[node] == degree):
                color_map.append('black')
            elif (betweenness[node] < degree and betweenness[node] >= (degree*0.75)):
                color_map.append('red')
            elif (betweenness[node] < degree*0.75 and betweenness[node] >= (degree*0.50)):
                color_map.append('orange')
            elif (betweenness[node] < degree*0.50 and betweenness[node] >= (degree*0.25)):
                color_map.append('yellow')
            elif (betweenness[node] < degree*0.25 ):
                color_map.append('#34F907')

        nx.draw(self, node_color=color_map, with_labels=label)
        plt.show()
              
    def drawGraphByDegreeFancy(self,label=False):
        
        pos = nx.spring_layout(self)
        degree=self.maxDegree()
        Gaux1=nx.Graph()
        Gaux2=nx.Graph()
        Gaux3=nx.Graph()
        Gaux4=nx.Graph()
        Gaux5=nx.Graph()
        
        for node in self.nodes():
            
            if (self.degree(node) == degree):
                Gaux1.add_node(node)
            elif (self.degree(node) < degree and self.degree(node) >= (degree*0.75)):
                Gaux2.add_node(node)
            elif (self.degree(node) < degree*0.75 and self.degree(node) >= (degree*0.50)):
                Gaux3.add_node(node)
            elif (self.degree(node) < degree*0.50 and self.degree(node) >= (degree*0.25)):
                Gaux4.add_node(node)
            elif (self.degree(node) < degree*0.25 ):
                Gaux5.add_node(node)
        
        nx.draw_networkx_nodes(self, pos,Gaux5,node_color="#34F907",node_size=5000/len(self.nodes()),label=True)
        nx.draw_networkx_nodes(self, pos,Gaux4,node_color="yellow",node_size=10000/len(self.nodes()),label=True)
        nx.draw_networkx_nodes(self, pos,Gaux3,node_color="orange",node_size=15000/len(self.nodes()),label=True)
        nx.draw_networkx_nodes(self, pos,Gaux2,node_color="red",node_size=20000/len(self.nodes()),label=True)
        nx.draw_networkx_nodes(self, pos,Gaux1,node_color="black",node_size=25000/len(self.nodes()),label=True)

        nx.draw_networkx_edges(self, pos,width=min(1,100/max(len(self.edges()),1)),label='weight')
        plt.show()
        
        
        
    def drawGraphByBetweennessFancy(self):
        betweenness = nx.betweenness_centrality(self, k=None, normalized=True, weight='weight', endpoints=False, seed=None)
        pos = nx.spring_layout(self)
        degree=max(betweenness.values())

        Gaux1=nx.Graph()
        Gaux2=nx.Graph()
        Gaux3=nx.Graph()
        Gaux4=nx.Graph()
        Gaux5=nx.Graph()
        
        
        for node in betweenness:
            
            if (betweenness[node] == degree):
                Gaux1.add_node(node)
            elif (betweenness[node] < degree and betweenness[node] >= (degree*0.75)):
                Gaux2.add_node(node)
            elif (betweenness[node] < degree*0.75 and betweenness[node] >= (degree*0.50)):
                Gaux3.add_node(node)
            elif (betweenness[node] < degree*0.50 and betweenness[node] >= (degree*0.25)):
                Gaux4.add_node(node)
            elif (betweenness[node] < degree*0.25 ):
                Gaux5.add_node(node)
        
        nx.draw_networkx_nodes(self, pos,Gaux5,node_color="#34F907",node_size=5000/len(self.nodes()),label=True)
        nx.draw_networkx_nodes(self, pos,Gaux4,node_color="yellow",node_size=10000/len(self.nodes()),label=True)
        nx.draw_networkx_nodes(self, pos,Gaux3,node_color="orange",node_size=15000/len(self.nodes()),label=True)
        nx.draw_networkx_nodes(self, pos,Gaux2,node_color="red",node_size=20000/len(self.nodes()),label=True)
        nx.draw_networkx_nodes(self, pos,Gaux1,node_color="black",node_size=25000/len(self.nodes()),label=True)

        nx.draw_networkx_edges(self, pos,width=min(1,100/max(len(self.edges()),1)),label='weight')
        plt.show()

        
        
        
        
        
        
        
        
        
        
        
        