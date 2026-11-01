"""Replace every occurrence of 'Donkey' in donkey.txt."""

import re

file_name = "donkey.txt"

with open(file_name, "r", encoding="utf-8") as file:
    text = file.read()

text, replacements = re.subn(r"\bDonkey\b", "#####", text, flags=re.IGNORECASE)

with open(file_name, "w", encoding="utf-8") as file:
    file.write(text)

if replacements:
    print(f"Replaced 'Donkey' {replacements} time(s) with '#####'.")
else:
    print("The word 'Donkey' was not found in the file.")
