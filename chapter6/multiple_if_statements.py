#multiple if and elif statements
a=int(input("Enter a number: "))
if a>0:
    print("The number is positive")
if a%2==0:
    print("The number is even")

elif a<0:
    print("The number is negative")
elif a>18:
    print("eligible to vote")
else:
    print("not eligible to vote")