"""Find and display the lines that contain a search word."""

import argparse
from pathlib import Path


def find_matches(path, search_word):
    with path.open(encoding="utf-8") as file:
        return [
            (line_number, line.rstrip())
            for line_number, line in enumerate(file, start=1)
            if search_word.casefold() in line.casefold()
        ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("word", help="word or phrase to search for")
    parser.add_argument("file", nargs="?", type=Path, default=Path("file.txt"))
    args = parser.parse_args()

    if not args.word.strip():
        parser.error("search word cannot be empty")

    try:
        matches = find_matches(args.file, args.word.strip())
    except FileNotFoundError:
        parser.error(f"file not found: {args.file}")
    except UnicodeError:
        parser.error(f"could not decode as UTF-8: {args.file}")

    for line_number, line in matches:
        print(f"Found on line {line_number}: {line}")
    if not matches:
        print(f"'{args.word}' was not found in {args.file}.")


if __name__ == "__main__":
    main()
