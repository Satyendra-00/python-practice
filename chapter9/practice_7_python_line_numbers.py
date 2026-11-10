"""Show the line numbers containing 'python' in a log file."""

import argparse
from pathlib import Path


def python_line_numbers(path, term="python"):
    """Return one-based line numbers containing term (case-insensitive)."""
    if not term:
        raise ValueError("search term must not be empty")
    with path.open(encoding="utf-8") as log_file:
        return [
            line_number
            for line_number, line in enumerate(log_file, start=1)
            if term.casefold() in line.casefold()
        ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log_file", nargs="?", type=Path, default=Path("log.txt"))
    parser.add_argument("--term", default="python", help="term to search for")
    args = parser.parse_args()
    try:
        numbers = python_line_numbers(args.log_file, args.term)
    except FileNotFoundError:
        parser.error(f"log file not found: {args.log_file}")
    except UnicodeError:
        parser.error(f"could not decode as UTF-8: {args.log_file}")
    except ValueError as error:
        parser.error(str(error))
    if numbers:
        print(f"{args.term!r} found on line(s): " + ", ".join(map(str, numbers)))
    else:
        print(f"{args.term!r} was not found in {args.log_file}.")


if __name__ == "__main__":
    main()
