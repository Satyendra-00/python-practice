"""Append a line of text to a file."""

data = input("Enter the data to append: ").strip()

if not data:
    print("No data entered. Nothing was appended.")
else:
    with open("file.txt", "a", encoding="utf-8") as file:
        file.write(data + "\n")
    print("Data appended successfully.")
