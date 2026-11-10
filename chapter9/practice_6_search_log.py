"""Check whether a log file contains the word 'python'."""

import argparse
from pathlib import Path


def contains_python(path, term="python"):
    """Return True when term occurs in the log, ignoring case."""
    if not term:
        raise ValueError("search term must not be empty")
    with path.open(encoding="utf-8") as log_file:
        return any(term.casefold() in line.casefold() for line in log_file)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log_file", nargs="?", type=Path, default=Path("log.txt"))
    parser.add_argument("--term", default="python", help="term to search for")
    args = parser.parse_args()
    try:
        found = contains_python(args.log_file, args.term)
    except FileNotFoundError:
        parser.error(f"log file not found: {args.log_file}")
    except UnicodeError:
        parser.error(f"could not decode as UTF-8: {args.log_file}")
    except ValueError as error:
        parser.error(str(error))
    print(f"{args.term!r} was {'found' if found else 'not found'} in {args.log_file}.")


if __name__ == "__main__":
    main()
