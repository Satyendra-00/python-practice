import unittest

from chapter8.p1 import greatest_of_three
from chapter7.p4 import is_prime


class GreatestOfThreeTests(unittest.TestCase):
    def test_returns_largest_when_values_differ(self):
        self.assertEqual(greatest_of_three(2, 9, 4), 9)

    def test_returns_tied_largest_value(self):
        self.assertEqual(greatest_of_three(9, 2, 9), 9)
        self.assertEqual(greatest_of_three(7, 7, 7), 7)


class PrimeNumberTests(unittest.TestCase):
    def test_numbers_below_two_are_not_prime(self):
        for number in (-5, 0, 1):
            with self.subTest(number=number):
                self.assertFalse(is_prime(number))

    def test_prime_and_composite_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(100))


if __name__ == "__main__":
    unittest.main()
