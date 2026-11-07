"""Replace every occurrence of 'Donkey' in a text file."""

import argparse
import re
from pathlib import Path


def replace_word(path, word="Donkey", replacement="#####"):
    if not word:
        raise ValueError("word must not be empty")
    text = path.read_text(encoding="utf-8")
    updated_text, replacements = re.subn(
        rf"\b{re.escape(word)}\b", replacement, text, flags=re.IGNORECASE
    )
    if replacements:
        path.write_text(updated_text, encoding="utf-8")
    return replacements


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", type=Path, default=Path("donkey.txt"))
    args = parser.parse_args()

    try:
        replacements = replace_word(args.file)
    except FileNotFoundError:
        parser.error(f"file not found: {args.file}")
    except UnicodeError:
        parser.error(f"could not decode as UTF-8: {args.file}")

    if replacements:
        print(f"Replaced 'Donkey' {replacements} time(s) with '#####'.")
    else:
        print("The word 'Donkey' was not found; the file was left unchanged.")


if __name__ == "__main__":
    main()
