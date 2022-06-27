from src.controller.plot import AltairPlot
from io import StringIO
from src.model.objects.wave import ComplexWaveDB
import src.model.modules.YahooFinanceAPI as yf
import src.model.procedures.ValueResults as ValueResults

import numpy as np


class ResultController:
    
    def __init__(self):
        pass

    def getRecomendation(self,resultList):
        recomendation =[]
        minVol=np.inf
        current=""
        for result in resultList:
            vol = self.getVolatilityStandarDeviationProcess(result.y)
            if vol < minVol:
                minVol = vol
                current = result.dataName
                recomendation = result.components
                
        output = "From "+current.replace('Aprox', '') +" "+ str(recomendation)
        
        return output
    
    def getVolatilityStandarDeviationProcess(self,data):
        counter = 0
        #Calculate mean
        for i in range(len(data)):
            counter +=data[i]
        mean = counter/len(data)
        #Calculate Deviation
        deviationSquared=0
        for i in range(len(data)):
            deviationSquared += (data[i] - mean)**2
        variance = deviationSquared/len(data)
        #If prices are randomly sampled from a normal distribution,
        #then about 68% of all data values will fall within one standard deviation
        # 95% in 2*standarDeviation
        standarDeviation = np.sqrt(variance)*(256/len(data))
        return standarDeviation
            