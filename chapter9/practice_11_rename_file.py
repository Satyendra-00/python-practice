"""Rename a file to renamed_by_python.txt."""

import argparse
from pathlib import Path

DESTINATION = Path("renamed_by_python.txt")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", type=Path, default=Path("this.txt"))
    parser.add_argument("--destination", type=Path, default=DESTINATION)
    args = parser.parse_args()
    if not args.source.is_file():
        parser.error(f"source file not found: {args.source}")
    if args.source.resolve() == args.destination.resolve():
        parser.error("source and destination are already the same file")
    if args.destination.exists():
        parser.error(f"destination already exists: {args.destination}")
    try:
        args.source.rename(args.destination)
    except OSError as error:
        parser.error(str(error))
    print(f"Renamed {args.source} to {args.destination}.")


if __name__ == "__main__":
    main()
