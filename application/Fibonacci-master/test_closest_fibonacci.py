import unittest
from fibonacci import *


class TestClosestFibonacciFunctions(unittest.TestCase):
    def test_closest_fibonacci(self):
        self.assertEqual(closest_fibonacci(0), 0)
        self.assertEqual(closest_fibonacci(1), 1)
        self.assertEqual(closest_fibonacci(2), 1)
        self.assertEqual(closest_fibonacci(3), 2)
        self.assertEqual(closest_fibonacci(4), 3)
        self.assertEqual(closest_fibonacci(5), 5)
        self.assertEqual(closest_fibonacci(6), 5)
        self.assertEqual(closest_fibonacci(7), 8)
        self.assertEqual(closest_fibonacci(8), 8)
        self.assertEqual(closest_fibonacci(9), 8)
        self.assertEqual(closest_fibonacci(10), 8)
        self.assertEqual(closest_fibonacci(11), 13)
        self.assertEqual(closest_fibonacci(12), 13)
        
    def test_closest_fibonacci_non_integer(self):
        self.assertEqual(closest_fibonacci(3.5), 3)
        self.assertEqual(closest_fibonacci(4.2), 3)
        self.assertEqual(closest_fibonacci(5.7), 5)
        self.assertEqual(closest_fibonacci(6.3), 5)
        self.assertEqual(closest_fibonacci(7.9), 8)
        self.assertEqual(closest_fibonacci(8.1), 8)
        self.assertEqual(closest_fibonacci(9.4), 8)
        self.assertEqual(closest_fibonacci(10.6), 8)
        self.assertEqual(closest_fibonacci(11.7), 13)
        self.assertEqual(closest_fibonacci(12.3), 13)
        
    def test_closest_fibonacci_zero(self):
        self.assertEqual(closest_fibonacci(0), 0)
         


if __name__ == '__main__':
    unittest.main()
