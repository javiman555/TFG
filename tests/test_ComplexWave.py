import unittest as utest
import numpy.testing as ntest
from src.model.objects.wave import ComplexWaveDB
from src.model.objects.wave import ComplexWaveRandom
import random as rd

class TestComplexWave(utest.TestCase):

    def test_create_random_complex_wave(self):
        rd.seed(4)
        complexWave = ComplexWaveRandom.ComplexWaveRandom(1,2, 2, 2, 5)
        
        self.assertEqual(complexWave.dataName, "Random - 2")
        self.assertEqual(complexWave.precision, 1)

        ntest.assert_array_almost_equal(complexWave.t, [0.,  0.2, 0.4, 0.6, 0.8])
        ntest.assert_array_almost_equal(complexWave.y, [-2.52441295,  2.99503816, -2.32166059,  0.76148758,  1.0895478 ])

    def test_create_stock_complex_wave(self):
        complexWave = ComplexWaveDB.ComplexWaveDB('SAB.MC','Open','DataStocksTest.csv',precision=1)
        
        self.assertEqual(complexWave.dataName, "SAB.MC")
        self.assertEqual(complexWave.precision, 1)
        self.assertEqual(complexWave.t[0], 0)
        self.assertAlmostEqual(complexWave.y[0], 0.4665)

        complexWaveDuplicated = ComplexWaveDB.ComplexWaveDB('SAB.MC','Open','DataStocksTest.csv',precision=1)
        
        ntest.assert_array_almost_equal(complexWave.t, complexWaveDuplicated.t)
        ntest.assert_array_almost_equal(complexWave.y, complexWaveDuplicated.y)


if __name__ == '__main__':
    utest.main()