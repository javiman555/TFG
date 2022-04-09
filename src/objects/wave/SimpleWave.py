import numpy as np
import matplotlib.pyplot as plt
import random as rd

class SimpleWave:
    
  def __init__(self,amplitude,frecuency, points):
      if points <= 0:
          raise ValueError('A simple wave needs a positive number of points')
      interval = 1.0/points
      self.t = np.arange(0,1,interval)
      self.y = amplitude*np.sin((2*np.pi*frecuency*self.t)+rd.randint(-amplitude,frecuency))

  def paint(self):
      plt.figure(figsize = (8, 6))
      plt.plot(self.t, self.y, 'b')
      plt.ylabel('Amplitude')
      plt.xlabel('Time (t)')
      plt.show()
      
    

