import unittest
from fibonacci_module import ensure_positive_int, fibList, is_fibonacci, n_Binet, f_Binet, nearest_Binet_fib, make_saved_Fibonacci_file, get_nth_saved_Fibonacci_number, nearest_saved_fib, nearest_saved_fib_index


class TestFibonacciModule(unittest.TestCase):
    
    def test_ensure_positive_int(self):
        # Test with valid positive integer
        self.assertEqual(ensure_positive_int(10), 10)
        
        # Test with non-integer input
        with self.assertRaises(ValueError):
            ensure_positive_int('abc')
        
        # Test with negative integer
        with self.assertRaises(ValueError):
            ensure_positive_int(-10)
        
        # Test with zero
        with self.assertRaises(ValueError):
            ensure_positive_int(0)
        
    def test_fibList(self):
        # Test with valid positive integer
        self.assertEqual(fibList(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        
        # Test with non-integer input
        with self.assertRaises(ValueError):
            fibList('abc')
        
        # Test with negative integer
        with self.assertRaises(ValueError):
            fibList(-10)
        
        # Test with zero
        self.assertEqual(fibList(0), [])
        
    def test_is_fibonacci(self):
        # Test with valid Fibonacci number
        self.assertTrue(is_fibonacci(13))
        
        # Test with non-Fibonacci number
        self.assertFalse(is_fibonacci(14))
        
        # Test with non-integer input
        with self.assertRaises(ValueError):
            is_fibonacci('abc')
        
        # Test with negative integer
        with self.assertRaises(ValueError):
            is_fibonacci(-10)
        
        # Test with zero
        self.assertTrue(is_fibonacci(0))
        
    def test_n_Binet(self):
        # Test with valid Fibonacci number
        self.assertEqual(n_Binet(13), (7, 7))
        
        # Test with non-Fibonacci number
        self.assertNotEqual(n_Binet(14), (7, 7))
        
        # Test with non-integer input
        with self.assertRaises(ValueError):
            n_Binet('abc')
        
        # Test with negative integer
        with self.assertRaises(ValueError):
            n_Binet(-10)
        
        # Test with zero
        self.assertEqual(n_Binet(0), (1, 1))
        
    def test_f_Binet(self):
        # Test with valid index
        self.assertEqual(f_Binet(7), 13)
        
        # Test with non-integer input
        with self.assertRaises(ValueError):
            f_Binet('abc')
        
        # Test with negative integer
        with self.assertRaises(ValueError):
            f_Binet(-10)
        
        # Test with zero
        with self.assertRaises(ValueError):
            f_Binet(0)
        
    def test_nearest_Binet_fib(self):
        # Test with valid input
        self.assertEqual(nearest_Binet_fib(14), 13)
        
        # Test with non-integer input
        with self.assertRaises(ValueError):
            nearest_Binet_fib('abc')
        
        # Test with negative integer
        with self.assertRaises(ValueError):
            nearest_Binet_fib(-10)
        
        # Test with zero
        self.assertEqual(nearest_Binet_fib(0), 0)
        
    def test_make_saved_Fibonacci_file(self):
        # Test that the file is created
        make_saved_Fibonacci_file()
        self.assertTrue(os.path.isfile('savedFibonacciNumbers.bin'))
        
    def test_get_nth_saved_Fibonacci_number(self):
        # Test with valid index
        self.assertEqual(get_nth_saved_Fibonacci_number(7), 13)
        
        # Test with non-integer input
        with self.assertRaises(ValueError):
            get_nth_saved_Fibonacci_number('abc')
        
        # Test with negative integer
        with self.assertRaises(ValueError):
            get_nth_saved_Fibonacci_number(-10)
        
        # Test with zero
        with self.assertRaises(ValueError):
            get_nth_saved_Fibonacci_number(0)
        
    def test_nearest_saved_fib(self):
        # Test with valid input
        self.assertEqual(nearest_saved_fib(14), 13)
        
        # Test with non-integer input
        with self.assertRaises(ValueError):
            nearest_saved_fib('abc')
        
        # Test with negative integer
        with self.assertRaises(ValueError):
            nearest_saved_fib(-10)
        
        # Test with zero
        self.assertEqual(nearest_saved_fib(0), 0)
        
    def test_nearest_saved_fib_index(self):
        # Test with valid input
        self.assertEqual(nearest_saved_fib_index(14), 7)
        
        # Test with non-integer input
        with self.assertRaises(ValueError):
            nearest_saved_fib_index('abc')
        
        # Test with negative integer
        with self.assertRaises(ValueError):
            nearest_saved_fib_index(-10)
        
        # Test with zero
        self.assertEqual(nearest_saved_fib_index(0), 1)
           


if __name__ == '__main__':
    unittest.main()
