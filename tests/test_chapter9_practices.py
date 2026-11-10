import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from chapter9 import practice_4_replace_donkey
from chapter9 import practice_5_censor_words
from chapter9 import practice_6_search_log
from chapter9 import practice_7_python_line_numbers
from chapter9 import practice_8_copy_this
from chapter9 import practice_9_compare_files


class Chapter9PracticeTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.folder = Path(self.temp_dir.name)

    def test_replace_word_treats_replacement_as_literal_text(self):
        path = self.folder / "input.txt"
        path.write_text("Donkey", encoding="utf-8")

        count = practice_4_replace_donkey.replace_word(path, replacement=r"\g<1>")

        self.assertEqual(count, 1)
        self.assertEqual(path.read_text(encoding="utf-8"), r"\g<1>")

    def test_censor_words_treats_replacement_as_literal_text(self):
        path = self.folder / "input.txt"
        path.write_text("Donkey", encoding="utf-8")

        count = practice_5_censor_words.censor_words(
            path, words=("Donkey",), replacement=r"\g<1>"
        )

        self.assertEqual(count, 1)
        self.assertEqual(path.read_text(encoding="utf-8"), r"\g<1>")

    def test_search_log_cli_accepts_a_custom_term(self):
        path = self.folder / "log.txt"
        path.write_text("Found Needle", encoding="utf-8")
        output = io.StringIO()

        with patch("sys.argv", ["search_log.py", str(path), "--term", "needle"]):
            with contextlib.redirect_stdout(output):
                practice_6_search_log.main()

        self.assertIn("'needle' was found", output.getvalue())

    def test_line_number_cli_accepts_a_custom_term(self):
        path = self.folder / "log.txt"
        path.write_text("other\nNeedle here\n", encoding="utf-8")
        output = io.StringIO()

        with patch("sys.argv", ["line_numbers.py", str(path), "--term", "needle"]):
            with contextlib.redirect_stdout(output):
                practice_7_python_line_numbers.main()

        self.assertIn("'needle' found on line(s): 2", output.getvalue())

    def test_copy_does_not_create_destination_parent_when_source_is_missing(self):
        source = self.folder / "missing.txt"
        destination = self.folder / "new-folder" / "copy.txt"

        with self.assertRaises(FileNotFoundError):
            practice_8_copy_this.copy_text_file(source, destination)

        self.assertFalse(destination.parent.exists())

    def test_file_comparison_error_names_missing_path(self):
        missing = self.folder / "missing.txt"
        existing = self.folder / "existing.txt"
        existing.write_text("content", encoding="utf-8")

        with self.assertRaises(FileNotFoundError) as error:
            practice_9_compare_files.files_are_identical(missing, existing)

        self.assertIn(str(missing), str(error.exception))


if __name__ == "__main__":
    unittest.main()
