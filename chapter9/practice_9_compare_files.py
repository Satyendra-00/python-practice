"""Check whether two text files have identical contents."""

import argparse
from pathlib import Path


def files_are_identical(first, second):
    """Compare files in binary mode so every byte must match."""
    if first.resolve() == second.resolve():
        return True
    with first.open("rb") as first_file, second.open("rb") as second_file:
        while True:
            first_chunk = first_file.read(8192)
            second_chunk = second_file.read(8192)
            if first_chunk != second_chunk:
                return False
            if not first_chunk:
                return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("first", nargs="?", type=Path, default=Path("this.txt"))
    parser.add_argument("second", nargs="?", type=Path, default=Path("this_copy.txt"))
    args = parser.parse_args()
    try:
        identical = files_are_identical(args.first, args.second)
    except FileNotFoundError as error:
        parser.error(f"file not found: {error.filename}")
    print("The files have identical contents." if identical else "The files differ.")


if __name__ == "__main__":
    main()
