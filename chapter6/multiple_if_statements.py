#multiple if and elif statements
a=int(input("Enter a number: "))
if a > 0:
    print("The number is positive")
elif a < 0:
    print("The number is negative")
else:
    print("The number is zero")

if a % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

if a >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
