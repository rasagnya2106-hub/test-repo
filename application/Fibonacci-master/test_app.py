import unittest
from app import app


class TestAppFunctions(unittest.TestCase):
    
    def test_index(self):
        # Test that the index function returns a 200 status code
        tester = app.test_client()
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_test_script(self):
        # Test that the test_script function returns a 200 status code
        tester = app.test_client()
        response = tester.get('/test_script')
        self.assertEqual(response.status_code, 200)
        
    def test_fib_usage(self):
        # Test that the fib_usage function returns a 200 status code
        tester = app.test_client()
        response = tester.get('/fib_usage')
        self.assertEqual(response.status_code, 200)
        
    def test_my_fib(self):
        # Test that the my_fib function returns a 200 status code
        tester = app.test_client()
        response = tester.get('/myFib?argument=10')
        self.assertEqual(response.status_code, 200)
        
    def test_my_fib_invalid_input(self):
        # Test that the my_fib function returns a 200 status code with invalid input
        tester = app.test_client()
        response = tester.get('/myFib?argument=abc')
        self.assertEqual(response.status_code, 200)
        
    def test_my_fib_negative_input(self):
        # Test that the my_fib function returns a 200 status code with negative input
        tester = app.test_client()
        response = tester.get('/myFib?argument=-10')
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
