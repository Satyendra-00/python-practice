"""Write a string to a text file."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", type=Path, default=Path("file.txt"))
    parser.add_argument("text", nargs="?", default="hey you are amazing")
    args = parser.parse_args()
    args.file.write_text(args.text, encoding="utf-8")
    print(f"Saved text to '{args.file}'.")


if __name__ == "__main__":
    main()
