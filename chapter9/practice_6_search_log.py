"""Check whether a log file contains the word 'python'."""

import argparse
from pathlib import Path


def contains_python(path):
    """Return True when 'python' occurs in the log, ignoring case."""
    with path.open(encoding="utf-8") as log_file:
        return any("python" in line.casefold() for line in log_file)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log_file", nargs="?", type=Path, default=Path("log.txt"))
    args = parser.parse_args()
    try:
        found = contains_python(args.log_file)
    except FileNotFoundError:
        parser.error(f"log file not found: {args.log_file}")
    except UnicodeError:
        parser.error(f"could not decode as UTF-8: {args.log_file}")
    print(f"'python' was {'found' if found else 'not found'} in {args.log_file}.")


if __name__ == "__main__":
    main()
