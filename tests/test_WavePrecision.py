import unittest as utest
from src.objects.wave import ComplexWaveDB

import src.modules.YahooFinanceAPI as yf
import src.procedures.WavePrecision as WavePrecision
import src.modules.Fourier as Fourier
import src.modules.Wavelete as Wavelete

class TestWavePrecision(utest.TestCase):
     
    @classmethod
    def setUpClass(cls):
        yf1=yf.YahooFinanceAPI(debug=True)
        cls.waves =[]
        
        for element in yf1.stocks:
            
            wave = ComplexWaveDB.ComplexWaveDB(element,'Open','DataStocksTest.csv')
            wave.normalice()
            cls.waves.append(wave)        
        
        
       
    def test_compare_same_wave(self):
        realWaveList = self.__class__.waves
        wavePrecision = WavePrecision.WavePrecision(realWaveList)
        aproxWaveList = []
        for realWave in realWaveList:
            aproxWave = realWave
            aproxWaveList.append(aproxWave)
        precision = wavePrecision.compareData(aproxWaveList)
        self.assertEqual(precision, 100)

    def test_compare_wave_1_wavelete(self):
        realWaveList = self.__class__.waves
        wavePrecision = WavePrecision.WavePrecision(realWaveList)
        wavelete = Wavelete.Wavelete()
        aproxWaveList = []
        for realWave in realWaveList:
            aproxWave = wavelete.simplificationComplexWave(realWave)
            aproxWaveList.append(aproxWave)
            
        precision = wavePrecision.compareData(aproxWaveList)
        self.assertAlmostEqual(precision, 97.44, 2)
        
    def test_compare_wave_2_wavelete(self):
        realWaveList = self.__class__.waves
        wavePrecision = WavePrecision.WavePrecision(realWaveList)
        wavelete = Wavelete.Wavelete()
        aproxWaveList = []
        for realWave in realWaveList:
            aproxWave = realWave
            aproxWave = wavelete.simplificationComplexWave(aproxWave)#96.36 / 99.8 / 94.35
            aproxWave = wavelete.simplificationComplexWave(aproxWave)#83.13 /x/
            aproxWaveList.append(aproxWave)
            
        precision = wavePrecision.compareData(aproxWaveList)
        self.assertAlmostEqual(precision, 96.65, 2)

    def test_compare_wave_3_wavelete(self):
        realWaveList = self.__class__.waves
        wavePrecision = WavePrecision.WavePrecision(realWaveList)
        wavelete = Wavelete.Wavelete()
        aproxWaveList = []
        for realWave in realWaveList:
            aproxWave = realWave
            aproxWave = wavelete.simplificationComplexWave(aproxWave)#96.36 / 99.8 / 94.35
            aproxWave = wavelete.simplificationComplexWave(aproxWave)#83.13 /x/
            aproxWave = wavelete.simplificationComplexWave(aproxWave)#79.28 /x/ 76
            aproxWaveList.append(aproxWave)
            
        precision = wavePrecision.compareData(aproxWaveList)
        self.assertAlmostEqual(precision, 93.11, 2)

    def test_compare_wave_4_wavelete(self):
        realWaveList = self.__class__.waves
        wavePrecision = WavePrecision.WavePrecision(realWaveList)
        wavelete = Wavelete.Wavelete()
        aproxWaveList = []
        for realWave in realWaveList:
            aproxWave = realWave
            aproxWave = wavelete.simplificationComplexWave(aproxWave)#96.36 / 99.8 / 94.35
            aproxWave = wavelete.simplificationComplexWave(aproxWave)#83.13 /x/
            aproxWave = wavelete.simplificationComplexWave(aproxWave)#79.28 /x/ 76
            aproxWave = wavelete.simplificationComplexWave(aproxWave)#66.85 / 94.292 / 55.72
            aproxWaveList.append(aproxWave)
            
        precision = wavePrecision.compareData(aproxWaveList)
        self.assertAlmostEqual(precision, 87.40, 2)

    def test_compare_wave_fourier(self):
        realWaveList = self.__class__.waves
        wavePrecision = WavePrecision.WavePrecision(realWaveList)
        fourier = Fourier.Fourier()
        aproxWaveList = []
        for realWave in realWaveList:
            aproxWave = realWave
            aproxWave = fourier.DFT(realWave)
            aproxWaveList.append(aproxWave)
            
        precision = wavePrecision.compareData(aproxWaveList)
        self.assertAlmostEqual(precision, 48.81, 2)

if __name__ == '__main__':
    utest.main()