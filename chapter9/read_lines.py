"""Read a text file one line at a time."""

file_name = "file.txt"

with open(file_name, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"{line_number}: {line.rstrip()}")
