"""List the entries in a directory."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args()

    if not args.directory.is_dir():
        parser.error(f"not a directory: {args.directory}")

    for item in sorted(args.directory.iterdir(), key=lambda path: path.name.casefold()):
        print(item.name)


if __name__ == "__main__":
    main()
