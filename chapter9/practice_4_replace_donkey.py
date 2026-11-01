"""Replace every occurrence of 'Donkey' in donkey.txt."""

file_name = "donkey.txt"

with open(file_name, "r", encoding="utf-8") as file:
    text = file.read()

text = text.replace("Donkey", "#####")

with open(file_name, "w", encoding="utf-8") as file:
    file.write(text)

print("Replaced 'Donkey' with '#####' in the file.")
