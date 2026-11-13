"""Check whether a poem file contains the word 'twinkle'."""

import argparse
from pathlib import Path


def contains_twinkle(path):
    """Return whether a whitespace-delimited token is exactly ``twinkle``."""
    text = path.read_text(encoding="utf-8")
    words = (word.strip(".,!?;:'\"()[]{}") for word in text.split())
    return any(word.casefold() == "twinkle" for word in words)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", type=Path, default=Path("poems.txt"))
    args = parser.parse_args()
    try:
        found = contains_twinkle(args.file)
    except FileNotFoundError:
        parser.error(f"file not found: {args.file}")
    except UnicodeError:
        parser.error(f"could not decode as UTF-8: {args.file}")
    print(f"The word 'twinkle' is {'present' if found else 'not present'} in the file.")


if __name__ == "__main__":
    main()
