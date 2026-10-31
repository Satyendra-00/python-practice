"""Read and display all the contents of a text file."""

file_name = "file.txt"

with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

print(content)
