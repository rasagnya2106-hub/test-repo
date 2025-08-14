import unittest
from test_script import main


class TestTestScriptFunctions(unittest.TestCase):
    
    def test_main(self):
        # Test that the main function runs without any errors
        main()
        
if __name__ == '__main__':
    unittest.main()
