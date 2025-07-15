import unittest
from src.calculator import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 6)  # This test should fail

if __name__ == '__main__':
    unittest.main()