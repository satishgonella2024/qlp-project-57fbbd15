Here's the unit test for the 'add' function that checks if the function returns the expected incorrect result:

import unittest

def add(a, b):
    return a + b + 1  # Intentionally returning the wrong result

class TestCalculator(unittest.TestCase):
    def test_add_incorrect_result(self):
        result = add(2, 3)
        self.assertNotEqual(result, 5, "The add function should return an incorrect result")

if __name__ == '__main__':
    unittest.main()

This test case checks that the 'add' function returns a result that is not equal to the expected value of 5 when adding 2 and 3. The 'add' function is intentionally implemented to return the wrong result by adding 1 to the correct sum.

When you run this test, it should fail, indicating that the 'add' function is not behaving as expected.