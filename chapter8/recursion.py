def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
fact = factorial(5)
print("Factorial of 5 is:", fact)