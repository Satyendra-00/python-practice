"""Read and display all the contents of a text file."""

from pathlib import Path

file_name = Path("file.txt")

if not file_name.exists():
    print(f"File '{file_name}' does not exist.")
else:
    content = file_name.read_text(encoding="utf-8")
    print(content)
