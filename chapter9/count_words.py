"""Count the lines and words in a text file."""

import argparse
from pathlib import Path


def count_text(path):
    content = path.read_text(encoding="utf-8")
    return len(content.splitlines()), len(content.split())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", type=Path, default=Path("file.txt"))
    args = parser.parse_args()

    try:
        lines, words = count_text(args.file)
    except FileNotFoundError:
        parser.error(f"file not found: {args.file}")
    except UnicodeError:
        parser.error(f"could not decode as UTF-8: {args.file}")

    print(f"Lines: {lines}")
    print(f"Words: {words}")


if __name__ == "__main__":
    main()
