import unittest
from src.script import add


class TestAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(3, 4)
        self.assertEqual(result, 7)

    def test_add_negative_numbers(self):
        result = add(-5, -2)
        self.assertEqual(result, -7)

    def test_add_zero(self):
        result = add(0, 10)
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main()
