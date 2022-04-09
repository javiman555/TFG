import unittest as utest
import numpy.testing as ntest
from src.objects.wave import SimpleWave
import random as rd

class TestSimpleWave(utest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')
        
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
       
    
    def setUp(self):
        print('setup')
    
    def tearDown(self):
        print('tearDown')

    def test_create_simple_wave(self):
        rd.seed(4)
        simpleWave = SimpleWave.SimpleWave(1, 1, 5)
        ntest.assert_array_almost_equal(simpleWave.t, [0.,  0.2, 0.4, 0.6, 0.8])
        ntest.assert_array_almost_equal(simpleWave.y, [-0.84147098,  0.25382919,  0.99834605,  0.3631826,  -0.77388686])

    def test_compare_two_simple_wave(self):
        rd.seed(4)
        simpleWave1 = SimpleWave.SimpleWave(1, 1, 5)
        rd.seed(4)
        simpleWave2 = SimpleWave.SimpleWave(1, 1, 5)
        ntest.assert_array_almost_equal(simpleWave1.t, simpleWave2.t)
        ntest.assert_array_almost_equal(simpleWave1.y, simpleWave2.y)
    
    def test_create_wrong_simple_wave(self):
        with self.assertRaises(ValueError):
            SimpleWave.SimpleWave(1, 1, -1)

if __name__ == '__main__':
    utest.main()