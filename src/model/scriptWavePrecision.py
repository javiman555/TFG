from src.model.objects.wave import ComplexWaveDB

import src.model.modules.YahooFinanceAPI as yf
import src.model.procedures.WavePrecision as WavePrecision
import src.model.modules.Fourier as Fourier
import src.model.modules.Wavelete as Wavelete
import src.model.procedures.ValueResults as ValueResults
import sys
import os
import numpy as np
from config.definitions import ROOT_DIR

yf1=yf.YahooFinanceAPI(debug=False)
valueResults=ValueResults.ValueResults()
dateList=[['2021-01-01','2021-01-31'],
          ['2021-01-01','2021-06-31'], 
          ['2021-01-01','2021-12-31'], 
          ['2020-01-01','2020-12-31'],
          ['2019-01-01','2019-12-31'], 
          ['2018-01-01','2018-12-31'],
          ['2017-01-01','2017-12-31'],
          ['2016-01-01','2016-12-31'] 
          ]
source = os.path.join(ROOT_DIR, 'resources', 'output','DataPrecision.txt')
f = open(source, 'w+')
sys.stdout = f
for i in range (len(dateList)):
    dateStart = dateList[i][0]
    dateEnd = dateList[i][1]
    print('Data form: '+dateStart+' to '+dateEnd)
    waves =[]
    for element in yf1.stocks:
        
        wave = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocks.csv',dateStart=dateStart,dateEnd=dateEnd,precision = 2)
        wave.normalice()
        waves.append(wave)
        
    for flag in range(1,4):
    
        
        realWaveList = waves
        wavePrecision = WavePrecision.WavePrecision(realWaveList,flag=flag)
        fourier = Fourier.Fourier()
        aproxWaveList = []
        for realWave in realWaveList:
            aproxWave = realWave
            aproxWave = fourier.DFT(realWave)
            aproxWaveList.append(aproxWave)
            
        precision = wavePrecision.compareData(aproxWaveList,flag=flag)
        if flag==1:
            print('----Default----')
        if flag==2:
            print('----Course----')
        if flag==3:
            print('----CourseValue----')
        print('Fourier:'+str(np.round(precision,2)))
        
        
        wavePrecision = WavePrecision.WavePrecision(realWaveList,flag=flag)
        realWaveList = waves
        wavelete = Wavelete.Wavelete()
        aproxWaveList = []
        for realWave in realWaveList:
            aproxWave = realWave
            aproxWave = wavelete.simplificationComplexWave(aproxWave)
            aproxWaveList.append(aproxWave)
            
        precision = wavePrecision.compareData(aproxWaveList,flag=flag)
        
        print('Wavelet:'+str(np.round(precision,2)))
        
    wavesGraph = valueResults.createWaveGraph(dateStart,dateEnd,yf1.stocks,debug=False)
    for flag in range(1,4):
    
        
        realWaveList = wavesGraph
        wavePrecision = WavePrecision.WavePrecision(realWaveList,flag=flag)
        fourier = Fourier.Fourier()
        aproxWaveList = []
        for realWave in realWaveList:
            aproxWave = realWave
            aproxWave = fourier.DFT(realWave)
            aproxWaveList.append(aproxWave)
            
        precision = wavePrecision.compareData(aproxWaveList,flag=flag)
        if flag==1:
            print('----DefaultGraph----')
        if flag==2:
            print('----CourseGraph----')
        if flag==3:
            print('----CourseValueGraph----')
        print('Fourier:'+str(np.round(precision,2)))
        
        
        wavePrecision = WavePrecision.WavePrecision(realWaveList,flag=flag)
        realWaveList = waves
        wavelete = Wavelete.Wavelete()
        aproxWaveList = []
        for realWave in realWaveList:
            aproxWave = realWave
            aproxWave = wavelete.simplificationComplexWave(aproxWave)
            aproxWaveList.append(aproxWave)
            
        precision = wavePrecision.compareData(aproxWaveList,flag=flag)
        
        print('Wavelet:'+str(np.round(precision,2)))
