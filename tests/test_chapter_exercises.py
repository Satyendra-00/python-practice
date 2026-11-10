from importlib import import_module
import unittest

from chapter8.p1 import greatest_of_three
from chapter7.p4 import is_prime
from chapter7.p6 import factorial
from chapter7.p5 import sum_to
from projects.project1 import play_round

average_module = import_module("chapter8.functions&reccursion")


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


class FactorialTests(unittest.TestCase):
    def test_factorial_values(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(6), 720)

    def test_negative_input_is_rejected(self):
        with self.assertRaises(ValueError):
            factorial(-1)


class SumToTests(unittest.TestCase):
    def test_sums_inclusive_range_from_zero(self):
        self.assertEqual(sum_to(0), 0)
        self.assertEqual(sum_to(5), 15)

    def test_negative_input_is_rejected(self):
        with self.assertRaises(ValueError):
            sum_to(-1)


class AverageTests(unittest.TestCase):
    def test_computes_average_without_replacing_builtin_sum(self):
        self.assertEqual(average_module.average([2, 4, 6]), 4)

    def test_rejects_empty_collection(self):
        with self.assertRaises(ValueError):
            average_module.average([])


class GameRoundTests(unittest.TestCase):
    def test_rejects_choices_outside_the_game(self):
        with self.assertRaises(ValueError):
            play_round(0, 1)
        with self.assertRaises(ValueError):
            play_round(1, 4)

    def test_returns_result_for_valid_choices(self):
        self.assertEqual(play_round(1, 2), "You win!")
        self.assertEqual(play_round(3, 3), "It's a draw.")


if __name__ == "__main__":
    unittest.main()
