"""Write multiplication tables from 2 to 20 into separate files."""

import argparse
from pathlib import Path


def write_tables(folder, start=2, end=20, limit=10):
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
    args = parser.parse_args()
    write_tables(args.folder)
    print(f"Tables from 2 to 20 have been saved in '{args.folder}'.")


if __name__ == "__main__":
    main()
