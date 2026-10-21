hindi=int(input("Enter your marks in Hindi: "))
english=int(input("Enter your marks in English: "))
maths=int(input("Enter your marks in Maths: "))
if hindi>=33 and english>=33 and maths>=33 and hindi+english+maths>=120:
    print("You are pass")
else:
    print("You are fail")