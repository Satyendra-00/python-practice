"""Read a text file one line at a time."""

from pathlib import Path

file_name = Path("file.txt")

try:
    with file_name.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        print("The file is empty.")
    else:
        for line_number, line in enumerate(lines, start=1):
            print(f"{line_number}: {line.rstrip()}")
except FileNotFoundError:
    print(f"File '{file_name}' does not exist.")
