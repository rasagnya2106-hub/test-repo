import unittest
from views import index, test_script, fib_usage, myFib
from flask import url_for
from yourapplication import app


class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def test_index(self):
        # Test root URL
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)
        
        # Test /index URL
        response = self.app.get('/index')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)
        
    def test_test_script(self):
        # Test /test_script.html URL
        response = self.app.get('/test_script.html')
        self.assertEqual(response.status_code, 200)
        
    def test_fib_usage(self):
        # Test /fib/ URL
        response = self.app.get('/fib/')
        self.assertEqual(response.status_code, 200)
        
    def test_myFib_valid_input(self):
        # Test myFib with valid integer input
        response = self.app.get('/fib/10')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Fibonacci sequence:', response.data)
        
    def test_myFib_non_integer_input(self):
        # Test myFib with non-integer input
        response = self.app.get('/fib/abc')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid input. Please enter a positive integer.', response.data)
        
    def test_myFib_negative_input(self):
        # Test myFib with negative integer input
        response = self.app.get('/fib/-10')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid input. Please enter a positive integer.', response.data)
        
    def test_myFib_truncated_output(self):
        # Test myFib with truncated output
        response = self.app.get('/fib/100')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Fibonacci sequence truncated after', response.data)
        
    def test_fibList(self):
        # Test fibList with various inputs
        self.assertEqual(fibList(1), [0])
        self.assertEqual(fibList(2), [0, 1])
        self.assertEqual(fibList(3), [0, 1, 1])
        self.assertEqual(fibList(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        
        # Test fibList with edge cases
        self.assertEqual(fibList(0), [])
        self.assertEqual(fibList(-1), [])
        
        # Test fibList with truncation
        self.assertEqual(len(fibList(100)), 10)  # assuming TRUNCATE_AFTER_THIS_MANY = 10
         


if __name__ == '__main__':
    unittest.main()
