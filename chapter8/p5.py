n=int(input("Enter a value: "))
def pattern(n):
    if n==0:
        return
    print("*" * n)
    pattern(n-1)
pattern(n)