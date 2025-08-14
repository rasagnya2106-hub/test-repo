import unittest
from fibonacci_module import fibList, phi, is_fibonacci, f_Binet, n_Binet, nearest_Binet_fib, make_saved_Fibonacci_file, get_nth_saved_Fibonacci_number, nearest_saved_fib, nearest_saved_fib_index
import os


class TestFibonacciModuleFunctions(unittest.TestCase):
    """
    Test class for fibonacci_module functions.
    """
    def test_fibList(self):
        """
        Test the fibList function.
        """
        self.assertEqual(fibList(1), ([0], ''))
        self.assertEqual(fibList(2), ([0, 1], ''))
        self.assertEqual(fibList(3), ([0, 1, 1], ''))
        self.assertEqual(fibList(5), ([0, 1, 1, 2, 3], ''))
        self.assertEqual(fibList(8), ([0, 1, 1, 2, 3, 5, 8, 13], ''))

    def test_phi(self):
        """
        Test the phi constant.
        """
        self.assertAlmostEqual(phi, (1 + 5**0.5)/2)

    def test_is_fibonacci(self):
        """
        Test the is_fibonacci function.
        """
        self.assertTrue(is_fibonacci(0))
        self.assertTrue(is_fibonacci(1))
        self.assertTrue(is_fibonacci(1))
        self.assertTrue(is_fibonacci(2))
        self.assertTrue(is_fibonacci(3))
        self.assertTrue(is_fibonacci(5))
        self.assertTrue(is_fibonacci(8))
        self.assertTrue(is_fibonacci(13))
        self.assertFalse(is_fibonacci(4))
        self.assertFalse(is_fibonacci(6))
        self.assertFalse(is_fibonacci(7))
        self.assertFalse(is_fibonacci(9))
        self.assertFalse(is_fibonacci(10))
        self.assertFalse(is_fibonacci(11))
        self.assertFalse(is_fibonacci(12))

    def test_f_Binet(self):
        """
        Test the f_Binet function.
        """
        self.assertEqual(f_Binet(1), 0)
        self.assertEqual(f_Binet(2), 1)
        self.assertEqual(f_Binet(3), 1)
        self.assertEqual(f_Binet(5), 3)
        self.assertEqual(f_Binet(8), 13)

    def test_n_Binet(self):
        """
        Test the n_Binet function.
        """
        self.assertAlmostEqual(n_Binet(0), (1, 1))
        self.assertAlmostEqual(n_Binet(1), (2, 2))
        self.assertAlmostEqual(n_Binet(1), (2, 2))
        self.assertAlmostEqual(n_Binet(2), (3, 3))
        self.assertAlmostEqual(n_Binet(3), (5, 5))
        self.assertAlmostEqual(n_Binet(8), (13, 13))
        self.assertAlmostEqual(n_Binet(13), (21, 21))

    def test_nearest_Binet_fib(self):
        """
        Test the nearest_Binet_fib function.
        """
        self.assertEqual(nearest_Binet_fib(0), 0)
        self.assertEqual(nearest_Binet_fib(1), 1)
        self.assertEqual(nearest_Binet_fib(1), 1)
        self.assertEqual(nearest_Binet_fib(2), 2)
        self.assertEqual(nearest_Binet_fib(3), 3)
        self.assertEqual(nearest_Binet_fib(5), 5)
        self.assertEqual(nearest_Binet_fib(8), 8)
        self.assertEqual(nearest_Binet_fib(13), 13)
        self.assertEqual(nearest_Binet_fib(4), 3)
        self.assertEqual(nearest_Binet_fib(6), 5)
        self.assertEqual(nearest_Binet_fib(7), 8)
        self.assertEqual(nearest_Binet_fib(9), 8)
        self.assertEqual(nearest_Binet_fib(10), 8)
        self.assertEqual(nearest_Binet_fib(11), 13)
        self.assertEqual(nearest_Binet_fib(12), 13)

    def test_make_saved_Fibonacci_file(self):
        """
        Test the make_saved_Fibonacci_file function.
        """
        make_saved_Fibonacci_file()
        self.assertTrue(os.path.isfile('savedFibonacciNumbers.bin'))

    def test_get_nth_saved_Fibonacci_number(self):
        """
        Test the get_nth_saved_Fibonacci_number function.
        """
        make_saved_Fibonacci_file()
        self.assertEqual(get_nth_saved_Fibonacci_number(1), 0)
        self.assertEqual(get_nth_saved_Fibonacci_number(2), 1)
        self.assertEqual(get_nth_saved_Fibonacci_number(3), 1)
        self.assertEqual(get_nth_saved_Fibonacci_number(5), 3)
        self.assertEqual(get_nth_saved_Fibonacci_number(8), 13)

    def test_nearest_saved_fib(self):
        """
        Test the nearest_saved_fib function.
        """
        make_saved_Fibonacci_file()
        self.assertEqual(nearest_saved_fib(0), 0)
        self.assertEqual(nearest_saved_fib(1), 1)
        self.assertEqual(nearest_saved_fib(1), 1)
        self.assertEqual(nearest_saved_fib(2), 2)
        self.assertEqual(nearest_saved_fib(3), 3)
        self.assertEqual(nearest_saved_fib(5), 5)
        self.assertEqual(nearest_saved_fib(8), 8)
        self.assertEqual(nearest_saved_fib(13), 13)
        self.assertEqual(nearest_saved_fib(4), 3)
        self.assertEqual(nearest_saved_fib(6), 5)
        self.assertEqual(nearest_saved_fib(7), 8)
        self.assertEqual(nearest_saved_fib(9), 8)
        self.assertEqual(nearest_saved_fib(10), 8)
        self.assertEqual(nearest_saved_fib(11), 13)
        self.assertEqual(nearest_saved_fib(12), 13)

    def test_nearest_saved_fib_index(self):
        """
        Test the nearest_saved_fib_index function.
        """
        make_saved_Fibonacci_file()
        self.assertEqual(nearest_saved_fib_index(0), 1)
        self.assertEqual(nearest_saved_fib_index(1), 2)
        self.assertEqual(nearest_saved_fib_index(1), 2)
        self.assertEqual(nearest_saved_fib_index(2), 3)
        self.assertEqual(nearest_saved_fib_index(3), 4)
        self.assertEqual(nearest_saved_fib_index(5), 6)
        self.assertEqual(nearest_saved_fib_index(8), 8)
        self.assertEqual(nearest_saved_fib_index(13), 10)
        self.assertEqual(nearest_saved_fib_index(4), 4)
        self.assertEqual(nearest_saved_fib_index(6), 6)
        self.assertEqual(nearest_saved_fib_index(7), 8)
        self.assertEqual(nearest_saved_fib_index(9), 7)
        self.assertEqual(nearest_saved_fib_index(10), 7)
        self.assertEqual(nearest_saved_fib_index(11), 10)
        self.assertEqual(nearest_saved_fib_index(12), 10)

if __name__ == '__main__':
    unittest.main()