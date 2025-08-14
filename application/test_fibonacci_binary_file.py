import unittest
from fibonacci_module import generate_fibonacci_binary_file, read_fibonacci_from_binary_file, find_closest_fibonacci
import os

class TestFibonacciBinaryFile(unittest.TestCase):
    def test_generate_fibonacci_binary_file(self):
        max_numbers = 10
        filename = 'fibonacci.bin'
        generate_fibonacci_binary_file(max_numbers, filename)
        self.assertTrue(os.path.exists(filename))
        
    def test_read_fibonacci_from_binary_file(self):
        max_numbers = 10
        filename = 'fibonacci.bin'
        generate_fibonacci_binary_file(max_numbers, filename)
        fibonacci_numbers = read_fibonacci_from_binary_file(filename)
        self.assertEqual(len(fibonacci_numbers), max_numbers)
        
    def test_find_closest_fibonacci(self):
        max_numbers = 10
        filename = 'fibonacci.bin'
        generate_fibonacci_binary_file(max_numbers, filename)
        fibonacci_numbers = read_fibonacci_from_binary_file(filename)
        n = 10
        closest_fibonacci = find_closest_fibonacci(fibonacci_numbers, n)
        self.assertIn(closest_fibonacci, fibonacci_numbers)
        
if __name__ == '__main__':
    unittest.main()