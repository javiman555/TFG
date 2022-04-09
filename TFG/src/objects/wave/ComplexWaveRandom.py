import numpy as np
import matplotlib.pyplot as plt
import random as rd
from src.objects.wave import SimpleWave
from src.objects.wave.ComplexWave import ComplexWave
import pandas as pd

class ComplexWaveRandom(ComplexWave):
    
    def __init__(self,precision,nwaves,maxamp,maxfre,points):
        
        ComplexWave.__init__(self,precision)
        self.inicializeRandom(nwaves,maxamp,maxfre,points)
        self.processDatatoGraph()

        
    def inicializeRandom(self,nwaves,maxamp,maxfre,points):
        self.dataName = "Random - " + str(nwaves)
        if points <= 0:
            raise ValueError('A simple wave needs a positive number of points')
        # sampling interval
        interval = 1.0/points
        self.t = np.arange(0,1,interval)
      
        self.y = 0
        waves=[]

        for i in range(nwaves):
            waves.append(SimpleWave.SimpleWave(rd.randint(1,maxamp),rd.randint(1,maxfre),points))
        for wave in waves:
            self.y = self.y + wave.y
