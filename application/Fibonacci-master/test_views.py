import unittest
from unittest.mock import patch, MagicMock
from app import app
from app.views import index, test_script, fib_usage, my_fib


class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        with patch('flask.render_template') as mock_render_template:
            index()
            mock_render_template.assert_called_once_with('index.html', title="Home")

    def test_test_script(self):
        with patch('flask.render_template') as mock_render_template:
            test_script()
            mock_render_template.assert_called_once_with('test_script.html')

    def test_fib_usage(self):
        with patch('flask.render_template') as mock_render_template:
            fib_usage()
            mock_render_template.assert_called_once_with('usage.html')

    def test_my_fib(self):
        with patch('app.views.fib_list') as mock_fib_list:
            mock_fib_list.return_value = ([0, 1], '')
            result = my_fib('10')
            self.assertEqual(result.status_code, 200)
            self.assertIn(b'First 10 Fibonacci numbers:', result.data)

    def test_my_fib_invalid_input(self):
        result = my_fib('abc')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Could not interpret abc as an integer.', result.data)

    def test_my_fib_negative_input(self):
        result = my_fib('-10')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Invalid input. -10 must be a positive integer.', result.data)

if __name__ == '__main__':
    unittest.main()
