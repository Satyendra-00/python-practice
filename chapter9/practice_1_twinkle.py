"""Check whether poems.txt contains the word 'twinkle'."""

file_name = "poems.txt"

with open(file_name, "r", encoding="utf-8") as file:
    poem = file.read()

if "twinkle" in poem.lower():
    print("The word 'twinkle' is present in the file.")
else:
    print("The word 'twinkle' is not present in the file.")
