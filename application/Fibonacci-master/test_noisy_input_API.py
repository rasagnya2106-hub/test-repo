import unittest
from noisy_input_API import add_noise, get_data
import numpy as np


class TestNoisyInputAPI(unittest.TestCase):
    def test_add_noise(self):
        # Test add_noise function
        pure_data = [1, 2, 3, 4, 5]
        noisy_data = add_noise(pure_data)
        self.assertEqual(len(pure_data), len(noisy_data))
        for i in range(len(pure_data)):
            self.assertAlmostEqual(pure_data[i], noisy_data[i], places=2)

    def test_get_data(self):
        # Test get_data function
        num_data_points = 10
        data = get_data(num_data_points)
        self.assertEqual(len(data), num_data_points)
        for i in range(len(data)):
            self.assertGreaterEqual(data[i], 0)

    def test_get_data_edge_cases(self):
        # Test get_data function with edge cases
        num_data_points = 0
        data = get_data(num_data_points)
        self.assertEqual(len(data), 0)

        num_data_points = -1
        with self.assertRaises(ValueError):
            get_data(num_data_points)

if __name__ == '__main__':
    unittest.main()