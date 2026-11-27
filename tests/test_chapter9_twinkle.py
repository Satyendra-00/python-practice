import tempfile
import unittest
from pathlib import Path

from chapter9.p1 import contains_twinkle


class ContainsTwinkleTests(unittest.TestCase):
    def test_matches_case_insensitively_around_punctuation(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "poem.txt"
            path.write_text("'TwInKlE,' little star", encoding="utf-8")

            self.assertTrue(contains_twinkle(path))

    def test_does_not_match_a_word_containing_twinkle(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "poem.txt"
            path.write_text("twinkler", encoding="utf-8")

            self.assertFalse(contains_twinkle(path))


if __name__ == "__main__":
    unittest.main()
