import numpy as np
import matplotlib.pyplot as plt
import random as rd
from src.model.objects.wave.ComplexWave import ComplexWave
import pandas as pd
import math

import os
from config.definitions import ROOT_DIR

class ComplexWaveDB(ComplexWave):
    
    def __init__(self,name,dataType,file, precision = 2):
        
        ComplexWave.__init__(self,precision)
        self.inicializeDB(name,dataType,file)
        self.processDatatoGraph()



    def inicializeDB(self,name,dataType,file):
        source = os.path.join(ROOT_DIR, 'resources', 'data',file)
        self.inicializeDBProccess(name,dataType,source)
        
    def inicializeDBProccess(self,name,dataType,source): 

        self.dataName = name+' ('+dataType+')'

        data=pd.read_csv(source,header=0)
    
        criteria = (data['ticker'] ==name)
        data=data[criteria]
        
        self.y =np.array(data[dataType].array)
        
        #Check to protect of empty rows of wave data
        for i in range(len(self.y)):
            if math.isnan(self.y[i]):
                if i != 0:
                    self.y[i] = self.y[i-1]
                else:
                    self.y[i] = self.y[i+1]
        
        # sampling interval
        self.date = [pd.to_datetime(date, format='%Y-%m-%d') for date in  data['Date']]

        ts = 1.0/(int(data[dataType].size))
        self.t = np.arange(0,1,ts)