import unittest
from fibonacci_module import is_fibonacci


class TestIsFibonacciFunction(unittest.TestCase):
    def test_fibonacci_numbers(self):
        # Test that Fibonacci numbers return True
        self.assertTrue(is_fibonacci(0))
        self.assertTrue(is_fibonacci(1))
        self.assertTrue(is_fibonacci(1))
        self.assertTrue(is_fibonacci(2))
        self.assertTrue(is_fibonacci(3))
        self.assertTrue(is_fibonacci(5))
        self.assertTrue(is_fibonacci(8))
        self.assertTrue(is_fibonacci(13))
        self.assertTrue(is_fibonacci(21))
        self.assertTrue(is_fibonacci(34))
        
    def test_non_fibonacci_numbers(self):
        # Test that non-Fibonacci numbers return False
        self.assertFalse(is_fibonacci(2))
        self.assertFalse(is_fibonacci(3))
        self.assertFalse(is_fibonacci(4))
        self.assertFalse(is_fibonacci(6))
        self.assertFalse(is_fibonacci(7))
        self.assertFalse(is_fibonacci(9))
        self.assertFalse(is_fibonacci(10))
        self.assertFalse(is_fibonacci(11))
        self.assertFalse(is_fibonacci(12))
        
    def test_zero(self):
        # Test that zero returns True
        self.assertTrue(is_fibonacci(0))
        
    def test_negative_numbers(self):
        # Test that negative numbers raise an error
        with self.assertRaises(ValueError):
            is_fibonacci(-1)
        with self.assertRaises(ValueError):
            is_fibonacci(-2)
        with self.assertRaises(ValueError):
            is_fibonacci(-3)
        
    def test_non_integer_inputs(self):
        # Test that non-integer inputs raise an error
        with self.assertRaises(ValueError):
            is_fibonacci(2.5)
        with self.assertRaises(ValueError):
            is_fibonacci(3.7)
        with self.assertRaises(ValueError):
            is_fibonacci(1.2)
          


if __name__ == '__main__':
    unittest.main()
