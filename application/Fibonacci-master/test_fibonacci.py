import unittest
from fibonacci import *
from fibonacci import closest_fibonacci


class TestFibonacciFunctions(unittest.TestCase):
    def test_fibList(self):
        self.assertEqual(fibList(1), [0])
        self.assertEqual(fibList(2), [0, 1])
        self.assertEqual(fibList(3), [0, 1, 1])
        self.assertEqual(fibList(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        
    def test_is_square(self):
        self.assertTrue(is_square(4))
        self.assertTrue(is_square(9))
        self.assertTrue(is_square(16))
        self.assertFalse(is_square(5))
        self.assertFalse(is_square(7))
        
    def test_is_fibonacci(self):
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
        self.assertFalse(is_fibonacci(4))
        self.assertFalse(is_fibonacci(6))
        self.assertFalse(is_fibonacci(7))
        self.assertFalse(is_fibonacci(9))
        self.assertFalse(is_fibonacci(10))
        self.assertFalse(is_fibonacci(11))
        self.assertFalse(is_fibonacci(12))
        
    def test_n_Binet(self):
        self.assertAlmostEqual(n_Binet(0), (1, 1))
        self.assertAlmostEqual(n_Binet(1), (1, 1))
        self.assertAlmostEqual(n_Binet(1), (1, 1))
        self.assertAlmostEqual(n_Binet(2), (2, 2))
        self.assertAlmostEqual(n_Binet(3), (3, 3))
        self.assertAlmostEqual(n_Binet(5), (5, 5))
        self.assertAlmostEqual(n_Binet(8), (6, 6))
        self.assertAlmostEqual(n_Binet(13), (7, 7))
        self.assertAlmostEqual(n_Binet(21), (8, 8))
        self.assertAlmostEqual(n_Binet(34), (9, 9))
        
    def test_f_Binet(self):
        self.assertEqual(f_Binet(1), 0)
        self.assertEqual(f_Binet(2), 1)
        self.assertEqual(f_Binet(3), 1)
        self.assertEqual(f_Binet(4), 2)
        self.assertEqual(f_Binet(5), 3)
        self.assertEqual(f_Binet(6), 5)
        self.assertEqual(f_Binet(7), 8)
        self.assertEqual(f_Binet(8), 13)
        self.assertEqual(f_Binet(9), 21)
        self.assertEqual(f_Binet(10), 34)
        
    def test_nearest_Binet_fib(self):
        self.assertEqual(nearest_Binet_fib(0), 0)
        self.assertEqual(nearest_Binet_fib(1), 1)
        self.assertEqual(nearest_Binet_fib(2), 1)
        self.assertEqual(nearest_Binet_fib(3), 2)
        self.assertEqual(nearest_Binet_fib(4), 3)
        self.assertEqual(nearest_Binet_fib(5), 5)
        self.assertEqual(nearest_Binet_fib(6), 5)
        self.assertEqual(nearest_Binet_fib(7), 8)
        self.assertEqual(nearest_Binet_fib(8), 8)
        self.assertEqual(nearest_Binet_fib(9), 8)
        self.assertEqual(nearest_Binet_fib(10), 8)
        self.assertEqual(nearest_Binet_fib(11), 13)
        self.assertEqual(nearest_Binet_fib(12), 13)
    
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
