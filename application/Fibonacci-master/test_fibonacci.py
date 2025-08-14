import unittest
from fibonacci import fibList
from fibonacci_module import phi


class TestFibonacciFunctions(unittest.TestCase):
    """
    Test class for fibonacci functions.
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

if __name__ == '__main__':
    unittest.main()