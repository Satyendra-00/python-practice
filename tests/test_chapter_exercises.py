import unittest

from chapter8.p1 import greatest_of_three


class GreatestOfThreeTests(unittest.TestCase):
    def test_returns_largest_when_values_differ(self):
        self.assertEqual(greatest_of_three(2, 9, 4), 9)

    def test_returns_tied_largest_value(self):
        self.assertEqual(greatest_of_three(9, 2, 9), 9)
        self.assertEqual(greatest_of_three(7, 7, 7), 7)


if __name__ == "__main__":
    unittest.main()
