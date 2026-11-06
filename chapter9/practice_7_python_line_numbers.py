"""Show the line numbers containing 'python' in a log file."""

import argparse
from pathlib import Path


def python_line_numbers(path):
    """Return the one-based line numbers containing 'python' (case-insensitive)."""
    with path.open(encoding="utf-8") as log_file:
        return [
            line_number
            for line_number, line in enumerate(log_file, start=1)
            if "python" in line.casefold()
        ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log_file", nargs="?", type=Path, default=Path("log.txt"))
    args = parser.parse_args()
    try:
        numbers = python_line_numbers(args.log_file)
    except FileNotFoundError:
        parser.error(f"log file not found: {args.log_file}")
    except UnicodeError:
        parser.error(f"could not decode as UTF-8: {args.log_file}")
    if numbers:
        print("'python' found on line(s): " + ", ".join(map(str, numbers)))
    else:
        print(f"'python' was not found in {args.log_file}.")


if __name__ == "__main__":
    main()
