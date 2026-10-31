"""Count the lines and words in a text file."""

file_name = "file.txt"

with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

line_count = len(content.splitlines())
word_count = len(content.split())

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
