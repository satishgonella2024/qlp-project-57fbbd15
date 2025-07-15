class TestAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
        
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        
    def test_add_float_numbers(self):
        self.assertEqual(add(2.5, 3.7), 6.2)
        
    def test_add_failure(self):
        self.assertEqual(add(2, 3), 6)  # This test should fail

if __name__ == '__main__':
    unittest.main()