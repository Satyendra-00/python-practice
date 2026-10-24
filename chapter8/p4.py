def sum_of_n(n):
    if n <= 0:
        return 0
    else:
        return n + sum_of_n(n - 1)
n=int(input("Enter a positive integer: "))
print("Sum of first", n, "natural numbers is:", sum_of_n(n))