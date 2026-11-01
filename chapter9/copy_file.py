"""Copy the contents of one text file into another file."""

from pathlib import Path

source_name = Path("file.txt")
destination_name = Path("file_copy.txt")

if source_name == destination_name:
    print("Source and destination are the same file. Nothing to copy.")
else:
    try:
        content = source_name.read_text(encoding="utf-8")
        destination_name.write_text(content, encoding="utf-8")
        print(f"Contents copied from {source_name} to {destination_name}.")
    except FileNotFoundError:
        print(f"Source file '{source_name}' does not exist.")
