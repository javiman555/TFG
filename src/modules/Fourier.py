import numpy as np
import copy
import src.objects.wave.ComplexWave as cw

#This class is useless
class Fourier:
    
    def __init__(self, precision = 4):
       self.precision = precision
        
    def DFT(self,realWave):
        """
        Function to calculate the 
        discrete Fourier Transform 
        of a 1D real-valued signal x
        """
        N = len(realWave.y)
        n = np.arange(N)
        k = n.reshape((N, 1))
        e = np.exp(-2j * np.pi * k * n / N)
    
        X = np.dot(e, realWave.y)
    
        self.FT = X
        self.processFTtoGraph()
        output = copy.copy(realWave)
        output.t = np.arange(0,1,1.0/len(self.FT))
        output.y =self.FT
        return output
    
    def processFTtoGraph(self):
        N = len(self.FT)
        n = np.arange(N)
        T = N/100
        freq = n/T 
        
        n_oneside = N//2
        # get the one side frequency
        f_oneside = freq[:n_oneside]
        
        self.FT[0]= 0
        self.toGraph=[]
        # normalize the amplitude
        X_oneside =self.FT[:n_oneside]/n_oneside
        self.FT=[]
        for i in range(len(X_oneside)):
            if round(abs(X_oneside[i]),self.precision) != 0:
                self.FT.append(round(abs(X_oneside[i]),self.precision))
                self.toGraph.append([f_oneside[i],round(abs(X_oneside[i]),self.precision)])
            else:
                self.FT.append(0)