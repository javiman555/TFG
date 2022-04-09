import src.objects.wave.ComplexWaveDB as cw
import matplotlib.pyplot as plt
import numpy as np
import copy

class Stock:
    
    
    
    def __init__(self,stockName,file,precision):
        
        self.precision = precision
        
        self.open = cw.ComplexWaveDB(stockName,'Open',file,precision)
        self.close = cw.ComplexWaveDB(stockName,'Close',file,precision)
        self.high = cw.ComplexWaveDB(stockName,'High',file,precision)
        self.low = cw.ComplexWaveDB(stockName,'Low',file,precision)
        
        self.volatilityParkinson = self.getVolatilityParkinson()
        
        self.volatilityStandarDeviationOpen = self.getVolatilityStandarDeviation(self.open.y)
        self.volatilityStandarDeviationClose = self.getVolatilityStandarDeviation(self.close.y)
        self.volatilityStandarDeviationHigh = self.getVolatilityStandarDeviation(self.high.y)
        self.volatilityStandarDeviationLow = self.getVolatilityStandarDeviation(self.low.y)
        [self.volatilityStandarDeviationHighLow1,self.volatilityStandarDeviationHighLow2] = self.getVolatilityStandarDeviationHighLow(self.high.y,self.low.y)
        
        self.stockName = stockName

    def getVolatilityParkinson(self):
        output = 0
        for i in range(len(self.open.y)):
            output +=(0.5*np.log(self.high.y[i]/self.low.y[i])**2)-(2*np.log(2)-1)*(np.log(self.close.y[i]/self.open.y[i])**2)
        return output
    
    def drawHighLow(self):
        self.high.drawProcess(self.high.y,'g')
        self.low.drawProcess(self.low.y,'r')
        plt.ylabel('Data - '+self.stockName)
        plt.xlabel('Time (t) / Frecuencia (?)')
        plt.show()
    
    def getVolatilityStandarDeviation(self,data):
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
        standarDeviation = np.sqrt(variance)
        return standarDeviation
    
    def getVolatilityStandarDeviationHighLow(self,high,low):
        counter = 0
        #Calculate mean
        for i in range(len(high)):
            counter +=high[i]+low[i]
        mean = counter/(2*len(high))
        #Calculate Deviation
        deviationSquared1=0
        deviationSquared2=0
        for i in range(len(high)):
            if (high[i]+low[i])/2 <= mean:
                deviationSquared1 += (high[i] - mean)**2
                deviationSquared2 += (low[i] - mean)**2  
            else:
                deviationSquared1 += (low[i] - mean)**2  
                deviationSquared2 += (high[i] - mean)**2
        variance1 = deviationSquared1/len(high)
        variance2 = deviationSquared2/len(high)

        standarDeviation1 = np.sqrt(variance1)
        standarDeviation2 = np.sqrt(variance2)
        return [standarDeviation1,standarDeviation2]