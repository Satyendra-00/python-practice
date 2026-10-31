"""Copy the contents of one text file into another file."""

source_name = "file.txt"
destination_name = "file_copy.txt"

with open(source_name, "r", encoding="utf-8") as source_file:
    content = source_file.read()

with open(destination_name, "w", encoding="utf-8") as destination_file:
    destination_file.write(content)

print(f"Contents copied from {source_name} to {destination_name}.")
