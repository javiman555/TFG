import numpy as np
import matplotlib.pyplot as plt
import copy

class ComplexWave:
    
    
    
    def __init__(self,precision = 2):
        self.y = 0
        self.precision = precision
        self.toGraph = []
        self.dataName = ""
        self.components=[]
        self.magnitude = 1
    
    def __lt__(self, other):
        if isinstance(other, ComplexWave):
            value = 0
            otherValue = 0
            for i in range(len(self.y)):
                value += self.y[i]
                otherValue += other.y[i]
            return value < otherValue
        else:
            return False
        
        return self.dataName == other.dataName and self.y == other.y
    
    def  __add__(self, number):
        output = copy.deepcopy(self)
        for i in range(len(self.y)):
            output.y[i] = self.y[i]+number
        return output
        
        
    def draw(self,y):
        plt.figure(figsize = (8, 6))
        self.drawProcess(y,'k')
        plt.title('Wave: '+self.dataName)
        plt.ylabel('Data - '+self.dataName)
        plt.xlabel('Time (t)')
        plt.show()
        
        
    def drawProcess(self,y,color):
        sr = len(y)
        # sampling interval
        ts = 1.0/sr
        x = np.arange(0,1,ts)
        if len(x) != len(y):
            x = np.delete(x,0)
            
        plt.plot(x,y,color)
        
    def normalice(self):
        self.magnitude = max(self.y)
        ratio = 1/self.magnitude
        self.y = self.y * ratio
        
    
    def processDatatoGraph(self):
        
        self.toGraph=[]
        for i in range(len(self.y)):
            self.y[i]=round(self.y[i],15)
            self.t[i]=round(self.t[i],15)
            self.toGraph.append([self.t[i],self.y[i]])
            