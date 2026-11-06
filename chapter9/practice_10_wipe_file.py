"""Wipe the contents of a file after asking for confirmation."""

import argparse
from pathlib import Path


def wipe_file(path):
    """Truncate a file, leaving it present but empty."""
    with path.open("w", encoding="utf-8"):
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="file whose contents should be erased")
    args = parser.parse_args()
    if not args.file.is_file():
        parser.error(f"file not found: {args.file}")
    answer = input(f"Erase all contents of '{args.file}'? Type yes to continue: ").strip().lower()
    if answer != "yes":
        print("Cancelled; file was not changed.")
        return
    try:
        wipe_file(args.file)
    except OSError as error:
        parser.error(str(error))
    print(f"Contents of {args.file} have been erased.")


if __name__ == "__main__":
    main()
