import unittest
from fibonacci_module import is_square


class TestIsSquareFunction(unittest.TestCase):
    def test_perfect_squares(self):
        # Test that perfect squares return True
        self.assertTrue(is_square(1))
        self.assertTrue(is_square(4))
        self.assertTrue(is_square(9))
        self.assertTrue(is_square(16))
        self.assertTrue(is_square(25))
        
    def test_non_perfect_squares(self):
        # Test that non-perfect squares return False
        self.assertFalse(is_square(2))
        self.assertFalse(is_square(3))
        self.assertFalse(is_square(5))
        self.assertFalse(is_square(6))
        self.assertFalse(is_square(7))
        self.assertFalse(is_square(8))
        
    def test_zero(self):
        # Test that zero returns True
        self.assertTrue(is_square(0))
        
    def test_negative_numbers(self):
        # Test that negative numbers raise an error
        with self.assertRaises(ValueError):
            is_square(-1)
        with self.assertRaises(ValueError):
            is_square(-4)
        with self.assertRaises(ValueError):
            is_square(-9)
        
    def test_non_integer_inputs(self):
        # Test that non-integer inputs raise an error
        with self.assertRaises(ValueError):
            is_square(2.5)
        with self.assertRaises(ValueError):
            is_square(3.7)
        with self.assertRaises(ValueError):
            is_square(1.2)
           


if __name__ == '__main__':
    unittest.main()
