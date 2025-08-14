import unittest
from fibonacci_module import ensure_positive_int

class TestEnsurePositiveInt(unittest.TestCase):
    def test_non_integer_input(self):
        # Test ensure_positive_int with non-integer input
        with self.assertRaises(ValueError):
            ensure_positive_int('abc')
        
    def test_negative_integer_input(self):
        # Test ensure_positive_int with negative integer input
        with self.assertRaises(ValueError):
            ensure_positive_int(-10)
        
    def test_zero_input(self):
        # Test ensure_positive_int with zero input
        with self.assertRaises(ValueError):
            ensure_positive_int(0)
        
    def test_positive_integer_input(self):
        # Test ensure_positive_int with positive integer input
        self.assertEqual(ensure_positive_int(10), 10)
        
    def test_float_input(self):
        # Test ensure_positive_int with float input
        with self.assertRaises(ValueError):
            ensure_positive_int(10.5)
        
if __name__ == '__main__':
    unittest.main()