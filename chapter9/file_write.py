"""Write a string to a text file."""

from pathlib import Path

text = "hey you are amazing"
file_path = Path("file.txt")

file_path.write_text(text, encoding="utf-8")
print(f"Saved text to '{file_path}'.")