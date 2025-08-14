import unittest
from unittest.mock import Mock, patch
from run import app


class TestRun(unittest.TestCase):
    
    @patch('app.app')
    def test_run(self, mock_app):
        # Test that the app runs without any errors
        mock_app.run.return_value = None
        app.run(debug=True)
        mock_app.run.assert_called_once_with(debug=True)
        
if __name__ == '__main__':
    unittest.main()
