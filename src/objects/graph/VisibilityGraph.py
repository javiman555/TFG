import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import src.objects.graph.Graph as Graph


class VisibilityGraph(Graph.Graph):
    
    
    def __init__(self,points,data):
        
        Graph.Graph.__init__(self);
        self.dataName = data
        
        for pointIni in points:
            
            self.add_node(tuple(pointIni))
            
            for pointEnd in points:
                
                if self.isVisible(points,pointIni,pointEnd):
                    
                    self.add_edge(tuple(pointIni), tuple(pointEnd))



    def isVisible(self,points,pointIni,pointEnd):
        
        if pointIni == pointEnd:
            return False
        
        for pointAux in points:
            
            if (pointAux[0] > pointIni[0] and pointAux[0] < pointEnd[0] or pointAux[0] < pointIni[0] and pointAux[0] > pointEnd[0]):
                
                highpoint = pointEnd[1] + (pointIni[1] - pointEnd[1])*(pointEnd[0] - pointAux[0])/(pointEnd[0] - pointIni[0])
                lowpoint = pointAux[1] 
                
                if ( lowpoint >= highpoint):
                    return False
              
        return True
        
        
    def drawVisibilityByDegree(self):
        
        degree=self.maxDegree()
        minVal=float("inf")
        for node in self.nodes():
            if node[1] < minVal:
                minVal=node[1]
        
        for node in self.nodes():
            
            if (self.degree(node) == degree):
                plt.plot([node[0],node[0]],[minVal,node[1]],"k",zorder=10)
            elif (self.degree(node) < degree and self.degree(node) >= (degree*0.75)):
                plt.plot([node[0],node[0]],[minVal,node[1]],"r",zorder=8)
            elif (self.degree(node) < degree*0.75 and self.degree(node) >= (degree*0.50)):
                plt.plot([node[0],node[0]],[minVal,node[1]],color='orange',zorder=6)
            elif (self.degree(node) < degree*0.50 and self.degree(node) >= (degree*0.25)):
                plt.plot([node[0],node[0]],[minVal,node[1]],"y",zorder=4)
            elif (self.degree(node) < degree*0.25 ):
                plt.plot([node[0],node[0]],[minVal,node[1]],color="#34F907",zorder=2)
        
        for edge in self.edges():
            
            if (self.degree(edge[0]) == degree)or(self.degree(edge[1]) == degree):
                plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]],"-",linewidth=0.25,color='black')
            elif (self.degree(edge[0]) < degree and self.degree(edge[0]) >= (degree*0.75)):
                plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]],"-",linewidth=0.25,color='red')
            elif (self.degree(edge[0]) < degree*0.75 and self.degree(edge[0]) >= (degree*0.50)):
                plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]],"-",linewidth=0.25,color='orange')
            elif (self.degree(edge[0]) < degree*0.50 and self.degree(edge[0]) >= (degree*0.25)):
                plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]],"-",linewidth=0.25,color='yellow')
            elif (self.degree(edge[0]) < degree*0.25 ):
                plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]],"-",linewidth=0.25,color='#34F907')
        
        plt.ylabel('Data - '+self.dataName)
        plt.xlabel('Time (t) / Frecuencia (?)')
        plt.show()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        