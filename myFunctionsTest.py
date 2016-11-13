from myFunctions import my_contains, my_first
import unittest

class TestMyFunctions(unittest.TestCase):
    def test_contains_simple_true(self):
        self.assertTrue(my_contains(3, [1, 2, 3]))

    def test_first_numbers(self):
        self.assertEqual(my_first([1, 2, 3]), 1)

    def test_first_empty(self):
        self.assertRaises(IndexError, my_first, [])


if __name__ == '__main__':
    unittest.main(exit=False)
