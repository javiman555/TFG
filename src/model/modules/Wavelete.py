import copy
import pywt
from src.model.objects.wave.ComplexWave import ComplexWave
import numpy as np

class Wavelete:
    
    def __init__(self):
        pass
   
    def simplificationComplexWave(self,complexWave:ComplexWave):
        
        dataY, noiseY = pywt.dwt(complexWave.y, 'db1') 
        output = copy.copy(complexWave)
        output.t = np.arange(0,1,1.0/len(dataY))
        output.y =dataY
        output.date=[]

        for i in range(len(complexWave.date)):
            if i%2 == 0:
                output.date.append(complexWave.date[i])
        
        realMagnitude = output.magnitude
        output.normalice()
        output.magnitude = realMagnitude
        return output
    
    def simplificationComplexWaveList(self,complexWaveList):
        output =[]
        for wave in complexWaveList:
            output.append(self.simplificationComplexWave(wave))
        return output
    
