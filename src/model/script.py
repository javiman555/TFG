import time
from src.controller.execution import ExecutionController
import random
import sys
import os
from config.definitions import ROOT_DIR
import numpy as np

def getVolatilityStandarDeviationProcess(data):
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

random.seed(2)



tickerList = ['SAB.MC', 'SAN.MC', 'AENA.MC', 'ELE.MC', 'NTGY.MC', 'PHM.MC', 'ENG.MC', 'GRF.MC', 'CABK.MC', 'ITX.MC', 'BKT.MC', 'VIS.MC', 'REE.MC', 'CLNX.MC', 'BBVA.MC', 'MRL.MC', 'FER.MC', 'MTS.MC', 'MAP.MC', 'COL.MC', 'ACX.MC', 'ACS.MC', 'IBE.MC', 'FDR.MC', 'TEF.MC', 'ANA.MC', 'IAG.MC', 'AMS.MC', 'SGRE.MC', 'MEL.MC', 'ALM.MC', 'CIE.MC', 'IDR.MC', 'ROVI.MC']
minimo = 4
maximo = 12
           
dateList=[#['2021-01-01','2021-01-31'],
          #['2021-01-01','2021-06-31'], #12 min
          #['2021-01-01','2021-12-31'], #33 min 
          #['2020-01-01','2020-12-31'], #45 min 
          #['2019-01-01','2019-12-31'], #40 min 
          #['2018-01-01','2018-12-31'], #40 min 
          #['2017-01-01','2017-12-31'], #40 min
          #['2016-01-01','2016-12-31'], #40 min
          #['2018-01-01','2021-12-31'], #+8 h
          ]
money = 1000

for i in range (len(dateList)):
    dateStart = dateList[i][0]
    dateEnd = dateList[i][1]
    start = time.time()
    source = os.path.join(ROOT_DIR, 'resources', 'output','Data '+dateStart+' --- '+dateEnd+'.txt')
    f = open(source, 'w+')
    sys.stdout = f
    
    
    executeController = ExecutionController.ExecutionController()
    
    
    
    
    results = {}
    resultsA = {}
    for k in range(minimo,maximo+1):
    
        [resultA,result] = executeController.executeSlow(tickerList,dateStart,dateEnd,money,k)
        results[k] = result
        resultsA[k] = resultA
        
        
    f.close()
    source = os.path.join(ROOT_DIR, 'resources', 'output','Average '+dateStart+' --- '+dateEnd+'.txt')
    f=open(source, 'w+')
    sys.stdout = f
    for i in range(len(results[minimo])):
        vol = 0
        val = 0
        
        volA = 0
        valA = 0
        for k,result in results.items():
            vol = vol + getVolatilityStandarDeviationProcess(results[k][i].y)
            val = val + results[k][i].y[len(results[k][i].y)-1]
            
            volA = volA + getVolatilityStandarDeviationProcess(resultsA[k][i].y)
            valA = valA + resultsA[k][i].y[len(resultsA[k][i].y)-1]
        vol = vol/len(results)
        val = val/len(results)
        volA = volA/len(results)
        valA = valA/len(results)
        
        print('----------------Average de '+results[k][i].dataName+' entre '+str(minimo)+' y '+str(maximo))
        print('Stocks: '+str(results[k][i].components))
        print('Volatilidad input: '+str(np.round(volA,2)))
        print('Valor input: '+str(np.round(valA,2)))
        print('Volatilidad Actual: '+str(np.round(vol,2)))
        print('Valor Actual: '+str(np.round(val,2)))
    
    
    end = time.time()
    print('Tiempo: '+str(end - start)+'s')
    #f.close()
        