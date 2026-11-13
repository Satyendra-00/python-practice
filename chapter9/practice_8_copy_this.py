"""Make a copy of this.txt named this_copy.txt."""

import argparse
from pathlib import Path


def copy_text_file(source, destination):
    """Copy UTF-8 text while preserving line endings exactly."""
    if source.resolve() == destination.resolve() or (
        destination.exists() and source.samefile(destination)
    ):
        raise ValueError("source and destination must be different files")
    with source.open("r", encoding="utf-8", newline="") as source_file:
        content = source_file.read()
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="") as destination_file:
        destination_file.write(content)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", type=Path, default=Path("this.txt"))
    parser.add_argument("destination", nargs="?", type=Path, default=Path("this_copy.txt"))
    args = parser.parse_args()
    try:
        copy_text_file(args.source, args.destination)
    except FileNotFoundError:
        parser.error(f"source file not found: {args.source}")
    except (UnicodeError, ValueError) as error:
        parser.error(str(error))
    print(f"Copied {args.source} to {args.destination}.")


if __name__ == "__main__":
    main()
