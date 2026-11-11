from datetime import date

letter = "Dear <name>,\nYou are selected.\n<date>"
name = input("Enter your name: ").strip()
today = date.today().strftime("%d %B %Y")
print(letter.replace("<name>", name).replace("<date>", today))
