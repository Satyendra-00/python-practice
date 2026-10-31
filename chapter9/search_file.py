"""Find and display the lines that contain a search word."""

file_name = "file.txt"
search_word = input("Enter a word to search for: ").strip()

if not search_word:
    print("Please enter a word to search for.")
else:
    found = False
    with open(file_name, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if search_word.lower() in line.lower():
                print(f"Found on line {line_number}: {line.rstrip()}")
                found = True

    if not found:
        print(f"'{search_word}' was not found in {file_name}.")
