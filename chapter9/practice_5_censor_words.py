"""Replace a list of censored words in a text file with hashes."""

import argparse
import re
from pathlib import Path

CENSORED_WORDS = ("Donkey", "badword")
REPLACEMENT = "#####"


def censor_words(path, words=CENSORED_WORDS, replacement=REPLACEMENT):
    """Replace whole-word matches (case-insensitively) and return the count."""
    words = tuple(word for word in words if word)
    if not words:
        return 0
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(
        r"\b(?:" + "|".join(re.escape(word) for word in words) + r")\b",
        flags=re.IGNORECASE,
    )
    updated_text, count = pattern.subn(replacement, text)
    if count:
        path.write_text(updated_text, encoding="utf-8")
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", type=Path, default=Path("donkey.txt"))
    args = parser.parse_args()
    try:
        count = censor_words(args.file)
    except FileNotFoundError:
        parser.error(f"file not found: {args.file}")
    except UnicodeError:
        parser.error(f"could not decode as UTF-8: {args.file}")

    if count:
        print(f"Censored {count} word occurrence(s) in {args.file}.")
    else:
        print(f"No censored words found in {args.file}; file unchanged.")


if __name__ == "__main__":
    main()
