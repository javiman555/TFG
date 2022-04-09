import pywt
from src.objects.wave.ComplexWave import ComplexWave
import numpy as np
import copy

class Wavelete:
    
    def __init__(self):
       pass
   
    def simplificationComplexWave(self,complexWave:ComplexWave):
        dataY, noiseY = pywt.dwt(complexWave.y, 'db1') 
        output = copy.copy(complexWave)
        output.t = np.arange(0,1,1.0/len(dataY))
        output.y =dataY
        return output
