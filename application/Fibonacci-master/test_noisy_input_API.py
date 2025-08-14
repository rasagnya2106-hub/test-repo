import unittest
from noisy_input_API import add_noise, get_data
import numpy as np


class TestNoisyInputAPI(unittest.TestCase):
    
    def test_add_noise(self):
        # Test with valid inputs
        y = [1, 2, 3, 4, 5]
        noisy_y = add_noise(y)
        self.assertNotEqual(y, noisy_y)
        
        # Test with edge cases
        y = []
        noisy_y = add_noise(y)
        self.assertEqual(y, noisy_y)
        
        # Test with large and small values
        y = [1e10, 1e-10]
        noisy_y = add_noise(y)
        self.assertNotEqual(y, noisy_y)
        
    def test_get_data(self):
        # Test with valid inputs
        n = 10
        data = get_data(n)
        self.assertEqual(len(data), n)
        
        # Test with edge cases
        n = 0
        data = get_data(n)
        self.assertEqual(data, [])
        
        n = -1
        with self.assertRaises(ValueError):
            get_data(n)
        
        # Test with large and small values
        n = 100
        data = get_data(n)
        self.assertEqual(len(data), n)
        
    def test_get_data_with_noise(self):
        # Test that the noise is applied correctly
        n = 10
        data = get_data(n)
        self.assertNotEqual(data, [fb.fibList(n)[0][i] for i in range(n)])
        
if __name__ == '__main__':
    unittest.main()
