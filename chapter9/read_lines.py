"""Read a text file one line at a time."""

from pathlib import Path

file_name = Path("file.txt")

try:
    with file_name.open("r", encoding="utf-8") as file:
        found_line = False
        for line_number, line in enumerate(file, start=1):
            found_line = True
            content = line.rstrip("\r\n")
            print(f"{line_number}: {content}")

    if not found_line:
        print("The file is empty.")
except FileNotFoundError:
    print(f"File '{file_name}' does not exist.")
