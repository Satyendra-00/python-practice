"""Write multiplication tables from 2 to 20 into separate files."""

import argparse
from pathlib import Path


def write_tables(folder, start=2, end=20, limit=10):
    if start > end:
        raise ValueError("start must be less than or equal to end")
    if limit < 1:
        raise ValueError("limit must be at least 1")
    folder.mkdir(parents=True, exist_ok=True)
    for number in range(start, end + 1):
        file_path = folder / f"table_{number}.txt"
        with file_path.open("w", encoding="utf-8") as file:
            file.write(f"Multiplication table of {number}\n")
            for multiplier in range(1, limit + 1):
                file.write(f"{number} x {multiplier} = {number * multiplier}\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--folder", type=Path, default=Path("tables"))
    parser.add_argument("--start", type=int, default=2)
    parser.add_argument("--end", type=int, default=20)
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    try:
        write_tables(args.folder, args.start, args.end, args.limit)
    except ValueError as error:
        parser.error(str(error))
    print(f"Tables from {args.start} to {args.end} have been saved in '{args.folder}'.")


if __name__ == "__main__":
    main()
