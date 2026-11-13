"""Append a line of text to a file."""

import argparse
from pathlib import Path


def append_line(path, text):
    with path.open("a", encoding="utf-8") as file:
        file.write(text + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", type=Path, default=Path("file.txt"))
    args = parser.parse_args()

    data = input("Enter the data to append: ")
    if not data.strip():
        print("No data entered. Nothing was appended.")
        return

    append_line(args.file, data)
    print(f"Data appended successfully to '{args.file}'.")


if __name__ == "__main__":
    main()
