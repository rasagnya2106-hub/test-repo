import unittest
from make_saved_Fibonacci_file import make_saved_fibonacci_file
import os.path
import distutils.util


class TestMakeSavedFibonacciFileFunctions(unittest.TestCase):
    
    def test_make_saved_fibonacci_file(self):
        # Test that the file is created
        make_saved_fibonacci_file()
        self.assertTrue(os.path.isfile('savedFibonacciNumbers.bin'))
        
if __name__ == '__main__':
    unittest.main()
