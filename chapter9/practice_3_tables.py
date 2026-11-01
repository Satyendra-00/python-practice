"""Write multiplication tables from 2 to 20 into separate files."""

import os

folder_name = "tables"
os.makedirs(folder_name, exist_ok=True)

for number in range(2, 21):
    file_name = os.path.join(folder_name, f"table_{number}.txt")

    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Multiplication table of {number}\n")
        for multiplier in range(1, 11):
            file.write(f"{number} x {multiplier} = {number * multiplier}\n")

print("Tables from 2 to 20 have been saved in the 'tables' folder.")
