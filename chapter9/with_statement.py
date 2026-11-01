"""Write to and read from a file using the with statement."""

file_name = "with_demo.txt"

with open(file_name, "w", encoding="utf-8") as file:
    file.write("Hello! I am learning file handling in Python.\n")
    file.write("The with statement closes the file automatically.")

with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

print("File content:")
print(content)
